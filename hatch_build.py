"""
Build hook that supplies client_secret.json to the distribution.

The credential is deliberately not in the repo: GitHub push protection
rejects Google OAuth secrets, and publicly scanned ones get reported to
Google and revoked. But it must ship inside the package so that a plain
`pip install pygcal` works with no user setup.

So the build copies it in from outside the tree, trying in order:

  1. $PYGCAL_CLIENT_SECRET  -- for release automation (CI secret -> file)
  2. ~/.config/pygcal/client_secret.json  -- the usual developer location
  3. src/pygcal/client_secret.json  -- already in place, left alone

If none is found the build fails loudly. Without that, hatchling would
silently omit the file and produce a package that breaks on first run for
every user.
"""

import os
import shutil

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

CLIENT_SECRET = os.path.join("src", "pygcal", "client_secret.json")
CONFIG_LOCATION = os.path.expanduser("~/.config/pygcal/client_secret.json")


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        target = os.path.join(self.root, CLIENT_SECRET)
        if os.path.isfile(target):
            return

        for source in (os.environ.get("PYGCAL_CLIENT_SECRET"), CONFIG_LOCATION):
            if source and os.path.isfile(source):
                os.makedirs(os.path.dirname(target), exist_ok=True)
                shutil.copyfile(source, target)
                # Not part of the source tree; do not leave it behind.
                build_data["artifacts"].append(f"/{CLIENT_SECRET}")
                return

        raise RuntimeError(
            f"missing {CLIENT_SECRET}\n"
            f"It is not kept in the repo. Put the credential at "
            f"{CONFIG_LOCATION},\n"
            "or set PYGCAL_CLIENT_SECRET to its path, before building."
        )
