# admin-spa: concise guide

[Expanded guide](../docs/admin-spa.md).

## 1. Preview status

Experimental API/design preview. Intended behavior may have bugs; not a full Django/Wagtail admin replacement.

## 2. Try the Bakery example

Use `/spa_admin/tables/`; active staff and model permissions required. Select breads/countries, double-click or Enter; New where allowed, Save persists, Cancel closes draft.

## 3. Declare the exposed models

Subclass DjangoTablesPage, explicitly declare table_fields. Exposure does not grant permissions. Search limit: 100 rows.

## 4. How forms are generated

Restricted ModelForm → Gramlot form/formlet and record Data bindings. FK/O2O: dbSelect; textarea: textBoxArea; other supported scalars: textBox. Related grids read-only.

## 5. Validation and saving

validate_record_field RPC validates current draft without saving. table_forms supports custom ModelForm clean methods and Django validation. Save validates again with permissions and transaction/row lock. Clean methods must be side-effect-free; drafts may be incomplete. Current error presentation can duplicate messages.

## 6. Boundaries and permissions

Relation queryset and target view permissions apply. Related fields must be exposed; parent saved and parent/target readable; 100-row limit. M2M preserved. No delete UI, full widget mapping or Wagtail workflow/tree editing. Table Inspector disabled by default.

## 7. Screenshot scope

Real Bakery/core 0.1.5 screenshots, 2026-09-16. Country open, required-field error, Cancel exercised without saving; narrow evidence, not general correctness.
