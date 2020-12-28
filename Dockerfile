
# First have to import Python version

FROM python:3.9.0
ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no cache --virtual . tmp gcc libc-dev linux-headers

RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /jobs
COPY ./jobs /jobs
WORKDIR /jobs
COPY ./scripts /scripts

RUN chmod +x /scripts/*
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user/vol
RUN chown -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]