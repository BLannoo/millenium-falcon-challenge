from pathlib import Path

import typer

from millenium_falcon_challenge.main import main

app = typer.Typer(name="give-me-the-odds")


def check_file_exists(path: Path) -> Path:
    if not path.exists():
        print(f"The path '{path}' does not exist.")
        raise typer.Exit(code=1)
    return path


@app.command()
def give_me_the_odds(
    millennium_falcon_path: Path = typer.Argument(..., callback=check_file_exists),
    empire_path: Path = typer.Argument(..., callback=check_file_exists),
):
    """
    Give the odds of reaching the destination without being captured by bounty hunters
    """
    odds = main(millennium_falcon_path, empire_path)
    print(odds * 100)
