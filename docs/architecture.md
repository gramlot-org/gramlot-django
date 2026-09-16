# Integration architecture

`gramlot_django` composes Django with the server-independent Gramlot framework.

| Owner | Responsibilities |
| --- | --- |
| Gramlot | Python WebPage and builder, Source/Data transport, shared service and runtime utilities, JavaScript components |
| gramlot-django | Django views/URLs, request and permissions, CSRF, ORM projection and schema, Django page specializations |
| Django application | Models, settings, middleware, URL mounting, record authorization, transactions and Python application pages |

`DjangoPageCollection` discovers pages and adapts Gramlot's service lifecycle to
Django. `DjangoPage` extends `WebPage` with request context and ORM helpers;
`DjangoTablesPage` and `DjangoIdePage` specialize it further. Runtime assets are
served from the installed Gramlot package. Shared core services are exposed through `gramlot.hosting` and
`gramlot.transport`; compatibility must be checked when core changes.

Examples include a small customer project and the upstream-licensed Bakery
snapshot. Their pages import `gramlot_django`; neither defines another adapter.
