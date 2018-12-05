# Simple Web Application

This is a simple web application using [Python Flask](http://flask.pocoo.org/).

This is based on a original project [simple-webapp-color](https://github.com/mmumshad/simple-webapp-color) from [Mumshad Mannambeth](https://www.udemy.com/user/mumshad-mannambeth/).

This is used as final project from [Docker for the Absolute Beginner - Hands On - DevOps](https://www.udemy.com/learn-docker/)

Created as a example to how [dockerizing](https://hub.docker.com/r/andersonbispos/simple-webapp-colored/) a application.

Previous docker image was created with all steps bellow already done and is ready to running container.
  
  Below are the steps required to get this working on a base linux system.
  
  - Install all required dependencies
  - Install and Configure Web Server
  - Start Web Server
   
## 1. Install all required dependencies
  
  Python and its dependencies

    apt-get install -y python python-setuptools python-dev build-essential python-pip
    
## 2. Install and Configure Web Server

Install Python Flask dependency

    pip install flask

- Copy app.py file and template/ folder or download it from source repository

## 3. Start Web Server

Start web server

    FLASK_APP=app.py flask run --host=0.0.0.0
    
## 4. Test

Open a browser and go to URL

    http://<IP>:5000                       => Hello World!
    http://<IP>:5000/color/blue            => Hello World! (blue background)
    http://<IP>:5000/color/red             => Hello World! (red background)
