# Overview

<TODO: complete this with an overview of your project>
In this project we build a complete CI/CD and deploy a Machine Learning.

- First go to Azure and open Azure Cloud Shell.
- You need to create a Resource Group or use existing, create a Azure Storage and a Fileshare
- Create a Python Environment: python -m venv ~/.myenv then activate the environemt:
  source ~/.myenv/bin/activate
- Create and ssh keys with: ssh-keygen -t rsa, youll be asked to select the path where it will be created.
  Then you can copy the key eg: cat path/id_rsa.pub and copy the content
- Go to github project https://github.com/cyborg001/flask_udacity_final_project and clone it:
  git clone git@github.com:cyborg001/flask_udacity_final_project.git
- Run make install to install the packages needed to run your app
- You can run python app.py to test it in the cloudshell
- Then deploy your Azure web service with az webap up --<name>
- Go to the link of your app: https://<name>.scm.azurewebsites.net/ where name is the name of your web service
- you can run make_predict_azure_app.sh to see its predictions but firts you have to modify the file and change
  the following lines:
- Once your application is deployed we can go to Azure DevOps and create your organization
- Then create an new project
- Enter your project name and description, and you can make it public or private
- Create a new Pipeline and selet the github repository
- You'll be asked by azure to use the github repositories youll be asked by azure for permision
- Next configure your Pipeline as Python to Linux Web App on Azure, select suscription and web app.
- Validate and configure the web application
- 


## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
https://trello.com/b/sffFVaBO/udacity-devops-final-project

* A link to a spreadsheet that includes the original and final project plan>
https://docs.google.com/spreadsheets/d/1RHEuMgcq6L4AC6dCm6VmNM21FDfzcsnS2nFwKLQpPpA/edit#gid=1348135932

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

![diagram](https://user-images.githubusercontent.com/27867802/183260896-e27a980d-f11a-4225-93c0-f839ba99dde1.png)

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service
![app_running_in_azurecloud](https://user-images.githubusercontent.com/27867802/183238965-58d9bc7e-3149-4332-8ee4-c7c424fadc37.png)


* Project cloned into Azure Cloud Shell
![cloudshell project screenshot](https://user-images.githubusercontent.com/27867802/183228949-667930e4-5bfa-42f3-ad77-b8b7c164338f.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![test_after_make_all](https://user-images.githubusercontent.com/27867802/183237635-a26453df-0832-44a7-abcc-f8fe185ae181.png)

* Output of a test run
![output_test](https://user-images.githubusercontent.com/27867802/183237593-126715a1-1e27-4ce7-88bb-39aa39aaded5.png)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![deployed_flask_ml_app](https://user-images.githubusercontent.com/27867802/183237710-a09f1914-05fb-4573-b6e7-451ad0749f69.png)
https://calm-forest-cdeb821ed6704dc19dd91c6e1388512b.scm.azurewebsites.net/

* Running Azure App Service from Azure Pipelines automatic deployment
![deployerd_CD](https://user-images.githubusercontent.com/27867802/183238075-da785ac2-431a-4841-8a3b-5ff874a10e22.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```
![make_predict](https://user-images.githubusercontent.com/27867802/183237890-0b90c289-9418-48be-a345-c0cec086990b.png)

* Output of streamed log files from deployed application
![log_printscreen](https://user-images.githubusercontent.com/27867802/183238142-c2dc169a-6a84-4d56-b1c0-4e0b0c0d6aa8.png)

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


