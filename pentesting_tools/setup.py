#!/bin/env python3

from pathlib import Path


# ========================================================================

# 1. Defining the names of the folders I am gonna create in the script

scripts = ["script.py", "main.py", "modules.py"]
recon = ["script.sh", "dirListing.sh"]
post_exploitation = ["main.js", "xss.js"]

DIR_STRUCTURE = {"scripts": scripts, "recon": recon, "post_exploitation": post_exploitation}

# ========================================================================

# 2. Create the contents to be written in the files
py_contents = ("#!/bin/env python3\n\n"
               "from pathlib import Path\n\n"
               "print(\"This is a python script\")\n")

sh_contents = ("#!/bin/env bash\n\n"
               "echo \"Hello, this is a bash script\"\n")

js_contents = "I don't know the JavaScriptin programming language, so...\n"

extension_mapping = {".py": py_contents, ".sh": sh_contents, ".js": js_contents}

# ========================================================================


def write_contents(file_path, file):
    for extension, contents in extension_mapping.items():
        if file.endswith(f"{extension}"):
            with open(file_path, "w") as f:
                f.write(contents)


def file_creation(dir_path, files):
    for file in files:
        file_path = dir_path / file
        file_path.touch(mode=0o700)
        write_contents(file_path, file)


def dir_creation():
    for directory, files in DIR_STRUCTURE.items():
        dir_path = Path.cwd() / directory
        dir_path.mkdir()
        file_creation(dir_path, files)



def main():
    dir_creation()


if __name__ == "__main__":
    main()
