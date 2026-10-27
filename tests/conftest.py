"""Pytest configuration and fixtures for isolated test execution."""

import os
from collections.abc import Generator
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """Change current working directory to a temporary directory for test isolation."""
    prev_dir = Path.cwd()
    os.chdir(tmp_path)
    try:
        yield tmp_path
    finally:
        os.chdir(prev_dir)
