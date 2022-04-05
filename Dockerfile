FROM python:3.9.9
RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat
# Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Sets the container's working directory to /app
WORKDIR /app

RUN mkdir /app/report
# Copies all files from our local project into the container
# ADD . /app
COPY . .

RUN python -m pip install --upgrade pip
# runs the pip install command for all packages listed in the requirements.txt file
RUN pip install -r requirements.txt
