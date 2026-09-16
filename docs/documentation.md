# Documentation policy

[Concise counterpart](https://github.com/gramlot-org/gramlot-django/blob/develop/docs_llm/documentation.md).

## 1. Two views of the same information

Follow [Gramlot constitution section 9](https://github.com/gramlot-org/gramlot/blob/main/docs/00-constitution.md):
pair `docs/<path>` with `docs_llm/<path>`. The expanded document explains context
and examples for people; its concise counterpart helps LLMs and readers navigate
with fewer words. Both remain human-readable and preserve decisions, constraints,
status, limitations and open questions. A shorter version must not strengthen a claim.
Use the same numbered sections for stable references, reciprocal links and English.

## 2. Current coverage

The initial paired set is `overview.md`, `architecture.md`, `documentation.md` and `readthedocs.md`, `admin-spa.md` and `inspector.md`.
The existing integration, installation, demos and release guides in `docs/` remain
the detailed references; they do not yet all have concise counterparts. Historical
verification reports retain their date and scope. Add mirrors as these guides are
substantially revised; do not pretend existing coverage is complete.
README links to both entry points; [the concise index](https://github.com/gramlot-org/gramlot-django/blob/develop/docs_llm/index.md) routes
to paired documents and the remaining detailed guides. Root SPECIFICATION remains
the adapter ownership reference.

## 3. Maintenance and review

Update both members of a pair in the same change. New architectural or product
contract documents need both forms. Read the product constitution and relevant
`gramlot-poc` evidence before changing integration claims. Distinguish observed,
proposed, accepted and verified behavior; do not invent APIs from planned contracts.
Examples and passing POC tests do not imply acceptance in the clean product repo.
Use Mermaid when a diagram clarifies a boundary, not instead of defining the contract.
Run repository documentation checks and review links and paired status before publishing.
