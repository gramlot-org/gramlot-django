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

## Architecture and paired documentation

- Read the Gramlot product constitution and overview in the sibling `gramlot`
  repository before architecture changes; use `gramlot-poc` for experimental evidence.
- Keep server adaptation separate from database/ORM adaptation, including Django's two roles.
- Treat this project and its downloadable preview as a POC under review, not a stable contract.
- Follow docs/055-documentation.md: update paired docs/<path> and docs_llm/<path> together,
  preserving decisions, constraints, status and open questions. New architecture and
  product-contract documents require both views. Existing unpaired guides are tracked
  by that policy; do not claim complete mirror coverage.

- Number maintained guides in steps of five; mirror paths and stable GD document/block
  IDs between docs and docs_llm. Preserve IDs across moves; follow docs/055-documentation.md.
