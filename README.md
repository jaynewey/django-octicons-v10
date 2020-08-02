# django-octicons-v10

![GitHub](https://img.shields.io/github/license/jaynewey/django-octicons-v10)
![Travis (.org)](https://img.shields.io/travis/jaynewey/django-octicons-v10)
![PyPI](https://img.shields.io/pypi/v/django-octicons-v10)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-octicons-v10)


> Django templatetags for [GitHub Octicons](https://primer.style/octicons) v10.0.0.

This library aims to provide a similar interface to the official (Jekyll, Ruby, etc.) octicon libraries provided by GitHub, but as Django templatetags.

[django-octicons](https://github.com/sanketsaurav/django-octicons) is a library that already does this, but currently for an older version of octicons.

## Installation

Install the latest version:

```
pip install django-octicons-v10
```

Place `octicons_v10` into your installed apps:

```python
INSTALLED_APPS = [
    # blah, blah, other apps...
    "octicons_v10",
]
```

## Usage

Load the `octicons` tag library in your Django template:

```
{% load octicons %}
```

Use template tags where you want to place an Octicon:

```html
{% octicon "git-branch" %}
```

### Classes

You can pass classes to your shiny new octicon:

```html
<a class="btn">
    {% octicon "git-branch" class="text-purple" %}
    Branches
</a>
```

Note: The following classes are assigned to the octicon by default:

* `octicon`
* `octicon-{ICON_NAME}`, for example `octicon-git-branch`

### Sizing

You can pass `width` or `height` or both for your desired size:

```html
<a href="#" class="Header-link">
    {% octicon "mark-github" width="32" %}
    GitHub
</a>
```

If only `width` or `height` is passed, then the other scales accordingly.

Note: The default size is 16px by 16px.
