# gramlot-django

Gramlot applications hosted by Django.

**Status: Pre-Alpha — repository boilerplate, no application implementation yet.**

## Scope

Django integration, with the Bakery application as the intended presentation example.

Use the existing gramlot.contrib.django adapter and standard Django project conventions. Verify which published Gramlot distribution contains the adapter before pinning dependencies.

The package currently contains only its namespace. Installing it does not start
a server or provide a working demo. Adapter extraction, runtime dependencies,
page migration and host commands are future implementation work described in
[SPECIFICATION.md](SPECIFICATION.md).

## Experimental examples

The examples use the experimental version of Gramlot maintained in
[gramlot-poc](https://github.com/gramlot-org/gramlot-poc). They will be progressively
adapted as Gramlot evolves and its APIs are reviewed and consolidated. Treat their
current code as experimental examples, not as a stable API reference.

## Development

```sh
git clone https://github.com/gramlot-org/gramlot-django.git
cd gramlot-django
uv sync --extra dev --extra docs
uv run python scripts/check.py
uv run python -m build
uv run python -m twine check dist/*
git config core.hooksPath hooks
```

Python 3.11+; Hatchling build backend; pytest, Ruff and advisory mypy; Sphinx
with Markdown support. `uv.lock` records
the development environment. A pip-based setup is also supported:
`python -m pip install -e '.[dev,docs]'`.

## Layout

- `src/gramlot_django/`: future implementation package.
- `tests/`: behavior tests added with the first implementation.
- `examples/`: future runnable, Python-authored Gramlot examples.
- `docs/`: Sphinx documentation.
- `hooks/`: pre-commit lint/advisory typing and pre-push checks.
- `.github/workflows/`: package and documentation checks.

`main` holds the initial baseline; use `develop` for new work. No automatic
package publication or deployment is configured. Read the Docs configuration
is provided, but its external service has not been connected.

## Checks

```sh
uv run python scripts/check.py
uv run mypy src/  # advisory
uv run python -m sphinx -W --keep-going -b html docs docs/_build/html
```

The check script explicitly reports that no application tests exist in the
initial scaffold. Once `tests/test_*.py` files are added, pytest is mandatory
and failures block the checks. CI also builds and installs the wheel in a
separate environment to verify packaging.

## License

Apache License 2.0. Copyright 2026 Softwell S.r.l. See LICENSE and NOTICE.
