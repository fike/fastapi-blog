<p align="left">
<a href="https://github.com/fike/fastapi-blog/actions?query=workflow%3ATests" target="_blank">
    <img src="https://github.com/fike/fastapi-blog/workflows/Tests/badge.svg" alt="Test">
</a>

# A FastAPI sample

It's a FastAPI implementation as the backend for a blog system. This project's a funny goal to apply things that I'm learning. Things that you see here like telemetry using open source projects, CRUD using REST, and GraphQL (I hope that I have time to do that).

## Dependencies

* Poetry
* SQLAlmechy
* Alembic for migrations
* OpenTelemtry for instrumentation
* Docker
* Docker-Compose
* Jaeger
* Make

## How to use

Use make command to run inside a docker container, it'll expose the port 8000 and access using URL: `http://localhost:8000`. I'm not sure if a makefile runs in the Powershell, probably yes but I suggest using [WSL2](https://docs.microsoft.com/windows/wsl/install-win10).

**Up and run**:

```bash
make dev-up
```

!["Screenshot with REST backend endpoints"](/assets/fastapi_blog_endpoints.png)

This repo is instrumented by OpenTelemtry and export metric to Jaeger that starts together with the app by Docker-Compose, to access: `http://localhost:16686/`

### Tests

To run tests will up a PostgreSQL container and expose 5433 port to populate. The report will write in `htmlcov` dir.

```bash
make test-local
```

### Run and watch on the Jaeger things breaking

The FastAPI code here was OpenTelemetry instrumented and to export Traces to Jaeger. If you want to see a break simulation, follow the steps below.

#### Install dependencies

```bash
python -m venv .venv

pip install poetry

poetry install
```

#### Start FastAPI, PostgreSQL and Jaeger

```bash
make dev-up
```

[![asciicast](https://asciinema.org/a/395681.svg)](https://asciinema.org/a/395681)

#### Open another shell session and run `populate_posts.py` to create users and posts samples.

```bash
opentelemetry-instrument tests/populate_posts.py
```

[![asciicast](https://asciinema.org/a/395680.svg)](https://asciinema.org/a/395680)

#### Break things

Open a third shell session to stop Postgres, this will break the FastAPI app. You'll see error messages in the log and the script client on the console. Stop Postgres, wait some seconds or a minute, start Postgres again.

```bash
make dev-db-kill

sleep 30

make dev-db-start
```

[![asciicast](https://asciinema.org/a/395681.svg)](https://asciinema.org/a/395681)

#### Stop populate script

Stop the `populate_posts.py` scritpt (`ctrl+c`), go to Jaeger UI (http://localhost:16686/). If everything fine (or fail... 😁), you'll see on Jaeger like screenshots below.

* **FastAPI errors exported by OpenTelemetry to Jaeger**

!["jaeger traces errors"](/assets/jaeger_traces.png)

* **An error detail from the client request and server**.

!["an example of errors in the jaeger"](/assets/jaeger_trace_error.png)

## Known issues

* Some Opentelemetry warnings will show when tests ran.

## TODO

* ~~Pagination~~
* CORS
* Token authentication
* GraphQL
* Improve Token
* SAML/Oauth2
* Run tests in container
* ~~Autentication~~
* Implement UI (React)
* Helm Chart
* Improvement tests with tox
* ~~Implement a default path (**/**)~~
* Custom Limit and Offset
* ~~Add script to ingest samples~~
* ~~CI tests~~
