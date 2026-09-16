# gramlot-django: POC overview

[Expanded counterpart](../docs/overview.md).

## 1. Status and repositories

- POC under review; reviewed prerelease intended soon, no fixed date or stable API.
- GitHub prerelease is an experimental download, not product acceptance; no PyPI publication.
- [gramlot-poc](https://github.com/gramlot-org/gramlot-poc): executable experimental core.
- [gramlot](https://github.com/gramlot-org/gramlot): future first consolidated product;
  currently principles and port protocol, not an installable runtime.

## 2. Responsibilities

- Python-first apps; Gramlot owns Source, Data, bindings, services and browser runtime.
- Django integration owns distinct host and ORM adaptations; see [architecture](architecture.md).

## 3. Usage

- [Pinned GitHub installation](../docs/github-preview.md); development uses sibling `gramlot-poc`.
- Bundled Polls: `gramlot-django demo --open`. Bakery needs its separate project/Wagtail dependencies.
- Examples are exploratory, not final API designs.

## 4. Acceptance and documentation

- Product constitution and port protocol govern acceptance; POC tests are evidence only.
- Paired `docs`/`docs_llm` preserve status, constraints and open questions; update together.
- Shared DB contracts and migration to accepted core ports remain to be consolidated.
- [Documentation coverage and policy](documentation.md).
