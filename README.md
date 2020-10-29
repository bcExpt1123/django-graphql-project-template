# Project Overview

This project is template project to use to scaffold or create the initial structure of your graphql
application using `django`, `graphene-django`, `djangorestframework` and `django-filter`.

**PROJECT STRUCTURE**

| File Name                 | Description                                                   |
| ------------------------- | ------------------------------------------------------------- |
| `├── config/`             | _This folder contains the source files for the config._       |
| `├── requirements/`       | _This folder contains the source files for the requirements._ |
| `.gitignore`              | Git ignore config file                                        |
| `manage.py`               |                                                               |
| `requirements.develop`    | Requirement file for development mode.                        |
| `requirements.production` | Requirement file for production mode.                         |
| `requirements.staging`    | Requirement file for staging mode.                            |
| `requirements.testing`    | Requirement file for testing mode.                            |
| `run.py`                  | Entrypoint for production mode.                               |
| `tox.ini`                 | Config file for linting, testing, coverage and ohter things.  |

# Pre-requisites

- Python 3.9: https://www.python.org/downloads/
- Git for Windows (only for Windows): https://git-scm.com/downloads

# Creating a new project

If you are using Windows, use git bash to run these commands.

**Creating the project folder**

```sh
mkdir awesome-graphql-api && cd awesome-graphql-api
```

**Creating the virtual environment**

```sh
python -m venv venv
```

**Activating the virtual environment**

```sh
source venv/bin/activate
```

_For Windows only_

```sh
. venv/Scripts/activate
```

**Deactivating the virtual environment**

```sh
deactivate
```

**Updating pip and installing pip-tools**

```sh
python -m pip install --upgrade pip && pip install pip-tools
```

## Compiling the requirement file

**For development**

```sh
pip-compile -r requirements/develop.in -o requirements.develop
```

**For production**

```sh
pip-compile -r requirements/production.in -o requirements.production
```

**For staging**

```sh
pip-compile -r requirements/staging.in -o requirements.staging
```

**For testing**

```sh
pip-compile -r requirements/testing.in -o requirements.testing
```

## Installing the dependencies

**For development**

```sh
pip install -r requirements.develop
```

**For production**

```sh
pip install -r requirements.production
```

**For staging**

```sh
pip install -r requirements.staging
```

**For testing**

```sh
pip install -r requirements.testing
```

## Scaffolding a project

```sh
django-admin startproject --template https://github.com/danilobrinu/django-graphql-project-template/archive/master.zip <awesome-project> .
```

> **Example:** `django-admin startproject --template https://github.com/danilobrinu/django-graphql-project-template/archive/master.zip my-graphql-api`

## Scaffolding an app

```sh
django-admin startapp --template https://github.com/danilobrinu/django-graphql-app-template/archive/master.zip <awesome-app>
```

**Example:** `python manage.py --template https://github.com/danilobrinu/django-graphql-app-template/archive/master.zip api_v1`

> **Note:** to read more about scaffoling an app, please go to: https://github.com/danilobrinu/django-graphql-app-template

## Scaffoling a domain app

To scaffold a domain app you need to go to inside of the domain folder part of an app. Only run this
this command inside of the your `<awesome-app>/domain` folder. For instance: `api_v1/domain`

```sh
django-admin startapp --template https://github.com/danilobrinu/django-graphql-app-domain-template/archive/master.zip <awesome-app-domain>
```

**Example:** `django-admin startapp --template https://github.com/danilobrinu/django-graphql-app-domain-template/archive/master.zip post`

> **Note:** to read more about scaffolding a domain app, please go to: https://github.com/danilobrinu/django-graphql-domain-app-template.

## Running an app

**For development**

```sh
python manage.py runserver
```

**For production**

```
python run.py
```

## Verifying

**Endpoint URL:** `http://<domain>/<path-to-your-graphql-endpoint>`

**For development:** The domain is `localhost:8000` and the path to your graphql is `graphql/v1`.

Open the GraphQL Playground with http://localhost:8000/graphql/v1

**For production**: The domain is `awesome.graphql.io` and the path to your graphql is `graphql/v1`.

Open the GraphQL Playground with http:///awesome.graphql.io/graphql/v1

> **Note:** change app.iow with the real endpoint for production.
