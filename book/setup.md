Installing Dependencies
=======================

This repository is intended as a base to be used for building more complex AIs, and has all the tooling needed to
transpile Python into JavaScript set up.

The `./build.py` script does the majority of the work, from setting up a new environment to building/publishing the
binary to the screeps server. However, you will need to install some dependencies:

- [`git`]. On Windows, this should come with "git bash"
  which will be useful when executing commands below
- [`python-3`] - Any decently modern version of Python 3 should work.
- `pip` - This should come with most Python 3.* distributions, though if you've
   installed using a Linux package manager you may need to manually install it.
- [`node` and `npm`] - Follow instructions at https://nodejs.org/en/download/

Next, if you haven't already cloned this repository, you'll want to. Use a git
gui if you have one, or:

```
git clone https://github.com/daboross/screeps-starter-python.git
```

Finally, you'll need to install remaining node dependencies into the project
directory:

```
cd screeps-starter-python
npm install
```

[`git`]: https://git-scm.com/
[`python-3`]: https://www.python.org/downloads/
[`node` and `npm`]: https://nodejs.org/en/download/

If this all works, proceed to [Post Installation
Steps](#post-installation-steps).

Installing under Windows using 'conda'
=====================================

This section was more necessary in a previous version of the project. If you
can't get Python to work on Windows regularly, this might be helpful! Otherwise,
skip this section and proceed to [Post Installation Steps](#post-installation-steps)

For Windows users, running `build.py` may fail if `virtualenv` cannot be detected in your `PATH`.  The setup procedure here
should only be used if the primary installation method at this top of this README does not work.

This setup procedure uses `conda`, which is provided through the Python Version 3.8
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

  1. `conda create -n screeps python=3.8`
  2. `activate screeps`
  3. `conda install git`

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

Alternatively, you can use your username and password for authentication by removing the `token` entry, and adding `username` and `password` fields to `config.json`.

Following that, you're all set up! `build.py` will automatically download and install the rest of the dependencies into
a local environment when it is first run.

To run `build.py` on a Unix system (Linux, MacOS), use:

```
python3 build.py
```

To run `build.py` on Windows with raw Python installed from python.org:

```
py build.py
```
