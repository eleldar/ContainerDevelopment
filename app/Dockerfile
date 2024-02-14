################################ temp stage ################################
ARG image=python:3.10.5
FROM ${image}-buster as builder
WORKDIR /server
RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./
ARG development
RUN if [ $development = 1 ] ; \
  then poetry install --no-root ; \
  else poetry install --without dev --no-root ; \
  fi
RUN rm -rf $POETRY_CACHE_DIR

################################ final stage ################################
FROM ${image}-slim-buster as runtime
WORKDIR /server

ENV VIRTUAL_ENV=/server/.venv \
    PATH="/server/.venv/bin:$PATH"
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY main.py main.py
COPY src src

### uncomment during development
COPY --from=builder /usr /usr
WORKDIR /app

### comment during development
# ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]