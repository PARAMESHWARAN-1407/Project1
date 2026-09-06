import os
import shutil
import stat
from git import Repo


class ATLAS:

    def __init__(self):

        self.repo_path = "cloned_repo"

    # -----------------------------------
    # FORCE DELETE READ-ONLY FILES
    # -----------------------------------

    def remove_readonly(self, func, path, _):

        os.chmod(path, stat.S_IWRITE)

        func(path)

    # -----------------------------------
    # CLONE REPOSITORY
    # -----------------------------------

    def clone_repo(self, repo_url):

        # DELETE OLD REPO SAFELY

        if os.path.exists(self.repo_path):

            shutil.rmtree(
                self.repo_path,
                onerror=self.remove_readonly
            )

        # CLONE NEW REPO

        Repo.clone_from(repo_url, self.repo_path)

        return {
            "status": "cloned"
        }

    # -----------------------------------
    # SCAN FILES
    # -----------------------------------

    def scan_files(self):

        allowed = [
            ".py",
            ".js",
            ".ts",
            ".json",
            ".md"
        ]

        files = []

        for root, _, filenames in os.walk(self.repo_path):

            for file in filenames:

                if any(file.endswith(ext) for ext in allowed):

                    files.append(
                        os.path.join(root, file)
                    )

        return files

    # -----------------------------------
    # READ FILES
    # -----------------------------------

    def read_files(self):

        files = self.scan_files()

        contents = {}

        for file in files[:20]:

            try:

                with open(file, "r", encoding="utf-8") as f:

                    contents[file] = f.read()[:1000]

            except:
                pass

        return contents

    # -----------------------------------
    # QUERY
    # -----------------------------------

    def query(self, text):

        files = self.read_files()

        matches = {}

        for file, content in files.items():

            if text.lower() in content.lower():
matches
                matches[file] = content[:500]

        return 