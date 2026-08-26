"""
Build hook that refuses to build a distribution without client_secret.json.

The file is gitignored (GitHub push protection rejects Google OAuth
secrets), so a fresh clone does not have it. Without this guard, hatchling
would silently omit it and produce a package that fails at first run for
every user.

To build a release, put the credential at src/pygcal/client_secret.json
(or point PYGCAL_CLIENT_SECRET at it).
"""

import os
import shutil

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

CLIENT_SECRET = os.path.join("src", "pygcal", "client_secret.json")


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        target = os.path.join(self.root, CLIENT_SECRET)
        if not os.path.isfile(target):
            source = os.environ.get("PYGCAL_CLIENT_SECRET")
            if source and os.path.isfile(source):
                os.makedirs(os.path.dirname(target), exist_ok=True)
                shutil.copyfile(source, target)
            else:
                raise RuntimeError(
                    f"missing {CLIENT_SECRET}\n"
                    "It is gitignored, so a fresh clone will not have it.\n"
                    "Copy the credential there, or set PYGCAL_CLIENT_SECRET "
                    "to its path, before building."
                )
