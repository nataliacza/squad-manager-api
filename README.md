# Squad Manager API

Since 2015 I'm member of <b>OSP Gdansk</b> 🚒 (Ochotnicza Straz Pozarna / Volunteer Fire Department). Our 
specialization is search for missing persons using trained and <b>certified dogs</b> 🐕‍🦺. Each similar formalized 
group struggles with the same issues - a lot of members, numerous deadlines, plenty of simple data that you need 
to store and remember about.

Why not create an application, which could manage everything in one place?

Main goal of this project is to create backend REST API for all-in-one tool, that would help to manage small organizations like OSP.

## Description
Application would be available only for limited users, which are involved in team management (chief or manager).

<b>Basic functionalities:</b>
- User can view a list of all members with their basic information.
- User can add new member.
- User can view member details (contact, dogs, courses)
- User can edit contact details, dogs assigned (or assign new dog), courses details.
- User can delete member.
- User can view a list of all dogs with details.
- User can add new dog.
- User can edit dog details.
- User can delete dog.
- User can view a list of all exams.
- User can add new member and dog exam.
- User can edit exam dates.
- User can delete exam.
- User can filter exams - by dog name, member name/surname and exam type.

All data storage in SQL database.

<b>Next steps:</b>
- Add authorization and authentication.
- Add pagination for all list views.
- Deploy (for frontend development).

<b>Possibilities to extend:</b>
- Add personal inventory for each member.
- Add group equipment list with details.
- Event and notification dashboard.
- List of actions group participated in - when, where, who.
- Personal training plan/diary.

Web application schema design in [Figma](https://www.figma.com/file/d2eQcOC1lFrzm9YcfCJkHZ/OSP---Web-design).

## Tech tools
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

<b>Branch naming convention:</b>
- <b>feature</b> - adding, refactoring or removing a feature
- <b>bugfix</b> - fixing a bug
- <b>hotfix</b> - changing code with a temporary solution and/or without following the usual process (high importance)

<details>
<summary markdown="span"><b>Examples</b></summary>
<i>

- feature/database-connection
- bugfix/docker-compose-ports
- hotfix/user-model

</i>
</details>
<br>

<b>Commit messages:</b>
- <b>build</b> - changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- <b>feat</b> - adding a new feature
- <b>fix</b> - fixing a bug
- <b>refactor</b> - changing code for performance or convenience purpose
- <b>test</b> - test-related code
- <b>chore</b> - everything else (formatting, cleaning useless code etc.)
- <b>docs</b> - creating or updating documents
- <b>ci</b> - changes to  CI configuration files and scripts

<details>
<summary markdown="span"><b>Examples</b></summary>
<i>

- feat: add new model
- fix: update port number
- refactor: rewrite get endpoint
- test: add 5 unit tests
- chore: write README documentation

</i>
</details>

### Git Hooks
In order to properly work with this repository, please copy prepared hooks located in <i>git_hooks</i> folder:
- commit-msg
- pre-commit
- prepare-commit-msg

<br>
You have few options to copy files from repository:

1. Use symlink

Open Command Line as admin and use command pattern: mklink (full path TO destination file) (full path FROM target 
file). See below:
```
mklink (path)\(repository-name)\.git\hooks\commit-msg (path)\(repository-name)\hooks\commit-msg.py
mklink (path)\(repository-name)\.git\hooks\pre-commit (path)\(repository-name)\hooks\pre-commit.py
mklink (path)\(repository-name)\.git\hooks\prepare-commit-msg (path)\(repository-name)\hooks\prepare-commit-msg.py
```
Example:
```
mklink D:\MyFolder\my-name\.git\hooks\commit-msg D:\MyFolder\my-name\git_hooks\commit-msg.py
```

2. Copy - paste

Just copy and paste all files from folder <i> .\git_hooks\ </i> to <i> .\my-repository\.git\hooks\ </i>.
