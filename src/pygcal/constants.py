"""
constants.py
"""

# the GCP project holding the OAuth client; pass(1) entries live under gcp/<project>/
GCP_PROJECT = "pygcal-id"
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    # "https://www.googleapis.com/auth/calendar.readonly",
]
API_SERVICE_NAME = "calendar"
API_VERSION = "v3"
