# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `hatch_build.py:26` - the build pulls the Google OAuth client secret from a plaintext `~/.config/pygcal/client_secret.json`, a second secret store outside pass(1). Keep the credential in pass and have the release step materialize it at build time (e.g. `PYGCAL_CLIENT_SECRET=<(pass show pygcal/client_secret)` or a temp file from `pass show`), then drop the `~/.config` fallback.
- `rsconstruct.toml:27-32` - `hatch_build.py` sits at the repo root, outside `src_dirs = ["src", "config", "tests"]`, so neither ruff nor mypy ever checks the build hook that gates every release. Add `src_files = ["hatch_build.py"]` to both processors (and `hatchling` to the dev group so mypy can resolve its import).
- `src/pygcal/configs.py:7-13` - `ConfigPagination.page_size` is never used: no endpoint registers it and the `calendarList().list()` calls (`main.py:37,55,70`) pass no `maxResults`. Either wire it in or delete `configs.py`.
- `src/pygcal/main.py:34-41,51-59,67-80` - the same pagination loop is copied into all three endpoints. Factor it into one `list_all_calendars(api)` helper.

## Low

- `src/pygcal/main.py:42` - `sorted(..., key=lambda cal: cal.get("summary"))` raises `TypeError` if any entry lacks a summary (None vs str); use `cal.get("summary", "")`.
- `src/pygcal/main.py:18-19` - `get_api()` re-sets `ConfigRequest.scopes`/`location`, which `main()` already sets at lines 90-91; keep one.
- `pyproject.toml:15` - description "Do stuff with google calendar" has drifted from `config/project.lua:2` ("Do various things with google calendar"); align them.
- `pyproject.toml:109-110` - `pylogconf` and `pytconf` are repeated in the dev group though they are already runtime dependencies (lines 36-37); remove them from `dev`.
- `pyproject.toml:87` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/`, which do not exist here (same line in 82 fleet pyproject files); set `"src"`.
- `doc/TODO.txt`, `doc/DONE.txt` - both empty; delete them.
