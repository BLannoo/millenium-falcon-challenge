from pathlib import Path

from millenium_falcon_challenge.algorithm import find_all_trajectories
from millenium_falcon_challenge.model.empire import Empire
from millenium_falcon_challenge.model.millennium_falcon import MillenniumFalcon
from millenium_falcon_challenge.model.routes import RoutesRepository


def odds_of_reaching_destination(
    millennium_falcon_path: Path, empire_path: Path
) -> float:
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

    if len(trajectories) == 0:
        return 0.0
    return 1.0 - min(
        trajectory.odds_of_capture(empire.bounty_hunters) for trajectory in trajectories
    )
