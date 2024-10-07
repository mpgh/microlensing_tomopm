FROM python:3.10
LABEL maintainer="markus.hundertmark@uni-heidelberg.de"

WORKDIR /microlensing_tomopm

COPY . /microlensing_tomopm
RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false --local
RUN poetry install --no-interaction

# Activate virtual env
ENV PATH="/microlensing_tomopm/env/bin:$PATH"

# disable buffering so that logs are rendered to stdout asap
ENV PYTHONUNBUFFERED=1

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
# the exposed port must match the deployment.yaml containerPort value
# one way to run:
#    docker build -t microlensing_tomopm:latest .
#    docker run -p 8080:80 microlensing_tomopm:latest
#    point your browser to http://localhost:8080
EXPOSE 80
ENTRYPOINT [ "/usr/local/bin/gunicorn", "microlensing_tomopm.wsgi", "-b", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-", "-k", "gevent", "--timeout", "300", "--workers", "2"]
