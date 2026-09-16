# gramlot-django: ownership and scope

## Maturity and consolidation — 2026-09-16

This integration is a POC under review, intended to become a reviewed prerelease
soon. The downloadable GitHub prerelease remains experimental. `gramlot-poc`
is the current executable dependency; `gramlot` will hold the first consolidated
product version and currently defines principles and reviewed ports.
Django supplies distinct server and ORM/database adaptations; neither role
implies the other. See docs/030-architecture.md and its docs_llm counterpart.

## Owner direction — 2026-09-15

This repository is the home of Gramlot's Django integration, including Python
adaptation to the server and database and Django-specific page definitions.
Transfer existing Django implementation, tests, guides and examples out of the
Gramlot framework repository. This supersedes the initial consumer-only scaffold
and the former `gramlot.contrib.django` ownership.

## Boundary

`gramlot_django` owns Django request/response handling, URL composition, host
middleware integration, CSRF and permissions, ORM selection/schema helpers,
DjangoPage, DjangoTablesPage and DjangoIdePage. Django examples, including Bakery,
belong here. Consumers use normal Django project conventions.

Gramlot retains its server-independent Python WebPage, builder, Source/Data
contracts, service invocation, shared host utilities and browser runtime. The
adapter uses the supported `gramlot.hosting` and `gramlot.transport` interfaces;
compatibility is verified with core and installed-package contract tests.
No duplicate JavaScript runtime or generic page implementation belongs here.

## Packaged demonstration

The base package includes a small Polls application and the `gramlot-django demo`
launcher. It uses normal Django migrations and runserver, keeps its SQLite data
outside the installed package, and serves standard Django Polls views/templates.
Gramlot SPA pages are embedded in that host site and authored in Python.
Bakery remains a separate demonstration with its own dependencies.

## Migration acceptance

- Preserve current adapter behavior and run its real Django integration tests.
- Update consumer imports to `gramlot_django`.
- Remove active Django adapter code and the Django extra from Gramlot after
  verifying the transferred implementation.
- Move maintained Django guides and examples; preserve licenses and historical
  decision records, with pointers to the new ownership where appropriate.
- Verify adapter packaging and core independence; retain unrelated local work.
- Keep application UI, state and requests in Python-authored Gramlot declarations.

## Dependency status

Development uses the local Gramlot 0.1.5 source. Consumer installs from current
GitHub main automatically obtain a checksummed 0.1.5 POC wheel from this repository's
preview assets; no matching core Git tag or sibling checkout is required.
PyPI currently provides only 0.1.0a1 (verified 2026-09-15). Development uses an
explicit sibling source override. A compatible core distribution must become
available before this integration can be installed solely from package indexes.
The owner authorized a GitHub preview on 2026-09-16. PyPI publication and
deployment remain outside that authorization.
