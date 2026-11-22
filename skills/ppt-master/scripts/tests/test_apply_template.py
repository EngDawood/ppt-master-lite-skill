#!/usr/bin/env python3
"""Tests for apply_template.py against the bundled template library."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from apply_template import (  # noqa: E402
    ApplyTemplateError,
    _receipt,
    apply_templates,
)

TEMPLATES = SCRIPTS_DIR.parent / "templates"
STYLE_ROOT = TEMPLATES / "styles" / "incident-postmortem"
BRAND_ROOT = TEMPLATES / "brands" / "中国电信"
LAYOUT_ROOT = TEMPLATES / "layouts" / "presentation_core"
DECK_ROOT = TEMPLATES / "decks" / "中国电信"


class ApplyTemplateTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.project = self.tmp / "proj"
        (self.project / "templates").mkdir(parents=True)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _apply(self, *roots: Path | str, **kwargs):
        kwargs.setdefault("validate", False)
        return apply_templates(self.project, [str(root) for root in roots], **kwargs)

    def test_library_style_installs_one_qualified_spec_with_provenance(self) -> None:
        plan = self._apply(STYLE_ROOT, validate=True)
        installed = self.project / "templates" / "design_spec.style.incident-postmortem.md"
        self.assertTrue(installed.is_file())
        text = installed.read_text(encoding="utf-8")
        h1 = text.index("# Incident Postmortem")
        self.assertIn(
            "\n\n> **Installed from**: `skills/ppt-master/templates/styles/"
            "incident-postmortem/` (library)\n",
            text[h1:],
        )
        self.assertEqual(text.count("**Installed from**"), 1)
        self.assertEqual(sorted(p.name for p in self.project.iterdir()), ["template_install.json", "templates"])
        receipt = _receipt(plan)
        self.assertIn("sources=library", receipt)
        self.assertIn("kinds=style", receipt)
        self.assertIn("direction:style", receipt)
        self.assertIn("structure:free-design", receipt)
        self.assertIn("active_roster=none", receipt)
        self.assertIn("install=copied", receipt)

    def test_rerun_is_idempotent(self) -> None:
        self._apply(STYLE_ROOT)
        plan = self._apply(STYLE_ROOT)
        self.assertEqual([m.status for m in plan.mappings], ["identical"])

    def test_duplicate_kind_is_rejected_before_writing(self) -> None:
        with self.assertRaises(ApplyTemplateError) as ctx:
            self._apply(STYLE_ROOT, TEMPLATES / "styles" / "consulting-decision")
        self.assertIn("one root per kind", str(ctx.exception))
        self.assertEqual(list((self.project / "templates").iterdir()), [])

    def test_explicit_root_keeps_its_path_as_provenance(self) -> None:
        explicit = self.tmp / "my_style"
        shutil.copytree(STYLE_ROOT, explicit)
        plan = self._apply(explicit)
        spec = self.project / "templates" / "design_spec.style.incident-postmortem.md"
        self.assertIn(
            f"> **Installed from**: `{explicit.resolve()}/` (explicit)",
            spec.read_text(encoding="utf-8"),
        )
        self.assertIn("sources=explicit", _receipt(plan))

    def test_inner_templates_directory_is_refused(self) -> None:
        with self.assertRaises(ApplyTemplateError) as ctx:
            self._apply(STYLE_ROOT / "templates")
        self.assertIn("workspace root", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
