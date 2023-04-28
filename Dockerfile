FROM python:3.9.16
LABEL mantainer="alik.delrisco92@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app

EXPOSE 8080

ARG DEV=false

# USER PERMISSIONS
ARG USER_ID
ARG GROUP_ID

ENV USER_ID=$USER_ID
ENV GROUP_ID=$GROUP_ID
ENV USER_ID=${USER_ID:-1001}
ENV GROUP_ID=${GROUP_ID:-1001}

RUN addgroup --gid ${GROUP_ID} django-user
RUN adduser --disabled-password --no-create-home --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} django-user
RUN chown -R django-user:django-user /app


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ;\
    fi && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"


USER django-user
