from pathlib import Path

from millenium_falcon_challenge.logic.algorithm import (
    find_all_trajectories,
    find_best_odds_of_success,
)
from millenium_falcon_challenge.model.empire import Empire
from millenium_falcon_challenge.model.millennium_falcon import MillenniumFalcon
from millenium_falcon_challenge.model.routes import RoutesRepository


def main(millennium_falcon_path: Path, empire_path: Path) -> float:
    millennium_falcon = MillenniumFalcon.parse_raw(millennium_falcon_path.read_text())
    empire = Empire.parse_raw(empire_path.read_text())

    routes_repository = RoutesRepository(
        db_path=millennium_falcon_path.parent / millennium_falcon.routes_db
    )

    trajectories = find_all_trajectories(
        routes_repository=routes_repository,
        departure=millennium_falcon.departure,
        arrival=millennium_falcon.arrival,
        countdown=empire.countdown,
        autonomy=millennium_falcon.autonomy,
    )

    return find_best_odds_of_success(trajectories, empire)
