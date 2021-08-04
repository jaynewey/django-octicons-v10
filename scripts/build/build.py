import tarfile, sys

from pathlib import Path
from shutil import rmtree

from fetch_octicons import fetch_octicons
from squash_paths import squash_paths


def build(build_dir, out_dir):
    # Make clean build directory. Removes all files in this directory!
    Path(build_dir).mkdir(parents=True, exist_ok=True)
    rmtree(Path(build_dir))
    
    version = fetch_octicons(build_dir, ".tar.gz")
    with tarfile.open(build_dir + "/octicons-" + version + ".tar.gz") as tar:
        tar.extractall(build_dir)
    squash_paths(build_dir + "/octicons-" + version[1:] + "/icons/", out_dir)


if __name__ == "__main__":
    if 1 < len(sys.argv) <= 3:
        build(*sys.argv[1:])
    else:
	    print("Usage: python3 build.py <build directory> <output directory>")