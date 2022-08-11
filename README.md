# Overview

In this project we build a complete CI/CD and deploy a Machine Learning.
You will be able to make predictions on house sales1.





## Project Plan

* A link to a Trello board for the project
https://trello.com/b/sffFVaBO/udacity-devops-final-project

* A link to a spreadsheet that includes the original and final project plan>
https://docs.google.com/spreadsheets/d/1RHEuMgcq6L4AC6dCm6VmNM21FDfzcsnS2nFwKLQpPpA/edit#gid=1348135932

## Instructions
- Here is a diagram of the project structure:
  ![diagram](https://user-images.githubusercontent.com/27867802/183272195-70493040-71d4-439d-977a-6c122aebfeae.png)
- First go to Azure and open Azure Cloud Shell.
- You need to create a Resource Group or use existing, create a Azure Storage and a Fileshare
- Create a Python Environment: python -m venv ~/.myenv then activate the environemt:
  source ~/.myenv/bin/activate
- Create and ssh keys with: ssh-keygen -t rsa, youll be asked to select the path where it will be created.
  Then you can copy the key eg: cat path/id_rsa.pub and copy the content
- Go to github project https://github.com/cyborg001/flask_udacity_final_project and clone it:
  git clone git@github.com:cyborg001/flask_udacity_final_project.git
  
  ![cloud_shell_clone_project](https://user-images.githubusercontent.com/27867802/184059501-2e9ca30c-01c3-49a7-8a0c-ddad0896b8ea.png)

- Run make install to install the packages needed to run your app

  ![make_all](https://user-images.githubusercontent.com/27867802/184061502-332fbaec-aba3-4f84-aaa0-b669d692fe7e.png)
  
  - You can run python app.py to test it in the cloudshell

  ![cloudshell project screenshot](https://user-images.githubusercontent.com/27867802/183272044-7c055d0e-1412-4a99-8ddb-bf1916fcc220.png)
  
  After make install in the make all you can see make test also executes
  
  ![passing_local_test_predictions](https://user-images.githubusercontent.com/27867802/184061824-86dcb3f8-29e3-4da7-9b1c-bc9b5ba4d886.png)



- Then deploy your Azure web service with az webap up --<name>
- Go to the link of your app: https://<name>.scm.azurewebsites.net/ where name is the name of your web service
  ![app_running_in_azurecloud](https://user-images.githubusercontent.com/27867802/183272062-a1d3b9c4-1345-4eb8-9779-17c28ef34965.png)

- Once your application is deployed we can go to Azure DevOps and create your organization
- Then create an new project
- Enter your project name and description, and you can make it public or private
- Create a new Pipeline and selet the github repository
- You'll be asked by azure to use the github repositories youll be asked by azure for permision
- Next configure your Pipeline as Python to Linux Web App on Azure, select suscription and web app.

  ![deployed_pipeline](https://user-images.githubusercontent.com/27867802/183272082-e8c9aa64-602d-408b-a4d4-a65cf7665d8c.png)

- Validate and configure the web application
- Save and run your pipeline.

  ![deployerd_CD](https://user-images.githubusercontent.com/27867802/183272090-51046418-8820-4e95-a841-971621452f58.png)

- you can run make_predict_azure_app.sh to see its predictions but firts you have to modify the file and change
  the following line:  -X POST https://(appname).azurewebsites.net:$PORT/predict youll change (appname) for the name
  of the web application.
- next run the command:
  ./make_predict_azure_app.sh
  and you will see the in the output the predicton:
        Port: 443
        {"prediction":[20.35373177134412]}

  ![make_predict](https://user-images.githubusercontent.com/27867802/183272094-e7509a84-8f3f-44cf-ad15-259f3cc93d2e.png)

- You can run the logs with
  az webapp log tail

  ![log_printscreen](https://user-images.githubusercontent.com/27867802/183272098-f79f33df-5c51-4e7b-b35e-368c5e39f940.png)



## Enhancements

A short description of how to improve the project in the future.

- You can use the Click tool to replace the script make_predict_azure_app.sh for a parametrized python code
  which accepts a dict as parameter.

## Demo 

Add link Screencast on YouTube:
https://youtu.be/sExdSs9Y4ZM


