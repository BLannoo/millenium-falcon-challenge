import pytest  # type: ignore
from assertpy import assert_that  # type: ignore

from millenium_falcon_challenge.algorithm import (
    find_all_trajectories,
)
from millenium_falcon_challenge.consts import HYPERSPACE_LABEL
from millenium_falcon_challenge.model.empire import BountyHunter
from millenium_falcon_challenge.model.routes import RoutesRepository
from millenium_falcon_challenge.trajectory import Trajectory


def test_query_routes(routes_repository: RoutesRepository):
    assert_that(routes_repository.get_routes_from("Tatooine")).extracting(
        "destination"
    ).contains_only(
        "Dagobah",
        "Hoth",
    )


def test_find_all_trajectories(routes_repository: RoutesRepository):
    assert_that(
        find_all_trajectories(
            routes_repository,
            departure="Dagobah",
            arrival="Endor",
            countdown=4,
            autonomy=6,
        )
    ).contains_only(
        Trajectory(("Dagobah", "Hoth", "Endor")),
        Trajectory(("Dagobah", "Dagobah", "Hoth", "Endor")),
        Trajectory(("Dagobah", "Dagobah", "Dagobah", "Hoth", "Endor")),
        Trajectory(("Dagobah", "Dagobah", "Hoth", "Hoth", "Endor")),
        Trajectory(("Dagobah", "Hoth", "Hoth", "Endor")),
        Trajectory(("Dagobah", "Hoth", "Hoth", "Hoth", "Endor")),
        Trajectory(
            ("Dagobah", HYPERSPACE_LABEL, HYPERSPACE_LABEL, HYPERSPACE_LABEL, "Endor")
        ),
    )


def test_find_all_trajectories_low_autonomy(routes_repository: RoutesRepository):
    assert_that(
        find_all_trajectories(
            routes_repository,
            departure="Dagobah",
            arrival="Endor",
            countdown=4,
            autonomy=1,
        )
    ).contains_only(
        Trajectory(("Dagobah", "Dagobah", "Hoth", "Hoth", "Endor")),
        Trajectory(("Dagobah", "Hoth", "Hoth", "Endor")),
        Trajectory(("Dagobah", "Hoth", "Hoth", "Hoth", "Endor")),
    )


@pytest.mark.parametrize(
    "travel_time, expected",
    [
        (1, Trajectory(("departure", "destination"))),
        (2, Trajectory(("departure", HYPERSPACE_LABEL, "destination"))),
        (
            3,
            Trajectory(
                ("departure", HYPERSPACE_LABEL, HYPERSPACE_LABEL, "destination")
            ),
        ),
    ],
)
def test_trajectory_add_route(travel_time: int, expected: Trajectory):
    assert_that(
        Trajectory(("departure",)).add_route(
            destination="destination", travel_time=travel_time
        )
    ).is_equal_to(expected)


@pytest.mark.parametrize(
    "burned_fuel, trajectory",
    [
        (0, Trajectory(("departure",))),
        (1, Trajectory(("departure", "destination"))),
        (2, Trajectory(("departure", "stop", "destination"))),
        (2, Trajectory(("departure", HYPERSPACE_LABEL, "destination"))),
        (
            3,
            Trajectory(
                ("departure", HYPERSPACE_LABEL, HYPERSPACE_LABEL, "destination")
            ),
        ),
        (1, Trajectory(("departure", "departure", "destination"))),
        (0, Trajectory(("departure", "destination", "destination"))),
    ],
)
def test_burned_fuel(burned_fuel: int, trajectory: Trajectory):
    assert_that(trajectory.burned_fuel).is_equal_to(burned_fuel)


@pytest.mark.parametrize(
    "odds, trajectory",
    [
        (0.0, Trajectory(("p0", "p4"))),
        (0.1, Trajectory(("p0", "p1", "p4"))),
        (0.19, Trajectory(("p0", "p1", "p2", "p4"))),
        (0.271, Trajectory(("p0", "p1", "p2", "p3", "p4"))),
    ],
)
def test_odds_of_capture(odds: float, trajectory: Trajectory):
    assert_that(
        trajectory.odds_of_capture(
            [
                BountyHunter(planet="p1", day=1),
                BountyHunter(planet="p2", day=2),
                BountyHunter(planet="p3", day=3),
            ]
        )
    ).is_equal_to(odds)
