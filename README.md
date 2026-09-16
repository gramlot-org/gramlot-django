# gramlot-django

Django hosting, page authoring and ORM integration for Gramlot.

**Status: Pre-Alpha — 0.1.0 GitHub preview; not published on PyPI.**

This repository owns the Python Django adapter, its behavior tests and Django
examples. Import it through `gramlot_django`. Gramlot supplies the independent
Python builder/page services, typed transport and browser runtime.

## Implemented scope

- `DjangoPageCollection`: normal Django URLconf integration, page discovery,
  Source/Data RPC, packaged runtime delivery and host templates.
- `DjangoPage`: request context, page permissions and explicit ORM selections.
- Schema browsing, `DjangoTablesPage` and `DjangoIdePage`.
- Real middleware, CSRF, authentication, ORM and transaction behavior tests.
- Customer example and adapted Bakery/Wagtail demonstration.

Use Django's normal settings, middleware, database configuration and management
commands. Application UI and interactions are authored through Python Gramlot
pages. See [the integration guide](docs/django.md) and [examples](examples/README.md).

## Install the GitHub preview

Python 3.11+; no Node.js or local Gramlot checkout is required.
In a virtual environment, install the compatible core and this adapter together:

```sh
python -m pip install \
  'https://github.com/gramlot-org/gramlot-django/releases/download/v0.1.0-preview.1/gramlot-0.1.5-py3-none-any.whl#sha256=63466802618c8cbd3fed0a83e1072556085a31bd522477dbcfe1122417a26f4a' \
  'git+https://github.com/gramlot-org/gramlot-django.git@v0.1.0-preview.1'
gramlot-django demo --open
```

The GitHub prerelease also provides wheels, source distributions and SHA-256
checksums. The bundled Gramlot 0.1.5 candidate supplies the Python APIs and
compiled browser runtime. `pip install gramlot-django` from PyPI alone is not
available yet. See [GitHub preview details](docs/github-preview.md),
[the quickstart](docs/quickstart.md) and [release procedure](docs/release.md).

## Bakery showcase

The full Wagtail Bakery site is the main integration demonstration, with Gramlot
SPA pages inside its navigation and templates. See [Bakery setup](docs/bakery-demo.md)
for `gramlot-django demo bakery`. Its dependencies and project files remain separate.

## Polls demo

With the package installed:

```sh
gramlot-django demo --open
```

This starts a Django Polls site with an embedded Gramlot SPA and shared SQLite votes at
`http://127.0.0.1:8064/polls/`. See [demo options](docs/polls-demo.md).
This is a development preview, not a production release.

## Development

Python 3.11+; Django 5.2 or 6.0 subject to its Python requirements.
The integration requires the **local Gramlot 0.1.5 source**, not the older
0.1.0a1 package currently published on PyPI. Keep the `gramlot-poc` checkout beside
this repository; `tool.uv.sources` explicitly selects it for development.

```sh
uv sync --extra dev --extra docs
uv run python scripts/check.py
uv run mypy src/  # advisory
uv run python -m build
uv run python -m twine check dist/*
git config core.hooksPath hooks
```

See [getting started](docs/getting-started.md) for installation details and
[the ownership specification](SPECIFICATION.md) for the core/adapter boundary.
`develop` is the development branch; `main` is the baseline.
See [candidate verification](docs/candidate-verification.md) for the passing local
package and offline browser checks. Manual publication workflows are prepared
but have not been triggered.
No deployment is configured.

## License

Apache License 2.0. Copyright 2026 Softwell S.r.l. See LICENSE and NOTICE.
The Bakery snapshot retains its upstream license in `examples/bakerydemo/LICENSE`.
