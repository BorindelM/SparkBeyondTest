FROM python:3.8-bookworm AS builder-image

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"


RUN  mkdir /opt/src
RUN  mkdir /opt/venv
COPY ./src/ /opt/src

# install requirements
COPY ./requirements.txt /opt/venv

RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r /opt/venv/requirements.txt


FROM python:3.8-bookworm AS runner-image
COPY --from=builder-image /opt /opt
RUN apt update 
RUN apt install -y coreutils


ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENTRYPOINT ["/opt/venv/bin/python3", "/opt/src/main.py"]
