from rules_engine import rules_engine
import pytest

def test_does_rules_engine_exist():
    re = rules_engine()
    assert isinstance(re, rules_engine)