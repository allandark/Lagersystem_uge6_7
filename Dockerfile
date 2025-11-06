FROM python:3.13

WORKDIR /lagersystem

COPY . /lagersystem/
RUN pip install -r requirements.txt
RUN apt update
RUN apt install nodejs npm -y
RUN cd lager-frontend && npm install && npm run build


ENTRYPOINT ["/bin/bash", "./scripts/entry_point.sh"]