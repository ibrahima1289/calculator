# Simple calculator

## I. Introduction

For this project, we will build the web app with **Python Flask** first, and we will check if it works in the local host.<br/>
Then, we will create a repo in github and upload all the files in that repo.<br/>
Also, we will use **AWS Beanstalk** to integrate the project.<br/>
Finally, we will create a project in **Jenkins**, link it to the [calculator repo](https://github.com/ibrahima1289/calculator).

The calculator built in this repository is not complete yet. It is an ongoing project.<br/>
The resources used to build the simple calculator are from this [link](https://github.com/vr025/Calculator-Application-Using-Python-Flask).

There are three features:
* **BMI Calculator**: returns BMI (Body Mass Index).
* **Simple Calculator**: as said, this is a simple calculator that do basic calculation. You can only input two values per operation.
* **Unites Converter** (*under construction*)

## II. Setting up the environment in VS Code:

Installation Flask in Python using visio code (Windows 10)
Flask requires Python 3

**Setup virtual environment**

Create an environment
```
$ mkdir app_directory
$ cd app_directory
$ py -3 -m venv virtual
```
Activate the environment
```
$ .\virtual\Scripts\activate
```

Install Flask
```
$ pip install Flask
```

In the app_directory folder, create a folder application_app  and a Python file where the code will be displayed. 

Create a static and templates folder in application_app folder.
In the static folder, create a CSS file for the style if needed.
In the templates folder, create a HTML file(s). 

Once the setup is done, import your codes in the correct files.
Now you can check locally if your web app works.

## III. Set up AWS Beanstalk

1. Create your [AWS account user](https://docs.aws.amazon.com/rekognition/latest/dg/setting-up.html).
2. After you log in into your **AWS** root account, add a **IAM** user account with **AWS Beanstalk** privilages. Make sure to *attach existing policies* and save both access and secret key for future use. 
3. Log out from the root account, and log in into the **IAM** account.
4. Go to Amazon Elastic Beanstalk and create an application.
5. In create a web app, put the application name, add tag(s), and select python platform.</br>
   Select sampke application > create application.
6. It may take few minutes to set up th environment. Be patient!
7. See [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html) for more set up information.
8. You should see this after the set up is done.

   ![](/images/Deploy4-21.PNG)

## IV. Set up Jenkins

1. Create an EC2 on AWS and set up Jenkins. Here is a [tutorial](https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/) from AWS.
2. Log in to your Jenkins account.
3. Go to [Plugins Manager](https://www.jenkins.io/doc/book/managing/plugins/) > Type AWSEB under Avalaible plugins.
4. Select AWSEB Deployment and Cloubees Creadentials > Install.
5. After updating the plugins, create a new [project](https://aws.amazon.com/blogs/devops/setting-up-a-ci-cd-pipeline-by-integrating-jenkins-with-aws-codebuild-and-aws-codedeploy/) with github and AWS Beanstalk linked to the Jenkins project.
6. When the project is done, build it on Jenkins.
7. Go back to Elastic Beanstalk > Environments > Simplecalc-env, and launch the web application by following the [URL](http://simplecalc-env.eba-dmtxjiih.us-east-1.elasticbeanstalk.com/) highlighted in red. 

   ![](/images/Deploy4-23.PNG)
   
   Then it will take you to the web application home page.
   
   ![](/images/Deploy4-22.PNG)

## V. Chages made to the calculator

From the source codes [vr025](https://github.com/vr025/Calculator-Application-Using-Python-Flask), I was able to add two new features which are calculating the **square root** of a number and **square** a number.

This was easy to add because the syntax of the source code remains the same. I just had to copy/paste the line code and update the different variables.</br>
For this, it is possible to upgrade this **Simple Calculator** into a **Scientific** one with more features.

The errors I ran into was mostly indentation of the lines in the codes.


***Source:***
1. AWS
2. Jenkins
3. CSS, Js, and some Python codes for the simple calculator are from [vr025](https://github.com/vr025/Calculator-Application-Using-Python-Flask).
4. Flask set up from this [link](https://flask.palletsprojects.com/en/2.0.x/installation/).
2. For the BMI calculator, this [resource](https://www.youtube.com/watch?v=1k3cNPWVpcY) was used.
