# Squad Manager API


## Description
Application would be available only for registered users, which are involved in team management (chief or manager).

MVP features:
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


## Tech
- Python 3
- FastAPI
- PostgreSQL / SQLAlchemy / SQLModel
- Docker and docker-compose
- Poetry


## Project workflow

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
- tests: add unit tests
- chore: write function documentation
- feat(api)!: send email to the customer when a product is shipped
- feat(lang): add Polish language


## Getting Started

...

## License

....
