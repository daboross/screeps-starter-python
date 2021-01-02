Software Setup
==============

This repository is intended as a base to be used for building more complex AIs, and has all the tooling needed to
transpile Python into JavaScript set up.

The `./build.py` script does the majority of the work. It sets up the python
environment, and installs all dependencies. However, you will still need some
base software installed:

- [`git`]
- [`python`] version 3.7 or above
- [`node.js`]
- `npm`


### Linux Software Install

Your Linux distribution should have python installed. Use your package manager
(`apt`, `dnf`, etc.) to install `git`, `node` and `npm`.

### MacOS Software Setup

Using [homebrew], install `git`, `python` and `node` (`npm` comes with `node`):

```
brew install git python@3 node
```

### Windows Software Setup

Install git from https://git-scm.com/download/win. Default options are fine.

Install the latest version of Python from https://www.python.org/downloads/.
Again, default options should be fine.

Install node.js LTS Windows Installer from https://nodejs.org/en/download/.
Default options should again be fine.

Start "git bash" to start a terminal for the next step.

[`git`]: https://git-scm.com/
[`python-3`]: https://www.python.org/downloads/
[`node.js`]: https://nodejs.org/en/download/
[homebrew]: https://brew.sh/


Repository Setup
================

Next, if you haven't already cloned this repository, you'll want to. Use a git
gui if you have one, or:

```
git clone https://github.com/daboross/screeps-starter-python.git
```

Next, you'll want to open this repository in your file manager, copy
`config.default.json` to `config.json` and proceed to [Post Installation
Steps](#post-installation-steps)


Post Installation Steps
=======================

The last step to setting up `screeps-game-api` is to create and configure the
build. This will allow `build.py` to upload files directly to the screeps server
after building.

Copy the contents of `config.default.json` into `config.json`. [Generate an
auth-token](https://docs.screeps.com/auth-tokens.html#Using-Auth-Tokens) with
full access rights through your screep's account management page, then copy the
token and paste it to the `token` key in `config.json`.

Alternatively, you can use your username and password for authentication. To
do this, remove the `token` line, and add `username` and `password` fields to
`config.json`. Be careful about commas - all lines except the last should have
trailing commas.

Deploying to Screeps
====================

Following that, you're all set up! `build.py` will automatically download and
install the rest of the dependencies into a local environment when it is first
run.

To run `build.py` on a Unix system (Linux, MacOS), use:

```
python3 build.py
```

To run `build.py` on Windows with raw Python installed from python.org:

```
py build.py
```

On first run, this will install remaining dependencies, then compile, build, and
deploy your code to Screeps! On subsequent runs, it will simply call installed
tools and deploy code from there.

Installing under Windows using 'conda'
=====================================

If you're having trouble running `build.py` in Windows, it might be worth trying
out an alternative installation method.

For Windows users, running `build.py` may fail if `virtualenv` cannot be
detected in your `PATH`.  The setup procedure here should only be used if the
primary installation method at this top of this README does not work.

This setup procedure uses `conda`, which is provided through the  [Miniconda
installer](https://conda.io/miniconda.html)  If you already have something
like [Anaconda](https://www.anaconda.com/what-is-anaconda/) on your system,
you can skip this step. If you are new to `conda`, the [official quick start
guide](https://conda.io/docs/user-guide/getting-started.html) does a great job
of covering the basics.

While Miniconda will install its own version of Python to your system, you do
not need to modify or uninstall any version already in place. The installer
will ask if you want Miniconda to be used as your default version of Python;
if you plan to use conda only for screeps, you can decline.

Once the installation is complete, look for a program icon labeled `Anaconda
Prompt` and run it.  All commands listed for the rest of the guide must be
entered in the terminal created by `Anaconda Prompt`.

Enter the following commands in the order listed:

  1. `conda create -n screeps python=3.8`
  2. `activate screeps`
  3. `conda install git`

Once finished, you can now try `python build.py` again.

To transpile your Python code to JavaScript, `build.py` must be called from an
Anaconda Prompt using the `screeps` environment; this can be achieved through
the following steps:

  1. Open an Anaconda Prompt
  2. enter the command: `activate screeps`

The above steps only need to be performed when opening a new Anaconda Prompt,
you can keep it running in the background while you make changes to your code
and switch to it only when you need to run `build.py`.  To deactivate the
`screeps` environment, you can either enter the command `deactivate screeps`,
or you can close the prompt itself.
