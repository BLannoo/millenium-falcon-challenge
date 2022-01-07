from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from millenium_falcon_challenge.consts import PROJECT_ROOT_FOLDER
from millenium_falcon_challenge.main import main_with_empire_parsed
from millenium_falcon_challenge.model.empire import Empire
from millenium_falcon_challenge.model.odds_of_success import OddsOfSuccess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/odds-of-success/")
def odds_of_success(empire_communication: Empire) -> OddsOfSuccess:
    return OddsOfSuccess(
        odds_of_success=main_with_empire_parsed(
            empire=empire_communication,
            millennium_falcon_path=PROJECT_ROOT_FOLDER
            / "examples/example1/millennium-falcon.json",
        )
    )
