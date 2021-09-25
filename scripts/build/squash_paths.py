import json, sys
from pathlib import Path
import xml.etree.ElementTree as ET


"""
Squashes all the svg paths in a directory into a single json.

:param root_dir: The directory containing the svgs
:type root_dir: str
:param out_dir: The directory to place octicons.json
:type out_dir: str
"""


def remove_namespace(doc, ns):
    ns = "{%s}" % ns

    for elem in doc:
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[len(ns):]


def squash_paths(root_dir, out_dir=None):
    paths = {}
    out_dir = out_dir if out_dir is not None else root_dir

    print("checking in:" + root_dir)
    for file_name in Path(root_dir).glob("*.svg"):
        print("Squashing " + str(file_name) + "...")

        svg = ET.parse(file_name).getroot()
        remove_namespace(svg, "http://www.w3.org/2000/svg")

        paths[file_name.stem] = ''.join(ET.tostring(p, encoding="unicode") for p in svg)

    with open(out_dir + "/octicons.json", "w") as f:
        json.dump(paths, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    if 1 < len(sys.argv) <= 3:
        squash_paths(*sys.argv[1:])
    else:
        print(
            "Usage: python3 squash_paths.py <directory containing svgs> *<output directory>"
        )
