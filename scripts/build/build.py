import tarfile, sys

from pathlib import Path
from shutil import rmtree, copy

from fetch_octicons import fetch_octicons
from squash_paths import squash_paths


def build(build_dir, out_dir):
    # Make clean build directory. Removes all files in this directory!
    if Path(build_dir).is_dir():
        rmtree(build_dir)
    Path(build_dir).mkdir(parents=True, exist_ok=True)
    
    version = fetch_octicons(build_dir, ".tar.gz")
    with tarfile.open(build_dir + "/octicons-" + version + ".tar.gz") as tar:
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, build_dir)
    squash_paths(build_dir + "/octicons-" + version[1:] + "/icons/", out_dir)
    
    # copy keywords
    copy(build_dir + "/octicons-" + version[1:] + "/keywords.json", out_dir + "/keywords.json")


if __name__ == "__main__":
    if 1 < len(sys.argv) <= 3:
        build(*sys.argv[1:])
    else:
	    print("Usage: python3 build.py <build directory> <output directory>")