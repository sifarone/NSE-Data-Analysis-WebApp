
# For WRITE SERVER

FROM ubuntu
WORKDIR '/server'

RUN apt update
Run apt -y upgrade

RUN apt -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt -y install python3.7

RUN apt -y install python3 python3-pip

RUN python3.7 -m pip install python-dateutil
RUN python3.7 -m pip install redis
RUN python3.7 -m pip install pyjwt
RUN python3.7 -m pip install passlib

#RUN python3.7 -m pip install redis-dump-load
#RUN python3.7 -m pip install redisdl

RUN python3.7 -m pip install aiohttp
RUN python3.7 -m pip install aiohttp_cors
RUN python3.7 -m pip install motor
RUN python3.7 -m pip install pandas
RUN python3.7 -m pip install nsetools

RUN apt -y autoclean
RUN apt -y autoremove

COPY . .

#ENTRYPOINT ["python3.7"]
#CMD ["cors_writeServer.py"]

CMD ["python3.7", "-u", "cors_writeServer.py"]