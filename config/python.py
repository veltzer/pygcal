""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "pygooglehelper",
    "google-api-python-client",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
requires = install_requires + build_requires + test_requires

scripts: dict[str,str] = {
    "pygcal": "pygcal.main:main",
}
