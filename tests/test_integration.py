from pathlib import Path

import pytest  # type: ignore
from assertpy import assert_that  # type: ignore

from millenium_falcon_challenge.main import odds_of_reaching_destination
from tests.conftest import TEST_ROOT_FOLDER
from tests.model.answer import Answer


@pytest.mark.parametrize(
    "input_folder",
    [
        TEST_ROOT_FOLDER / "../examples/example1",
        TEST_ROOT_FOLDER / "../examples/example2",
        TEST_ROOT_FOLDER / "../examples/example3",
        TEST_ROOT_FOLDER / "../examples/example4",
    ],
)
def test_odds_of_reaching_destination(input_folder: Path):
    millennium_falcon_path = input_folder / "millennium-falcon.json"
    empire_path = input_folder / "empire.json"
    answer_path = input_folder / "answer.json"

    assert_that(
        odds_of_reaching_destination(millennium_falcon_path, empire_path)
    ).is_equal_to(Answer.parse_raw(answer_path.read_text()).odds)
