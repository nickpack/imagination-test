__author__ = 'nickp666'

from setuptools import setup, find_packages
setup(
    name = "PopularNames",
    version = "0.1",
    packages = find_packages(),
    scripts = ['popular_names.py'],
    license = "MIT",
    entry_points = {
        "console_scripts": [
            "popular-names = popular_names:main",
        ],
    }
)