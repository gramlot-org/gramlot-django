# Copyright 2026 Softwell S.r.l. - SPDX-License-Identifier: Apache-2.0
"""Django hosting and ORM helpers for Gramlot."""
from .application import DjangoPageCollection
from .page import DjangoPage, selection_result

__all__ = ['DjangoPage', 'DjangoPageCollection', 'selection_result']
