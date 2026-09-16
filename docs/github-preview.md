# GitHub preview: v0.1.0-preview.1

This prerelease pairs gramlot-django 0.1.0 with a compatible Gramlot 0.1.5
candidate. Neither version is published on PyPI as part of this release.

## Installation

Create and activate a Python 3.11+ virtual environment, then run:

```sh
python -m pip install \
  'https://github.com/gramlot-org/gramlot-django/releases/download/v0.1.0-preview.1/gramlot-0.1.5-py3-none-any.whl#sha256=63466802618c8cbd3fed0a83e1072556085a31bd522477dbcfe1122417a26f4a' \
  'git+https://github.com/gramlot-org/gramlot-django.git@v0.1.0-preview.1'
gramlot-django demo --open
```

Git is needed for the source installation above. Alternatively, install both
wheels from the same GitHub prerelease together with `python -m pip install`.
The runtime is prebuilt: Node.js is not required. Polls is bundled; Bakery needs
the repository example and its separate dependencies; see [Bakery](bakery-demo.md).

## Artifact provenance

The Gramlot core wheel and matching source archive are the locally built candidate
used to verify the Bakery inspector theme correction on 2026-09-15. They are
provided here to make the extracted adapter installable while the coordinated
core release is pending. This does not publish or tag the core repository's
other ongoing development. `SHA256SUMS` covers every attached distribution.
The adapter source corresponds to this repository's preview tag.

This is an experimental preview. The demo server is for local development.

## Verification

The preview was checked with Python 3.12 in a fresh environment using the attached
wheels: Django system checks and nested runtime delivery pass without editable
checkouts. The installed Polls demo is also exercised in Chromium with external
requests blocked. Repository checks include Ruff, 33 behavior tests and strict
Sphinx documentation builds.
