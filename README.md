## FIRST TIME INSTALL ##
- pip install virtualenv
- virtualenv venv
- source ./venv/Scripts/activate
(make sure you have entered into the venv)
- pip install -r requirements.txt
- deactivate
​
## TO RUN ##
- windows(git bash) or linux > source ./venv/Scripts/activate
(make sure you use the appropriate python command for version 3)
- python app.py
​
## TO EXIT ##
(Ctrl+C to exit server)
- deactivate
(... to exit venv)
​
## POST VENV SYSTEM CHANGES ##
(enter your virtual environment)
- pip freeze > requirements.txt
​
## UPDATE VENV SYSTEM CHANGES ##
(enter your virtual environment)
- pip install -r requirements.txt