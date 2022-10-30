# Squad Manager API

Since 2015 I'm member of OSP Gdansk 🚒 (Ochotnicza Straz Pozarna / Volunteer Fire Department). Our specialization is search for missing persons using trained and certified dogs 🐕‍🦺 . Each formalized group struggles with the same issues - a lot of members, numerous deadlines, plenty of data that you need to store somewhere, not to mention how to manage all those things together.

Why not to create some tool, which could manage everything in one place?

Main goal of this project is to create all-in-one tool, that would help to manage small organizations.

## Description
Application would be available only for registered users, which are involved in team management (chief or manager).

Basic features:
- Member list with basic details.
- Member details - detailed information of the member, owned dogs, about courses taken.
- Dog list with details.
- Exam list with details - who, what, when.
- CRUD for all above.

Next steps:
- Add search and filter for exam list.
- Add pagination for all list views.
- Add authorization and authentication.
- Deploy.

Future plan:
- Add personal inventory for each member.
- Add equipment list with details.
- Event and notification dashboard (main page).
- List of actions group participated in - when, where, who.
- Training planner.

Web application design created in [Figma](https://www.figma.com/file/d2eQcOC1lFrzm9YcfCJkHZ/OSP---Web-design).

## Tech
- Python 3
- FastAPI
- PostgreSQL / SQLAlchemy / SQLModel
- Docker and docker-compose
- Poetry

## Run the application

1. Clone repository:
```
git clone https://github.com/nataliacza/squad-manager-api
```

2. Create **.env** file in root folder, copy the content from **.env-example** and change example variables.

3. Using docker compose run the containers:
```
docker-compose up
```

5. Open application in web browser:
- Endpoints (OpenApi documentation): http://localhost:8000/docs#/
- PgAdmin for database view: http://localhost:5050/login

## Branch and commits

Branch naming convention:
- feature - adding, refactoring or removing a feature
- bugfix - fixing a bug
- hotfix - changing code with a temporary solution and/or without following the usual process (high importance)

Examples:
- feature/database-connection
- bugfix/status-codes
- hotfix/user-model

Commit messages:
- build - changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- feat - adding a new feature
- fix - fixing a bug
- refactor - changing code for performance or convenience purpose
- test - test-related code
- chore - everything else (formatting, cleaning useless code etc.)
- docs - creating or updating documents
- ci - changes to  CI configuration files and scripts

Examples:
- feat: add new model
- fix: update port number
- refactor: rewrite get endpoint
- test: add unit tests
- chore: write function documentation
