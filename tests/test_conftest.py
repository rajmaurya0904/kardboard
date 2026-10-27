"""Tests for conftest fixtures."""

from pathlib import Path


def test_temp_dir_fixture(temp_dir: Path) -> None:
    """Verify temp_dir fixture changes working directory to a temp path."""
    current = Path.cwd().resolve()
    expected = temp_dir.resolve()
    assert current == expected
    # Also verify we can write files in it without affecting the repo root
    test_file = Path("test.txt")
    test_file.write_text("hello")
    assert test_file.exists()
