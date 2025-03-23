# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:4-python3.11-appservice
FROM mcr.microsoft.com/azure-functions/python:4-python3.11-slim

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY function_app.py /home/site/wwwroot
COPY host.json /home/site/wwwroot

# The followings lines are to enable ssh & remote debugging on the function app
# Remove these before deploying to production
RUN apt-get update \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd

COPY sshd_config /etc/ssh/
EXPOSE 8000 2222

#!/bin/sh
RUN service ssh start
