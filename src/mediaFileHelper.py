import os
import os.path
from pathlib import Path

class MediaFileHelper:

    def __init__(self, base_path):
        self._basePath = base_path

    def getFiles(self, id):
        full_path = os.path.join(self._basePath, id)

        if os.path.isdir(full_path):
            # directory with files
            all_files = [os.path.join(full_path, f) for f in os.listdir(full_path)]
            return sorted(filter(lambda f: os.path.isfile(f), all_files))
        elif os.path.isfile(full_path):
            # single file
            return [full_path]
        else:
            # maybe a playlist?
            return self._getPlaylist(id)

    def _getPlaylist(self, id):
        playlist_path = os.path.join(self._basePath, id + ".m3u")

        if os.path.isfile(playlist_path):
            return self._parse_m3u(playlist_path)
        else:
            print("no file found for id %s", id)
            return []

    def _parse_m3u(self, path):
        m3u_dir = str(Path(path).parent)

        # make relative paths absolute
        with open(path, "r") as file:
            files = [self._normalize_path(path, m3u_dir) for path in file.readlines()]

        return files

    def _normalize_path(self, path, base_path):
        path = path.strip()

        if (os.path.isabs(path)):
            return path
        else:
            return os.path.join(base_path, path)
