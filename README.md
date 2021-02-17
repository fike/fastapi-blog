<p align="left">
<a href="https://github.com/fike/fastapi-blog/actions?query=workflow%3ATests" target="_blank">
    <img src="https://github.com/fike/fastapi-blog/workflows/Tests/badge.svg" alt="Test">
</a>


# A FastAPI sample

This a FastAPI project for blog backend to learn purpose.

## Dependencies

* SQLAlmechy
* Alembic for migrations
* OpenTelemtry for instrumentation
* Docker
* Docker-Compose
* Jaeger
* Make

## How to use

Use make command to run inside a docker container, it'll expose the port 8000 and access using URL: `http://localhost:8000`. I'm not sure if a makefile run in the Powershell, probably yes but I suggest to use [WSL2](https://docs.microsoft.com/windows/wsl/install-win10).

**Up and run**:

```bash
make dev-up
```

This repo is instrumented by OpenTelemtry and export metric to Jaeger that start together the app by Docker-Compose, to access: `http://localhost:16686/`

### Tests

To run tests will up a postgresql container and expose 5432 port to populate. The report will write in htmlcov dir.

```bash
make test-local
```

## Known issues

* Some Opentelemetry warnings will show when tests ran.

## TODO

* ~~Pagination~~
* Run tests in container
* Autentication
* Implement UI (React)
* Helm Chart
* Improvement tests with tox
* ~~Implement a default path (**/api**)~~
* Custom Limit and Offset
* Add script to ingest samples
* ~~CI tests~~
