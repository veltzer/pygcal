"""
constants.py
"""

# the GCP project holding the OAuth client; pass(1) entries live under gcp/<project>/
GCP_PROJECT = "veltzer-pygcal-id"
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
]
API_SERVICE_NAME = "calendar"
API_VERSION = "v3"
