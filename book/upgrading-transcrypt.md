Upgrading screeps-transcrypt
============================

Transcrypt occasionally updates! To provide better compilations, or to provide other fixes.

When this happens, `screeps-transcrypt`, the semi-fork of Transcrypt which includes extra changes for the Screeps environment, will also update, and an update will be pushed to this repository with a new `requirements.txt` file.

If you've already got the new `requirements.txt`, simply delete `env/` and re-run `build.py` to re-download and reinstall transcrypt. Alternatively, you can run the environment's `pip` and update it yourself:

```bash
./env/bin/pip install --upgrade -r requirements.txt
```

I believe this steps will work for both Unix and Windows users, though they have only been tested on Linux so far.
