""" python deps for this project """

scripts: dict[str,str] = {
    "pygcal": "pygcal.main:main",
}

config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pygooglehelper",
    "google-api-python-client",
]
build_requires: list[str] = [
    "hatch",
    "pydmt",
    "pymakehelper",
    "pycmdtools",
]
test_requires: list[str] = [
    "pytest",
    "pylint",
    "mypy",
    "ruff",
]
requires = config_requires + install_requires + build_requires + test_requires
