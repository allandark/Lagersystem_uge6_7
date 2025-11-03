FROM python:3.13

# Install dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN apt update
RUN apt install nodejs npm -y

WORKDIR /lagersystem

ENTRYPOINT ["/bin/bash", "./entry_point.sh"]