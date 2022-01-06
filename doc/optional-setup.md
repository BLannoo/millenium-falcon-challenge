# Optional setup

## pre-commit

pre-commit mostly setup to run: black and flake8

```shell
poetry run pre-commit install
```

## Pydantic codegen

data models where generated with:

```shell
poetry run datamodel-codegen --input ./examples/example1/millennium-falcon.json --input-file-type json --class-name MillenniumFalcon --output millenium_falcon_challenge/model/millennium_falcon.py --enable-faux-immutability
poetry run datamodel-codegen --input ./examples/example1/empire.json --input-file-type json --class-name Empire --output millenium_falcon_challenge/model/empire.py --enable-faux-immutability
poetry run datamodel-codegen --input ./examples/example1/answer.json --input-file-type json --class-name Answer --output tests/model/answer.py --enable-faux-immutability
```
