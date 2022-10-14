# Squad Manager API


## Description
Application would be available only for registered users, which are involved in team management (chief or manager).

MVP features:
- Member list with basic details - contact details and courses.
- Member details - detailed information of the member, owned dogs, detailed information about courses taken. 
- Dog list with basic information - name, owner, chip id, etc.
- Dog details - detailed information with exams.
- Exam list with basic information - basically who, what, when.
- CRUD for all above.

Next steps:
- Add authorization and authentication.
- Equipment list with useful information.
- Event and notification dashboard.
- List of actions group participated in - when, where, who, etc.
- Training planner.
- Alarm system used for search actions.

## Tech
- Python 3
- FastAPI
- PostgreSQL
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
- chore - everything else (writing documentation, formatting, cleaning useless code etc.)
- ci - changes to  CI configuration files and scripts

Examples:
- feat: add new model
- fix: update port number
- refactor: rewrite get entpoint
- tests: add unit tests
- chore: write function documentation
- feat(api)!: send an email to the customer when a product is shipped
- feat(lang): add Polish language


## Getting Started

...

### Prerequisites

...

### Installation


## License

....


