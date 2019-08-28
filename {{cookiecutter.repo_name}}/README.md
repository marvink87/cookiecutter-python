# {{cookiecutter.project_name}}

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [marvink87/cookiecutter-python](https://github.com/marvink87/cookiecutter-python) project template.
