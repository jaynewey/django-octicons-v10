from django import template
from django.utils.html import format_html
from json import load
from pathlib import Path

register = template.Library()

# Load the octicon path data
with open(str(Path(__file__).parent / "octicons.json"), "r") as f:
    ICON_PATHS = load(f)


class Octicon:
    """Class representing a GitHub Octicon."""

    def __init__(self, icon_name, **attributes):
        self.icon_name = icon_name
        self.attributes = attributes

        self.set_size(int(attributes.get("width", 0)), int(attributes.get("height", 0)))

        # Must check if 24px variant exists as some icons do not have 24px variant
        self.icon_size = 24 if max(self.attributes["height"], self.attributes["width"]) > 16 and ICON_PATHS.get(icon_name + "-24") else 16

        if self.get_path() is None:
            raise KeyError("Could not find data for icon '" + icon_name + "' in icon set.")

        self.attributes["class"] = self.get_classes()
        self.attributes["viewBox"] = self.get_view_box()
        self.attributes["fill"] = "currentColor"
        self.attributes["aria-hidden"] = "true"

    def set_size(self, width, height):
        if width > 0 and height > 0:
            self.attributes["width"], self.attributes["height"] = width, height
        elif width <= 0 and height <= 0:
            self.attributes["width"], self.attributes["height"] = 16, 16
        else:
            self.attributes["width"], self.attributes["height"] = max(width, height), max(width, height)

    def get_classes(self):
        return ("octicon octicon-" + self.icon_name + " " + self.attributes.get("class", "")).strip()

    def get_path(self):
        return ICON_PATHS.get(self.icon_name + "-" + str(self.icon_size))

    def get_view_box(self):
        return "0 0 " + str(self.icon_size) + " " + str(self.icon_size)

    def convert_attributes(self):
        html_attributes = ""
        for attribute, value in self.attributes.items():
            html_attributes += attribute + '="' + str(value) + '" '
        return html_attributes.strip()

    def to_svg(self):
        return "<svg " + self.convert_attributes() + ">" + self.get_path() + "</svg>"


@register.simple_tag
def octicon(icon_name, **attributes):
    """Returns a html svg element representing the desired GitHub Octicon.
    Usage e.g: {% octicon "mark-github" width="32" %}

    :param icon_name: The name of the GitHub Octicon e.g "octoface"
    :type icon_name: str
    :param attributes: The html attributes to add to the svg element
    :return: An svg element with the default and applied classes and icon path element
    """
    return format_html(Octicon(icon_name, **attributes).to_svg())
