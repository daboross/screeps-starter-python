"""File Expansion of Nested screeps Source Code.

This package provides file expansion operations that targets screeps code
written in Python in order to allow files to be organized in a nested directory
structure.

Every time Transcrypt is run, user generated .py source code will be copied so
that they all sit directly under __py_build__.  Only new/updated files will
actually be copied; unmodified files are not replaced in __py_build__. Files can
reside directly under src/, or in subdirectories under src/.

The -xpath option available through Transcrypt already provides this
functionality; this package serves as a replacement for anyone experiencing
problems with Transcrypt recognizing python modules stored in sub-folders, or
for those looking for an alternative to -xpath itself."""

import pathlib
import shutil
import filecmp

from datetime import datetime


class FileExpander:
    """Class for managing file expansion operations.

        :type base_dir: pathlib.Path
        :type build_dir: pathlib.Path
    """

    def __init__(self, base_dir):
        """
        :param base_dir: absolute path of the screeps-starter-python directory
        :type base_dir: str

        """
        self.base_dir = pathlib.Path(base_dir).joinpath('src')
        self.build_dir = self.verify_build_directory()

    def verify_build_directory(self):
        """Verifies existence and contents of __py_build__ directory.

        Missing directories are either created, or copied from its counterpart
        in src/""

        :return: concrete Path object of the __py_build__ directory
        :rtype: pathlib.Path
        """

        build_directory = self.base_dir.joinpath('__py_build__')

        defs_source_directory = self.base_dir.joinpath('defs')
        defs_build_directory = build_directory.joinpath('defs')

        defs_source_path = str(defs_source_directory.absolute())
        defs_build_path = str(defs_build_directory.absolute())

        if not build_directory.is_dir():
            build_directory.mkdir(exist_ok=True)

        if not defs_build_directory.is_dir():
            shutil.copytree(defs_source_path, defs_build_path)

        self.verify_defs_integrity(defs_source_directory, build_directory)

        return build_directory

    @staticmethod
    def verify_defs_integrity(source_dir, build_dir):
        """Verifies integrity of defs/ folder in __py_build__

        File contents under src/defs are compared against __py_build__/defs; a
        file update will only be triggered by modifications to files under
        src/defs.

        :rtype: None
        """

        defs_source_files = [f.absolute() for f in source_dir.glob('**/*.py')]

        for file in defs_source_files:
            slice_index = file.parts.index('src') + 1
            partner = build_dir.joinpath(*file.parts[slice_index:])

            if not partner.is_file() or not filecmp.cmp(str(file), str(partner)):
                shutil.copy2(str(file), str(partner))

    def expand_files(self):
        """Creates a flattened file structure of all user-defined screeps code

        Copies all modified or new .py files found directly under src/, or in
        subdirectories under src/, to __py_build__.

        :return: total number of files copied to __py_build__
        :rtype: int
        """

        target_files = self.find_target_file_paths()

        copied_files = 0
        for target in target_files:
            partner = self.build_dir.joinpath(target.name)

            target_path, partner_path = str(target.absolute()), str(partner.absolute())

            if not (partner.is_file() and filecmp.cmp(target_path, partner_path)):
                shutil.copy2(target_path, partner_path)
                copied_files += 1

        return copied_files

    def find_target_file_paths(self):
        """Finds all potential target files for the file expansion operation

        :return: All files to be checked by self.expand_files
        :rtype: list[pathlib.Path]
        """

        exclusions = [
            '__pycache__',
            '__javascript__',
            '__py_build__',
            '.idea',
            '.git',
            'defs'
        ]

        target_files, target_directories = [], []
        for file_object in self.base_dir.iterdir():

            if not any(entry in file_object.name for entry in exclusions):
                if file_object.is_file():
                    target_files.append(file_object)
                else:
                    target_directories.append(file_object)

        # Directories processed separately to avoid performing glob on all of src/
        for directory in target_directories:
            for file in directory.glob('**/*.py'):
                target_files.append(file)

        return target_files

