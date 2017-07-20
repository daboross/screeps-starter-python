#!/usr/bin/env python3
import errno
import json
import subprocess
import sys
import urllib.parse
import urllib.request

import base64
import os
import shutil

transcrypt_arguments = ['-n', '-b', '-p', '.none']


def possible_transcrypt_binary_paths(config):
    """
    Finds all different places to look for a `transcrypt` binary to run.

    :type config: Configuration
    """
    return [
        os.path.join(config.base_dir, 'env', 'bin', 'transcrypt'),
        os.path.join(config.base_dir, 'env', 'bin', 'transcrypt.exe'),
        shutil.which('transcrypt'),
        shutil.which('transcrypt.exe'),
    ]


def possible_pip_binary_paths(config):
    """
    Finds all different places to look for a `pip` binary to run.

    :type config: Configuration
    """
    files = [
        os.path.join(config.base_dir, 'env', 'bin', 'pip'),
        os.path.join(config.base_dir, 'env', 'bin', 'pip.exe'),
    ]
    if not config.enter_env:
        for path in [shutil.which('pip'), shutil.which('pip.exe')]:
            if path is not None:
                files.append(path)

    return files


class Configuration:
    """
    Utility struct holding all configuration values.

    :type base_dir: str
    :type username: str
    :type password: str
    :type branch: str
    :type ptr: bool
    """

    def __init__(self, base_dir, config_json):
        """
        :type base_dir: str
        :type config_json: dict[str, str | bool]
        """
        self.base_dir = base_dir
        self.username = config_json.get('username') or config_json.get('email')
        self.password = config_json['password']
        self.branch = config_json.get('branch', 'default')
        self.ptr = config_json.get('ptr', False)
        self.enter_env = config_json.get('enter-env', True)

    def transcrypt_executable(self):
        """
        Utility method to find a transcrypt executable file.

        :rtype: str
        """
        for path in possible_transcrypt_binary_paths(self):
            if path is not None and os.path.exists(path):
                return path
        return None

    def pip_executable(self):
        """
        Utility method to find a pip executable file.

        :rtype: str
        """
        for path in possible_pip_binary_paths(self):
            if path is not None and os.path.exists(path):
                return path
        return None


def load_config(base_dir):
    """
    Loads the configuration from the `config.json` file.

    :type base_dir: str
    :rtype: Configuration
    """
    config_file = os.path.join(base_dir, 'config.json')

    with open(os.path.join(base_dir, config_file)) as f:
        config_json = json.load(f)

    return Configuration(base_dir, config_json)


def run_transcrypt(config):
    """
    Compiles source code using the `transcrypt` program.

    :type config: Configuration
    """
    transcrypt_executable = config.transcrypt_executable()
    source_main = os.path.join(config.base_dir, 'src', 'main.py')

    args = [transcrypt_executable] + transcrypt_arguments + [source_main]
    source_dir = os.path.join(config.base_dir, 'src')

    ret = subprocess.Popen(args, cwd=source_dir).wait()

    if ret != 0:
        raise Exception("transcrypt failed. exit code: {}. command line '{}'. working dir: '{}'."
                        .format(ret, "' '".join(args), source_dir))


def copy_artifacts(config):
    """
    Copies compiled JavaScript files to output directory after `transcrypt` has been run.

    :type config: Configuration
    """
    dist_directory = os.path.join(config.base_dir, 'dist')

    try:
        os.makedirs(dist_directory)
    except OSError as e:
        if e.errno == errno.EEXIST:
            shutil.rmtree(dist_directory)
            os.makedirs(dist_directory)
        else:
            raise

    shutil.copyfile(os.path.join(config.base_dir, 'src', '__javascript__', 'main.js'),
                    os.path.join(dist_directory, 'main.js'))

    js_directory = os.path.join(config.base_dir, 'js_files')

    if os.path.exists(js_directory) and os.path.isdir(js_directory):
        for name in os.listdir(js_directory):
            source = os.path.join(js_directory, name)
            dest = os.path.join(dist_directory, name)
            shutil.copy2(source, dest)


def build(config):
    """
    Compiles source code, and copies JavaScript files to output directory.

    :type config: Configuration
    """
    print("running transcrypt...")
    run_transcrypt(config)
    print("copying artifacts...")
    copy_artifacts(config)
    print("build successful.")


def upload(config):
    """
    Uploads JavaScript files found in the output directory to the Screeps server.

    :type config: Configuration
    """

    module_files = {}

    dist_dir = os.path.join(config.base_dir, 'dist')

    for file_name in os.listdir(dist_dir):
        with open(os.path.join(dist_dir, file_name)) as f:
            module_files[os.path.splitext(file_name)[0]] = f.read()

    if config.ptr:
        post_url = 'https://screeps.com/ptr/api/user/code'
    else:
        post_url = 'https://screeps.com/api/user/code'

    post_data = json.dumps({'modules': module_files, 'branch': config.branch}).encode('utf-8')

    auth_pair = config.username.encode('utf-8') + b':' + config.password.encode('utf-8')

    headers = {
        'Content-Type': b'application/json; charset=utf-8',
        'Authorization': b'Basic ' + base64.b64encode(auth_pair),
    }
    request = urllib.request.Request(post_url, post_data, headers)

    print("uploading files to branch {}{}...".format(config.branch, " on PTR" if config.ptr else ""))

    # any errors will be thrown.
    with urllib.request.urlopen(request) as response:
        decoded_data = response.read().decode('utf-8')
        json_response = json.loads(decoded_data)
        if not json_response.get('ok'):
            if 'error' in json_response:
                raise Exception("upload error: {}".format(json_response['error']))
            else:
                raise Exception("upload error: {}".format(json_response))

    print("upload successful.")


def install_env(config):
    """
    Creates a virtualenv environment in the `env/` folder, and attempts to install `transcrypt` into it.

    If `enter-env` is False in the `config.json` file, this will instead install `transcrypt`
    into the default location for the `pip` binary which is in the path.

    :type config: Configuration
    """
    if config.transcrypt_executable() is not None:
        return
    if config.enter_env:
        env_dir = os.path.join(config.base_dir, 'env')

        if not os.path.exists(env_dir):
            print("creating virtualenv environment...")
            if sys.version_info >= (3, 5):
                args = ['virtualenv', '--system-site-packages', env_dir]
            else:
                args = ['virtualenv', '-p', 'python3.5', '--system-site-packages', env_dir]

            ret = subprocess.Popen(args, cwd=config.base_dir).wait()

            if ret != 0:
                raise Exception("virtualenv failed. exit code: {}. command line '{}'. working dir: '{}'."
                                .format(ret, "' '".join(args), config.base_dir))

        if not os.path.exists(os.path.join(env_dir, 'bin', 'transcrypt')):
            print("installing transcrypt into env...")

            requirements_file = os.path.join(config.base_dir, 'requirements.txt')

            pip_executable = config.pip_executable()

            if not pip_executable:
                raise Exception("pip binary not found at any of {}".format(possible_pip_binary_paths(config)))

            install_args = [pip_executable, 'install', '-r', requirements_file]

            ret = subprocess.Popen(install_args, cwd=config.base_dir).wait()

            if ret != 0:
                raise Exception("pip install failed. exit code: {}. command line '{}'. working dir: '{}'."
                                .format(ret, "' '".join(install_args), config.base_dir))

    else:
        if not shutil.which('transcrypt'):
            print("installing transcrypt using 'pip'...")

            requirements_file = os.path.join(config.base_dir, 'requirements.txt')

            pip_executable = config.pip_executable()

            if not pip_executable:
                raise Exception("pip binary not found at any of {}".format(possible_pip_binary_paths(config)))

            install_args = [pip_executable, 'install', '-r', requirements_file]

            ret = subprocess.Popen(install_args, cwd=config.base_dir).wait()

            if ret != 0:
                raise Exception("pip install failed. exit code: {}. command line '{}'. working dir: '{}'."
                                .format(ret, "' '".join(install_args), config.base_dir))


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config = load_config(base_dir)

    install_env(config)
    build(config)
    upload(config)


if __name__ == "__main__":
    main()
