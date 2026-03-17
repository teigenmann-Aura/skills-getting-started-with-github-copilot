from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities after each test for deterministic results."""
    snapshot = deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(snapshot))


@pytest.fixture
def client():
    """Provide a FastAPI test client."""
    return TestClient(app_module.app)
