# Project Overview

This project is template project to use to scaffold or create the initial structure to your graphql
application using `django`, `graphene-django`, `djangorestframework` and `django-filter`.

**PROJECT STRUCTURE**

| File Name                 | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| `├── config/`             | _This folder contains the source files for the config_       |
| `├── requirements/`       | _This folder contains the source files for the requirements_ |
| `.gitignore`              | Git ignore config file                                       |
| `manage.py`               |                                                              |
| `requirements.develop`    | Requirement file for development mode                        |
| `requirements.production` | Requirement file for production mode                         |
| `requirements.staging`    | Requirement file for staging mode                            |
| `requirements.testing`    | Requirement file for testing mode                            |
| `run.py`                  | Entrypoint for production mode                               |
| `tox.ini`                 | Config file for liting, testing, coverage and ohter things   |

# Pre-requisites

- Python 3.9: https://www.python.org/downloads/
- Git for Windows (only for Windows): https://git-scm.com/downloads

# Creating a new project

If you are using Windows, use git bash to run these commands.

## Creating the project folder

```sh
mkdir awesome-graphql-api && cd awesome-graphql

```

## Creating the virtual environment

```sh
python -m venv venv
```

## Updating pip and installing pip-tools

```sh
python -m pip install --upgrade pip && pip install pip-tools
```

## Compiling the requirement file

### For development

```sh
pip-compile -r requirements/develop.in -o requirements.develop
```

### For production

```sh
pip-compile -r requirements/production.in -o requirements.production
```

### For staging

```sh
pip-compile -r requirements/staging.in -o requirements.staging
```

### For testing

```sh
pip-compile -r requirements/testing.in -o requirements.testing
```

## Installing the dependencies

### For development

```sh
pip install -r requirements.develop
```

### For production

```sh
pip install -r requirements.production
```

### For staging

```sh
pip install -r requirements.staging
```

### For testing

```sh
pip install -r requirements.testing
```

## Scaffolding the project

```sh
django-admin startproject --template https://github.com/danilobrinu/django-graphql-project-template/archive/master.zip <awesome-project> .
```

## Scaffolding the app

```sh
python manage.py startapp --template https://github.com/danilobrinu/django-graphql-app-template/archive/master.zip <awesome-app>
```

**Example:** `python manage.py --template https://github.com/danilobrinu/django-graphql-app-template/archive/master.zip api_v1`

## Scaffoling the app domain

```sh
mkdir <awesome-app>/domain/<awesome-app-domain> && python manage.py startapp -e py,graphql --template https://github.com/danilobrinu/django-graphql-app-domain-template/archive/master.zip <awesome-app-domain> <awesome-app>/domain/<awesome-app-domain>
```

**Example:** `mkdir api_v1/domain/post && python manage.py startapp -e py,graphql --template https://github.com/danilobrinu/django-graphql-app-domain-template/archive/master.zip post api_v1/domain/post`

## Running the app

### For development

```sh
python manage.py runserver
```

### For production

```
python run.py
```

## Verifying

Assuming that you have the link to the app for production mode is `app.io`:

### For development

Open the GraphQL Playground with http://localhost:8000/graphql/v1

### For production

Open the GraphQL Playground with http://app.io/graphql/v1

> **Note:** change app.iow with the real endpoint for production.
