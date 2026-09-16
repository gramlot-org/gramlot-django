# inspector: concise guide

[Expanded guide](../docs/inspector.md).

## 1. Preview status

Experimental API/design tool; behavior described is intended and may have bugs.

## 2. Open the Inspector

Bakery `/products/explore/` → magnifier Open inspector. Data/Source trees and Properties, movable/resizable panel.

## 3. Three different views

Data: runtime Bag. Source: runtime UI declaration tree. Separate Python CodeMirror viewer: read-only file. Inspector is not the IDE or a Python file editor.

## 4. Try a Data edit

Data/detail/title → edit value → leave property row. Bound bread title updates; later service data can replace it.

## 5. Try a Source edit

Source/h1_0 → edit value → leave property row. Heading updates. Typed scalar/attribute editors, add/delete attributes. Complex values read-only as a whole; expand to scalar children.

## 6. Lifetime and effects

Runtime edits do not write Python files. Reload restores server/declaration state. Changes may trigger bindings/controllers/RPCs; persistence uses services and permissions. source_inspection controls availability; table admin disables it by default.

## 7. Screenshot scope

Real Bakery/core 0.1.5 screenshots, 2026-09-16. Chromium Data/Source changes and reload restoration exercised; no guarantee of general correctness.
