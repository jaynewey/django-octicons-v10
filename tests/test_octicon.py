import pytest
from octicons_v10.templatetags.octicons import Octicon


def test_init():
    assert Octicon("zap")
    assert Octicon("zap", **{"class": "text-center"})


def test_detect_icon_missing():
    with pytest.raises(KeyError) as key_error:
        Octicon("missing-icon-name")

    assert str(key_error.value) == '"Could not find data for icon \'missing-icon-name\' in icon set."'


def test_correct_classes():
    octicon = Octicon("zap", **{"class": "text-center test-class"})
    assert octicon.attributes["class"] == "octicon octicon-zap text-center test-class"


def test_view_box():
    assert Octicon("zap").attributes["viewBox"] == "0 0 16 16"
    assert Octicon("zap", **{"width": "12"}).attributes["viewBox"] == "0 0 16 16"
    assert Octicon("zap", **{"height": "12"}).attributes["viewBox"] == "0 0 16 16"
    assert Octicon("zap", **{"width": "32"}).attributes["viewBox"] == "0 0 24 24"
    assert Octicon("zap", **{"height": "32"}).attributes["viewBox"] == "0 0 24 24"
    assert Octicon("zap", **{"width": "32", "height": "16"}).attributes["viewBox"] == "0 0 24 24"
    assert Octicon("zap", **{"width": "32"}).attributes["viewBox"] == "0 0 24 24"


def test_width():
    assert Octicon("zap").attributes["width"] == 16
    assert Octicon("zap", **{"width": 36}).attributes["width"] == 36
    assert Octicon("zap", **{"height": 36}).attributes["width"] == 36
    assert Octicon("zap", **{"width": 24, "height": 36}).attributes["width"] == 24


def test_height():
    assert Octicon("zap").attributes["height"] == 16
    assert Octicon("zap", **{"height": 36}).attributes["height"] == 36
    assert Octicon("zap", **{"width": 36}).attributes["height"] == 36
    assert Octicon("zap", **{"width": 36, "height": 24}).attributes["height"] == 24


def test_aria_hidden():
    assert Octicon("zap").attributes["aria-hidden"] == "true"
    assert Octicon("zap", **{"class": "test-class"}).attributes["aria-hidden"] == "true"


def test_convert_attributes():
    attributes = Octicon("zap", **{"style": "color: #ffffff;"}).convert_attributes()
    assert 'class="octicon octicon-zap"' in attributes
    assert 'width="16"' in attributes
    assert 'height="16"' in attributes
    assert 'viewBox="0 0 16 16"' in attributes
    assert 'aria-hidden="true"' in attributes
    assert 'fill="currentColor"' in attributes
    assert 'style="color: #ffffff;"' in attributes
