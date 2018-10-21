Installing under Linux and MacOS
================================

This repository is intended as a base to be used for building more complex AIs, and has all the tooling needed to
transpile Python into JavaScript set up.

The `./build.py` script does the majority of the work, from setting up a new environment to building/publishing the
binary to the screeps server. However, you will need to install some dependencies:

- `python-3.5` - Transcrypt works natively with Python 3.5, so you will need this version installed. Python 3.4 is more
  widely available, but will not work for our purposes.
- `pip` - Make sure you have a Python 3.* version of `pip` installed as well. While `pip-3.4` is fine, you do need at
  least that in order to make a `python-3.5` virtualenv. You can check your pip version with `pip --version`, and
  depending on how it was installed, you may need to use `pip3`, `pip-3`, `pip3.4` or `pip-3.4` instead.

After you have those set up, you'll need to install `virtualenv`:

To install virtualenv, use `pip` (or another `pip3*` / `pip-3*` command) as follows:

```
pip install --user virtualenv
```

Installing under Windows using 'conda'
=====================================

For Windows users, running `build.py` may fail if `virtualenv` cannot be detected in your `PATH`.  The setup procedure here
should only be used if the primary installation method at this top of this README does not work.

This setup procedure uses `conda`, which is provided through the Python Version 3.6
[Miniconda installer](https://conda.io/miniconda.html)  If you already have something like
[Anaconda](https://www.anaconda.com/what-is-anaconda/) on your system, you can skip this step.
If you are new to `conda`, the [official quick start guide](https://conda.io/docs/user-guide/getting-started.html) does a
great job of covering the basics.

While Miniconda will install its own version of Python to your system, you do not need to modify or uninstall any version
already in place.  The installer will ask if you want Miniconda to be used as your default version of Python; if you plan to
use conda only for screeps, you can decline.

Once the installation is complete, look for a program icon labeled `Anaconda Prompt` and run it.  All commands listed for the
rest of the guide must be entered in the terminal created by `Anaconda Prompt`.

Enter the following commands in the order listed:

  1. `conda create -n screeps python=3.5`
  2. `activate screeps`
  3. `conda install git`
  4. `conda install -c anaconda virtualenv`

Once finished, you can now try `python build.py` again.

To transpile your Python code to JavaScript, `build.py` must be called from an Anaconda Prompt using the `screeps`
environment; this can be achieved through the following steps:

  1. Open an Anaconda Prompt
  2. enter the command: `activate screeps`

The above steps only need to be performed when opening a new Anaconda Prompt, you can keep it running in the background while
you make changes to your code and switch to it only when you need to run `build.py`.  To deactivate the `screeps`
environment, you can either enter the command `deactivate screeps`, or you can close the prompt itself.

Post Installation Steps
=======================

The last step to setting up `screeps-game-api` is to create and configure the build. This will allow `build.py` to
upload files directly to the screeps server after building.

Copy the contents of `config.default.json` into `config.json`. [Generate an auth-token](https://docs.screeps.com/auth-tokens.html#Using-Auth-Tokens) with full access rights through your screep's account management page.  Existing tokens with a matching access level can also be used.  Copy the token and paste it to the `token` key in `config.json`.

Following that, you're all set up! `build.py` will automatically download and install the rest of the dependencies into
a local environment when it is first run.

All you need to do now is run `build.py` to compile, collect and deploy your code.
