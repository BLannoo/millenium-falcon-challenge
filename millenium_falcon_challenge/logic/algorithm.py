from dataclasses import dataclass
from typing import Set

from millenium_falcon_challenge.model.empire import Empire
from millenium_falcon_challenge.model.routes import RoutesRepository
from millenium_falcon_challenge.logic.trajectory import Trajectory


@dataclass(frozen=True)
class NextStop:
    destination: str
    travel_time: int


def find_all_trajectories(
    routes_repository: RoutesRepository,
    departure: str,
    arrival: str,
    countdown: int,
    autonomy: int,
) -> Set[Trajectory]:
    """
    Find all trajectories from departure to arrival
    that are within the time limits of the countdown
    and do not burn more fuel than the given autonomy
    """
    partial_trajectories = {Trajectory((departure,))}
    full_trajectories = set()

    while len(partial_trajectories) > 0:
        partial_trajectory = partial_trajectories.pop()
        current_stop = partial_trajectory[-1]

        next_stops = _determine_next_stops(routes_repository, current_stop)

        for next_stop in next_stops:
            new_trajectory = partial_trajectory.add_route(
                next_stop.destination, next_stop.travel_time
            )
            if new_trajectory.last_location_can_be_reached(countdown, autonomy):
                if new_trajectory[-1] == arrival:
                    full_trajectories.add(new_trajectory)
                else:
                    partial_trajectories.add(new_trajectory)

    return full_trajectories


def _determine_next_stops(
    routes_repository: RoutesRepository, current_stop: str
) -> Set[NextStop]:
    """
    Finds all the NextStop's available from the current_stop
    including staying at the current_stop for refuelling.
    """
    next_stops = {
        NextStop(
            destination=str(next_route.destination),
            travel_time=int(next_route.travel_time),
        )
        for next_route in routes_repository.get_routes_from(origin=current_stop)
    }

    next_stops.add(
        NextStop(
            destination=current_stop,
            travel_time=1,
        )
    )

    return next_stops


def find_best_odds_of_success(trajectories: Set[Trajectory], empire: Empire) -> float:
    if len(trajectories) == 0:
        return 0.0
    return 1.0 - min(
        trajectory.odds_of_capture(empire.bounty_hunters) for trajectory in trajectories
    )
