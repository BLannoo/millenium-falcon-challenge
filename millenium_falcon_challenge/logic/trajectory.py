from dataclasses import dataclass
from typing import Tuple, List

from millenium_falcon_challenge.consts import HYPERSPACE_LABEL
from millenium_falcon_challenge.model.empire import BountyHunter


@dataclass(frozen=True)
class Trajectory:
    """
    A Trajectory is a list of locations where the millennium falcon can be found
    with the index of the list representing the day.

    The locations can either be a planet or <HYPERSPACE_LABEL>
    """

    locations: Tuple[str, ...]

    @property
    def burned_fuel(self):
        """
        Calculate the amount of fuel that has been burned since last re-fuelling
        to reach the end point of this Trajectory.
        """
        for i in range(len(self) - 1):
            if self[-i - 1] == self[-i - 2] != HYPERSPACE_LABEL:
                return i
        return len(self) - 1

    def __len__(self):
        return len(self.locations)

    def __getitem__(self, item: int):
        return self.locations[item]

    def add_route(self, destination: str, travel_time: int) -> "Trajectory":
        """
        Create a new Trajectory starting with this trajectory,
        ending with the destination
        and padded with the appropriate amount of <HYPERSPACE_LABEL>
        locations given the travel_time.
        """
        days_in_hyperspace = (HYPERSPACE_LABEL,) * (travel_time - 1)
        return Trajectory(
            (
                *self.locations,
                *days_in_hyperspace,
                destination,
            )
        )

    def last_location_can_be_reached(self, countdown: int, autonomy: int) -> bool:
        """
        The last location can be reached if:
        1) It has enough fuel to reach the final location given it's autonomy
        2) It does not exceed the countdown

        Remark:
        This does not validate that the earlier parts of the trajectory
        stay within the given autonomy.
        This is not needed with the current algorithm,
        but could be added later if needed.
        """
        return self.burned_fuel <= autonomy and len(self) <= countdown + 1

    def odds_of_capture(self, bounty_hunters: List[BountyHunter]) -> float:
        """
        Calculate the odds of capture when following this trajectory,
        considering the bounty_hunters planned locations.
        """
        encounter_count = sum(
            1
            for bounty_hunter in bounty_hunters
            if (
                bounty_hunter.day < len(self)
                and self[bounty_hunter.day] == bounty_hunter.planet
            )
        )
        return sum(9 ** k / (10 ** (k + 1)) for k in range(encounter_count))
