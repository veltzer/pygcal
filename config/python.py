""" python depedencies for this project """
from typing import List

console_scripts: List[str] = [
    "pygcal=pygcal.main:main",
]

dev_requires: List[str] = [
    "pypitools",
    "black",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pygooglehelper",
    "google-api-python-client",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pytest",
    "pytest-cov",
    "flake8",
    "pylint",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
