"""
main entry point to the program
"""

import pylogconf.core
from pygooglehelper import register_functions, ConfigRequest
from pytconf import register_main, config_arg_parse_and_launch, register_endpoint

from pygcal.static import DESCRIPTION, APP_NAME, VERSION_STR
from pygcal.constants import SCOPES


@register_endpoint(
    description="List calendars",
)
def calendars_list() -> None:
    pass


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    ConfigRequest.app_name = APP_NAME
    ConfigRequest.scopes = SCOPES
    register_functions()
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
