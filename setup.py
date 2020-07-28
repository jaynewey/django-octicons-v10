from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="django-octicons-v10",
    packages=find_packages(),
    package_data={"octicons_v10": ["templatetags/octicons.json"]},
    version="1.0.3",
    license="MIT",
    description="Django templatetags for GitHub Octicons v10.0.0.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Jay Newey',
    author_email="jay.newey01@gmail.com",
    url="https://github.com/jaynewey/django-octicons-v10",
    download_url="https://github.com/jaynewey/django-octicons-v10/archive/v1.0.3.tar.gz",
    keywords=["octicons", "django", "templatetags"],
    install_requires=[
        "Django~=2.2.4",
    ],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Framework :: Django",
    ],
)
