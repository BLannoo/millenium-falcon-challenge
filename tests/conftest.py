from pathlib import Path

import pytest  # type: ignore

from millenium_falcon_challenge.model.routes import RoutesRepository

TEST_ROOT_FOLDER = Path(__file__).parent


@pytest.fixture
def routes_repository():
    return RoutesRepository(
        db_path=TEST_ROOT_FOLDER / "../examples/example1/universe.db"
    )
