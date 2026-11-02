import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import build


def row(t, p, s, summary="x"):
    return {"ticket": t, "priority": p, "status": s, "summary": summary}


class TestHandover(unittest.TestCase):
    def test_p1_first(self):
        note = build([row("T2", "P3", "open"), row("T1", "P1", "open")])
        self.assertLess(note.index("T1"), note.index("T2"))

    def test_closed_excluded(self):
        note = build([row("T1", "P1", "closed"), row("T2", "P2", "open")])
        self.assertNotIn("T1", note)
        self.assertIn("Open tickets: 1", note)

    def test_empty(self):
        self.assertIn("Open tickets: 0", build([]))
