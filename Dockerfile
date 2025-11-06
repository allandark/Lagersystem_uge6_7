FROM python:3.13

WORKDIR /lagersystem

COPY . /lagersystem/
RUN apt update
RUN apt install nodejs npm jq -y
RUN cd lager-frontend && npm install && npm run build
RUN pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/lagersystem/src"


ENTRYPOINT ["/bin/bash", "./scripts/entry_point.sh"]