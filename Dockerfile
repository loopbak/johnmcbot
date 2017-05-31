FROM ubuntu:14.04

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python-dev

RUN mkdir /opt/johnmcbot
WORKDIR /opt/johnmcbot

COPY ./* /opt/johnmcbot/

RUN pip install -r /opt/johnmcbot/requirements.txt

# expose port
EXPOSE 10010

# start app
CMD [ "python", "/opt/johnmcbot/bot_demo.py" ]
