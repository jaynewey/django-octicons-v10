![octicons cover light](https://user-images.githubusercontent.com/54012/138925195-5779c51d-ff8c-4264-a914-e64f4843893d.png#gh-light-mode-only)
![octicons cover dark](https://user-images.githubusercontent.com/54012/138925203-80e1afa1-ba54-4731-9525-3c41186663f9.png#gh-dark-mode-only)

# django-octicons-v10

![GitHub](https://img.shields.io/github/license/jaynewey/django-octicons-v10)
[![.github/workflows/main.yml](https://github.com/jaynewey/django-octicons-v10/actions/workflows/main.yml/badge.svg)](https://github.com/jaynewey/django-octicons-v10/actions/workflows/main.yml)
![PyPI](https://img.shields.io/pypi/v/django-octicons-v10)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-octicons-v10)
[![Downloads](https://pepy.tech/badge/django-octicons-v10)](https://pepy.tech/project/django-octicons-v10)

> Django templatetags for [GitHub Octicons](https://primer.style/octicons) v10.0.0+.

Current version `v4.1.0` supports [Octicons v16.1.0](https://github.com/primer/octicons/releases/tag/v16.1.0).

This library aims to provide a similar interface to the official JavaScript and Ruby octicon libraries provided by GitHub, but as Django templatetags.

[django-octicons](https://github.com/sanketsaurav/django-octicons) is a library that already does this, but currently for an older version of octicons.

## Installation

Install the latest version:

```
pip3 install django-octicons-v10
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

### 16px and 24px variants

The icon variant chosen is dependent on the size specified. If either your width or height is more than 16, then the 24px variant will be chosen.

#### What if I want to specify a variant regardless of size?

If say, you wanted a 32 width icon, but wanted to use the 16px variant, you can do so by specifying the whole variant name, in the form `{ICON_NAME}-{ICON_SIZE}`:

```{% octicon "alert-16" width="32" %}```

### Keywords

Octicons provides a list of keywords for each icon. You can get an `Octicon` instance's keywords by accessing its `keywords` attribute:

```python
>>> octicon = Octicon("octoface")
>>> octicon.keywords
['octocat', 'brand']
```

---

When using the GitHub logos, be sure to follow the [GitHub logo guidelines](https://github.com/logos).

## Issues

Please use the [GitHub issue tracker](https://github.com/jaynewey/django-octicons-v10/issues) to track issues.

## Contributing

Contributions are welcome. Please send a pull request through and explain the reasoning behind the change.

### Building

To automatically pull the latest versions of octicons, run:

```sh
python3 scripts/build/build.py build octicons_v10/templatetags
```

In the root folder of the repository.

