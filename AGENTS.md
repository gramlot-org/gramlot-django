# gramlot-django

Read README.md and SPECIFICATION.md before working. This is the pre-alpha home
of the Django adapter extracted from Gramlot.

- Keep code and maintained documentation in English.
- Use main for the baseline and develop for new development.
- Preserve copyright and Apache 2.0 notices.
- Keep secrets, virtualenvs, temp files and local worktrees out of Git.
- Use Python-first Gramlot declarations for applications; expose framework gaps
  instead of bypassing them with application-local DOM, events or fetch calls.
- Maintain the extracted adapter under gramlot_django and use standard Django project conventions.
- Keep server-independent page services and browser runtime in Gramlot; verify core compatibility.
- Development currently requires the local sibling gramlot-poc 0.1.5 checkout, not a published equivalent.
- Run scripts/check.py before commits/pushes; add behavior tests with implementation.
- Ruff and test failures block delivery; mypy is advisory.
- Do not add assistant co-author trailers to commit messages.
- Keep documentation aligned with implemented behavior; no speculative API claims.
- Do not introduce automatic package publication or deployment without authorization.
