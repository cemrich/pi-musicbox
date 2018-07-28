import os
import os.path
import shutil
from pathlib import Path

class MediaFileHelper:

    def __init__(self, base_path):
        self._basePath = base_path

    def copy_new(self, id):
        new_files = [filename for filename in os.listdir(self._basePath) if filename.startswith("new")]

        if not new_files:
            return

        full_path = os.path.join(self._basePath, new_files[0])
        dest_path = full_path.replace("new", id)

        #if os.path.isdir(full_path):
        shutil.move(full_path, dest_path)
        #else:
            #shutil.copy(full_path, dest_path)

    def get_files(self, id):
        prefixed_files = [filename for filename in os.listdir(self._basePath) if filename.startswith(id)]

        if prefixed_files:
            full_path = os.path.join(self._basePath, prefixed_files[0])
        else:
            print("no file found for id %s", id)
            return []

        if os.path.isdir(full_path):
            # directory with files
            all_files = [os.path.join(full_path, f) for f in os.listdir(full_path)]
            return sorted(filter(lambda f: os.path.isfile(f), all_files))
        elif full_path.endswith(".m3u") or full_path.endswith(".m3u8"):
            # playlist
            return self._parse_m3u(full_path)
        else:
            # single file
            return [full_path]

    def _parse_m3u(self, path):
        m3u_dir = str(Path(path).parent)

        # make relative paths absolute
        with open(path, "r") as file:
            files = [self._normalize_path(path, m3u_dir) for path in file.readlines()]

        return files

    def _normalize_path(self, path, base_path):
        path = path.strip()
        print(path, os.path.isabs(path))

        if (os.path.isabs(path) or "://" in path):
            return path
        else:
            return os.path.join(base_path, path)
