screeps-starter-python
==========

This repository is a starter Python AI written for the JavaScript based MMO game, [screeps](screeps.com).

While code uploaded to the server must be in JavaScript, this repository is written in Python. We use the
[Transcrypt](transcrypt.com) transpiler to transpile the python programming into JavaScript.

This repository is intended as a base to be used for building more complex AIs, and has all the tooling needed to
transpile Python into JavaScript set up.

The `./build.sh` script does the majority of the work, from setting up a new environment to building/publishing the
binary to the screeps server. However, you will need to install some dependencies:

- `python-3.5` - Transcrypt works natively with Python 3.5, so you will need this version installed. Python 3.4 is more
  widely available, but will not work for our purposes.
- `pip` - Make sure you have a Python 3.* version of `pip` installed as well. While `pip-3.4` is fine, you do need at
  least that in order to make a `python-3.5` virtualenv. You can check your pip version with `pip --version`, and
  depending on how it was installed, you may need to use `pip3`, `pip-3`, `pip3.4` or `pip-3.4` instead.
- `node.js` - You'll need an up to date version of `node` and `npm` (node package manager) in order to use the `grunt`
  script to upload transpiled code to the screeps server.

After you have those set up, you'll need to install `virtualenv` and `grunt`:

To install virtualenv, use `pip` (or another `pip3*` / `pip-3*` command) as follows:

```
pip install --user virtualenv
```

To install grunt, use `npm` as follows:

```
npm install -g grunt-cli
```
If you have a system version of `npm`, you may need to do the following instead:
```
npm install --user -g grunt-cli
```

After that, the rest of the dependencies will be installed upon running `build.sh` for the first time.

The only remaining step will be to provide your screeps credentials. To do that, put your log in email into a file
called `.screeps-email` in this project directory, and your password into a file called `.screeps-password`.

Following that, you're all set up! All you need to do now is run the `./build.sh` script whenever you want to compile
and deploy code, and it will deal with the rest of it.

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
