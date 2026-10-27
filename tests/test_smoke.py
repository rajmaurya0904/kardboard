"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import kardboard


def test_version_is_set() -> None:
    assert kardboard.__version__
