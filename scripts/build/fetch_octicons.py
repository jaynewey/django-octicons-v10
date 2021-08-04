import requests, sys
from pathlib import Path


LATEST_RELEASE_URL = "https://github.com/primer/octicons/releases/latest"
RELEASES_URL = "https://github.com/primer/octicons/archive/refs/tags/"


"""
Downloads the specified version of Octicons in the specified format. (.tar.gz or .zip).
If no version specified, downloads latest version.

:param fmt: The format, `.tar.gz` or `.zip`
:type fmt: str
:param version: The version name in the format 'vX.X.X' or 'latest'
:type version: str
:return: The version of octicons
"""
def fetch_octicons(out_dir, fmt, version="latest"):
    if version == "latest":
        version = (requests.get(LATEST_RELEASE_URL).url).split("/")[-1]
    
    r = requests.get(RELEASES_URL + version + fmt)
    out_tar = str(Path(out_dir) / ("octicons-" + version + ".tar.gz"))
    
    with open(out_tar, "wb") as f:
        f.write(r.content)
    
    return version

if __name__ == "__main__":
    if 1 < len(sys.argv) <= 4:
        fetch_octicons(*sys.argv[1:])
    else:
	    print("Usage: python3 fetch_octicons.py <output directory> <format (.tar.gz / zip)> *<version>")
  
    