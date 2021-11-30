#FROM python:3.9-alpine
#RUN /usr/local/bin/python -m pip install --upgrade pip
#RUN adduser -D myuser
#RUN apk add --no-cache gcc musl-dev linux-headers
#USER myuser
#WORKDIR /home/myuser
#ENV PATH="/home/myuser/.local/bin:${PATH}"
#COPY --chown=myuser:myuser . .
#RUN pip install -r requirements.txt

FROM python:3.8-buster
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update
RUN adduser myuser
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
#RUN pip install --upgrade pandas
#RUN pip install --upgrade pip setuptools wheel