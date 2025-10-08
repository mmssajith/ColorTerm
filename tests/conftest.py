"""Pytest configuration and shared fixtures."""

import sys
from pathlib import Path

import pytest

from tests.fixtures.sample_data import SAMPLE_COLORS, SAMPLE_TABLE_DATA, SAMPLE_TEXT

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def sample_text():
    """Provide sample text for testing."""
    return SAMPLE_TEXT


@pytest.fixture
def sample_colors():
    """Provide sample colors for testing."""
    return SAMPLE_COLORS


@pytest.fixture
def sample_table_data():
    """Provide sample table data for testing."""
    return SAMPLE_TABLE_DATA
