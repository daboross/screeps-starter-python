screeps-starter-python
==========

This repository is a starter Python AI written for the JavaScript based MMO game, [screeps](https://screeps.com).

While code uploaded to the server must be in JavaScript, this repository is written in Python. We use the
[Transcrypt](https://github.com/QQuick/Transcrypt) transpiler to transpile the python programming into JavaScript.

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


After that, the rest of the dependencies will be installed upon running `build.py` for the first time.

The only remaining step will be to provide your screeps credentials. To do that, copy `config.default.json` to
a new file `config.json`, and enter your email and password into the config.

Following that, you're all set up! All you need to do now is run `python3 build.py` to compile, collect and deploy your
code.

#### Transcrypt vs. Python:

While the program is in Python, not all python features will work natively.

Notes:
- For performance, the `in` operator has been patched to directly correspond with JavaScript's `in` operator. While this
  is faster, it means that `in` can no longer be used on lists. Instead, use `list.includes(item)`.
- Due to JavaScript's "everything is an object" architecture, negative indices won't work on arrays - resulting in
  `undefined`. Similarly, indexing past the length of the array will result in `undefined` rather than an explicit
  error. To work around this, I just use `list[len(list) - 1]` instead of `list[-1]`.
- Slicing out of bounds in an array will result in a list containing nulls. For instance, while `([1, 2, 3])[:5]` gives
  `[1, 2, 3]` in Python, it will give `[1, 2, 3, null, null]` in Transcrypt.
- `int()` does not floor values as expected - it simply parses float values. If flooring is needed, use
  `Math.floor(int(x))`.

If there is anything else you've found, do file an issue and I will include it here. Transcrypt does use the native
Python interpreter, but it doesn't replicate python perfectly. When in doubt, looking at the created `main.js` file can
provide a lot of insight into how things run.

#### Windows Setup

For Windows users, running `build.py` may fail if `virtualenv` cannot be detected in your `PATH`.  The setup procedure here
should only be used if the primary installation method at this top of this README does not work.

This setup procedure uses `conda`, which is provided through the Python Version 3.6
[Miniconda installer](https://conda.io/miniconda.html)  If you already have something like [Anaconda](https://www.anaconda.com/what-is-anaconda/) on your system, you can skip this step.  If you are new to `conda`, the [official quick start
guide](https://conda.io/docs/user-guide/getting-started.html) does a great job of covering the basics.

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
