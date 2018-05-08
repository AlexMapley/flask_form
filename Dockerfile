FROM ubuntu:16.04

# Update OS
RUN apt-get update
RUN apt-get -y upgrade

# Install Python
RUN apt-get install -y python-dev python-pip

# Create app directory
ADD . /netviewer

# Set the default directory for our environment
ENV HOME /netviewer
WORKDIR /netviewer

# Install app requirements
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["netviewer"]
