# Main tuttle needs
FROM debian:jessie
MAINTAINER Lexman <tuttle@lexman.org>
RUN apt-get update && apt-get install -y python python-psycopg2 postgresql-client python-pip 
RUN pip install --upgrade pip
RUN pip install https://github.com/lexman/tuttle/archive/v0.3-rc1.zip
VOLUME ["/project"]
WORKDIR /project

# Specific for geo-countries-110 :
RUN apt-get update && apt-get install -y git &&  git config --global user.email "tuttle-bot@lexman.org" && git config --global user.name "Bot"
RUN apt-get update && apt-get install -y unzip gdal-bin 
