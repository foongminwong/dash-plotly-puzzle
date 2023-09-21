FROM debian:latest

RUN apt-get update -y && apt upgrade -y && ACCEPT_EULA=Y
RUN apt-get install -y wget \
  && apt-get install -y python3 \
  && apt-get install -y python3-pip

RUN mkdir /dash-plotly-puzzle
WORKDIR /dash-plotly-puzzle
COPY requirements.txt .
RUN pip3 install -r requirements.txt --break-system-packages

COPY ./ ./
CMD [ "gunicorn", "--reload", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "src.app:server"]