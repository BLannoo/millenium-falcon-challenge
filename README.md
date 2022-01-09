# Developer Technical Test @ Dataiku

The assignment description can be found: [here](./doc/assignement.md)

The core project setup can be found bellow.
Setup not specific to the project (poetry, brew, pipx) can be found: [here](./doc/non-project-setup.md)
Some optional tooling can be found: [here](./doc/optional-setup.md)

## Setup to run tests

Install the project with:

```shell
poetry install
```

Run tests with:

```shell
poetry run pytest
```

## Setup to run CLI

Create a wheel with:

```shell
poetry build
```

Install the CLI as an executable using pipx:

```shell
pipx install dist/millenium_falcon_challenge-0.1.0-py3-none-any.whl
```

Run the CLI with:

```shell
give-me-the-odds examples/example1/millennium-falcon.json examples/example1/empire.json
```

## Setup to run backend and frontend

To run the full stack application you will need to have docker running,
in which case you can run:

```shell
docker-compose up --build
```

The application is served [here](http://localhost:8080/)
