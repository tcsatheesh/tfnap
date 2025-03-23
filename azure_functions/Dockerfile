# To enable ssh & remote debugging on app service change the base image to the one below
FROM mcr.microsoft.com/azure-functions/python:4-python3.11-appservice
# FROM mcr.microsoft.com/azure-functions/python:4-python3.11-slim

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY requirements.txt /
RUN pip install -r /requirements.txt

# COPY function_app.py /home/site/wwwroot
# COPY host.json /home/site/wwwroot

COPY non_existent_function_app.py /home/site/wwwroot
