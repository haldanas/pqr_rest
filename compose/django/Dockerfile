FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
    # mysqlclient dependencies
    && apk add python3-dev \
    && apk add mariadb-dev\
    && apk --no-cache --update add build-base\
    #Pillow dependencias
    && apk add jpeg-dev \
    && apk add zlib-dev freetype-dev\ 
    && apk add lcms2-dev openjpeg-dev\ 
    && apk add tiff-dev tk-dev tcl-dev\
    # CFFI dependencies
    && apk add libffi-dev py-cffi \
    # Translations dependencies
    && apk add gettext \
    # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
    && apk add mysql-client

#Update pip package.
RUN pip install --upgrade pip

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/development.txt

COPY ./compose/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
