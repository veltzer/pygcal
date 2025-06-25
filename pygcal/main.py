"""
main entry point to the program
"""

import pylogconf.core
from pygooglehelper import register_functions, ConfigRequest, get_credentials
from pytconf import register_main, config_arg_parse_and_launch, register_endpoint
import googleapiclient

from pygcal.static import DESCRIPTION, APP_NAME, VERSION_STR
from pygcal.constants import SCOPES, API_SERVICE_NAME, API_VERSION


def get_api():
    ConfigRequest.scopes = SCOPES
    ConfigRequest.app_name = APP_NAME
    credentials = get_credentials()
    return googleapiclient.discovery.build(
        serviceName=API_SERVICE_NAME,
        version=API_VERSION,
        credentials=credentials,
        cache_discovery=False,
    )


@register_endpoint(
    description="List calendars",
)
def calendars_list() -> None:
    api = get_api()
    print("Getting the list of calendars...")
    # pylint: disable=no-member
    calendars_result = api.calendarList().list().execute()
    calendars = calendars_result.get("items", [])

    if not calendars:
        print("No calendars found.")
        return

    print("Your Calendars:")
    for calendar in calendars:
        summary = calendar.get("summary", "No Title")
        calendar_id = calendar["id"]
        print(f"- {summary} (ID: {calendar_id})")


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
