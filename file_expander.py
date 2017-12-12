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


class FileExpander:
    """Class for managing file expansion operations.

    Attributes:
        base_dir (:obj:pathlib.Path): concrete Path object of the
            screeps-starter-python directory
        build_dir (:obj:pathlib.Path): concrete Path object of the __py_build__
            directory

    """

    def __init__(self, base_dir):
        """
        Args:
            base_dir (str): Absolute path of the screeps-starter-python
                directory
        """
        self.base_dir = pathlib.Path(base_dir).joinpath('src')
        self.build_dir = self.verify_build_directory()

    def verify_build_directory(self):
        """Verifies __py_build__, and __py_build__/defs exist.  While
        __py_build__ is simply created if it's missing, defs/ is copied directly
        from src/.

        Returns:
            (:obj:pathlib.Path): concrete Path object of the __py_build__
            directory
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

        else:
            if not self.verify_defs_integrity(defs_build_directory, defs_source_directory):
                shutil.copytree(defs_source_path, defs_build_path)

        return build_directory

    @staticmethod
    def verify_defs_integrity(build_dir, source_dir):
        """Verifies the contents of the defs file in src/defs against
        src/__py_build__/defs.  This ensures that the defs file directly under
        src/ is reflected at all times in the repository targeted by Transcrypt.

        This prevents the user from having to manually copy over the defs folder
        after updates.  Additionally, it allows them to make modifications
        locally while maintaining the correct folder structure.

        Returns:
            bool: True if all files match, else immediately returns false.

        """

        defs_source_files = [str(f.absolute()) for f in source_dir.glob('**/*.py')]
        defs_build_files = [str(f.absolute()) for f in build_dir.glob('**/*.py')]

        if len(defs_source_files) != len(defs_build_files):
            return False

        for build_file in sorted(defs_build_files):
            for src_file in sorted(defs_source_files):
                if filecmp.cmp(build_file, src_file):
                    break
            else:
                return False

        return True

    def expand_files(self):
        """Copies user generated files directly under src/, and nested in
        sub-folders under src/, to the __py_build__ folder.  Only new and/or
        modified files are copied; the original files, and their directory
        structure, are not modified.

        Returns:
            int: Total number of files copied to __py_build__
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
        """Finds all potential target files for the file expansion operation.
        Files and/or directories under the exclusions list are ignored.

        The files discovered by this method only represent objects that will be
        checked by self.expand_files() and not the final output of the copy
        operation.

        Returns:
            obj:`list` of :obj:`pathlib.Path`: All candidates for the final copy
                operation targeting __py_build__
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


def test_methods():
    base_dir = pathlib.Path(__file__).parent
    data_logger = FileExpander(base_dir)
    data_logger.expand_files()


if __name__ == "__main__":
    test_methods()
