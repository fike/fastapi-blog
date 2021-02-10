# A FastAPI sample

This a FastAPI project for blog backend to learn purpose.

## Dependencies

* SQLAlmechy
* Alembic for migrations
* OpenTelemtry for instrumentation
* Docker
* Docker-Compose
* Jaeger

## How to use

To run and use needs to have make installed too. I'm sure if makefile run in Powershell, probably will run if you have WSL2 installed.

```bash
make dev-up
```

To run tests will up a postgresql container and expose 5432 port to populate, The report will write in htmlcov dir.

```bash
make test-local
```

## TODO

* Pagination
* Run tests in container
* Autentication
* Implement UI (React)
* Helm Chart
* Improvement tests with tox
* Implement a default path (**/api**)
* Hard LIMIT clause when get all posts
* Add script to ingest samples
* CI tests
