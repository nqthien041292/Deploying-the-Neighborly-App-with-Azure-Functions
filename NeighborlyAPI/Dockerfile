# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    host:logger:consoleLoggingMode=always \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    myAzureCosmosMongoDBConnectionString=mongodb://developerproject2cosmosdb:kgQoi5hsFd2pt2toysJZYkg1JEVPPqVwgv6m3r8JrQEIMEyiYbiuBkcqKaVG5rV74Wfv1MFxM3ToACDbtG2TbQ==@developerproject2cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@developerproject2cosmosdb@

COPY requirements.txt /

EXPOSE 8080

RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot
