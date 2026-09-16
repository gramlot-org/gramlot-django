# Integration architecture

[Expanded counterpart and source links](../docs/architecture.md).

## 1. Authority and status

- Django POC under review. Gramlot constitution §§2/7/8 and overview §5 define boundaries.
- `gramlot-poc` supplies experimental evidence; accepted product lives in `gramlot`.

## 2. Independent adaptations

- Server adapter: pages/services to host; Django URLs, requests/responses, auth, CSRF, middleware.
- DB adapter: shared data services to backend/ORM; Django queries, projections, schema/model operations.
- Django supplies both roles. Django ORM is not a database engine.
- Independence does not imply every host/backend pair is implemented or tested.

## 3. Implemented POC

- Core: WebPage/builder, Source/Data, shared services, browser runtime.
- Host: `DjangoPageCollection`; database: `selection_result`, ORM/schema/model helpers.
- `DjangoPage` combines conveniences without merging responsibilities; Tables/Ide specialize pages.
- Applications own models/settings, record authorization and transactions.
- Public POC interfaces: `gramlot.hosting`, `gramlot.transport`; assets remain in core.

## 4. Open database contracts

- Constitution: `common`, `fake`, `genropy`, `sqlalchemy`; SQLite backend through SQLAlchemy.
- Owner direction 2026-09-16 identifies Django ORM adaptation here; no claim of an
  accepted complete Django DB contract or amended product taxonomy.
- Local POC database-handler guide inspected 2026-09-16; not yet on public develop.
  Experimental SQLite handler is evidence, not a new product adapter category.
- Django helpers do not establish final dataRecord/dataSelection/capability contracts.
- Keep minimum, common optional and implementation-specific capabilities distinct.
- Contract consolidation and reviewed ports remain open.

## 5. Authoring and evidence

- Python-first Source/Data, bindings, controllers, stores and services.
- No app-local DOM/fetch/parallel-state bypasses; fix reusable framework gaps.
- Customer/Polls/Bakery use this adapter; POC tests establish no stable product guarantee.
