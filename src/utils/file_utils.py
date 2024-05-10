import os
import sys


class FileUtils:
    @staticmethod
    def absolute_file_path(file_path: str) -> str:
        project_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
        return os.path.join(project_directory, file_path)
