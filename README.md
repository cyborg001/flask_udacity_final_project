# Overview

In this project we build a complete CI/CD and deploy a Machine Learning.
You will be able to make predictions on house sales1.

[![Python application test with Github Actions](https://github.com/cyborg001/flask_udacity_final_project/actions/workflows/python-app.yml/badge.svg)](https://github.com/cyborg001/flask_udacity_final_project/actions/workflows/python-app.yml)



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
  
  After make install in the make all you can see make test also executes and shows the output of a test
  
  ![passing_local_test_predictions](https://user-images.githubusercontent.com/27867802/184061824-86dcb3f8-29e3-4da7-9b1c-bc9b5ba4d886.png)
  
- Next go to Actions in your repository to set the file YML:
  
    ![yaml](https://user-images.githubusercontent.com/27867802/184064825-ff85c2ef-df12-4725-aae2-b21e9b6c366b.png)
    
    and change the code for the scaffolder in starter_files:
    
    ![change_yaml](https://user-images.githubusercontent.com/27867802/184064912-84c9d14a-2836-486e-95f7-63570a6bf7f7.png)
    
- Commit the workflow and wait for it to run automatically.
    
    ![build_ci_job](https://user-images.githubusercontent.com/27867802/184066093-581439b4-4921-4d1c-8284-7a9675b20dad.png)
    
- Last step for the Continues Integration is to create a badge:
    
    ![creating_status_badge](https://user-images.githubusercontent.com/27867802/184066412-4becf439-05df-4c5c-b265-c44088ffaa59.png)
    
- The status badge:
  
    ![status_badge](https://user-images.githubusercontent.com/27867802/184066471-e126348e-559c-4558-a792-89e2cb655654.png)


- Then deploy your Azure web service with az webap up --<name>
  ![create_service](https://user-images.githubusercontent.com/27867802/184275247-a87736da-6e0b-4048-b558-7adb4b8455c9.png)
  
- You can see your service deploy on Azure Cloud:
  ![service_plan_in_azure](https://user-images.githubusercontent.com/27867802/184275942-90bf4fb6-fea1-4d26-bacb-58451da334d5.png)


- Go to the link of your app: https://(name).scm.azurewebsites.net/ where (name) is the name of your web service

  ![image](https://user-images.githubusercontent.com/27867802/184286431-13478e54-83c3-4423-a41a-5d89a59a3114.png)

- Lets make the load test and predict test.
  - First the load test:
    ![load_test](https://user-images.githubusercontent.com/27867802/184286552-3879792f-dc14-44b0-aa7b-06708e25bc44.png)
  - Second the predict test:
  
   ![test_predict](https://user-images.githubusercontent.com/27867802/184287955-89aa89fb-41db-4eaa-b050-062ac0bfbe8b.png)


- Once your application is deployed we can go to Azure DevOps and create your organization or use existing
- Then create an new project

  ![create_A_devops_organization](https://user-images.githubusercontent.com/27867802/184447617-dd4363ff-4c9a-4bb1-9dfc-a82fde1b4c5c.png)

  
- Enter your project name and description, and you can make it public or private
- Go to Pipelines
- Create a new Pipeline 
  
  ![create_AD_Pipelines](https://user-images.githubusercontent.com/27867802/184448037-d54e489c-ac59-4d38-a368-9ffa40edddd1.png)

- In 'where is your code' select Github

  ![select_github(yml)](https://user-images.githubusercontent.com/27867802/184448250-bc262822-d3ed-4679-a8a4-b94003e8addd.png)
  
- Select your Github repository

  ![select_your_github_repository](https://user-images.githubusercontent.com/27867802/184448487-eb0eaabd-b119-451b-8be9-f713bca6c8c7.png)

- You'll be asked by azure to use the github repositories youll be asked by azure for permision
- Next configure your Pipeline as Python to Linux Web App on Azure, select suscription and web app.
  
  ![configure_pipeline](https://user-images.githubusercontent.com/27867802/184448653-47a51cf0-f1c3-4644-a9e6-339e3e8a2771.png)
    
- Validate and configure the web application
- Save and run your pipeline.
  
  ![CD_deployed](https://user-images.githubusercontent.com/27867802/184294437-cc86c723-cdec-461b-8b6a-d9d3e229bcc0.png)

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

  ![log_image](https://user-images.githubusercontent.com/27867802/184295115-9ece1bd6-d4cd-4a71-9e46-d312acd58949.png)



## A short description of how to improve the project in the future.

- You can use the Click tool to replace the script make_predict_azure_app.sh for a parametrized python code
  which accepts a dict as parameter.

## Demo 

## Add link Screencast on YouTube:
https://youtu.be/hhHbObN8xMg


