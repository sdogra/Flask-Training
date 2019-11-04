# Flask-Training

My Flask Training application is a simple application that allows you to view CAEN Software Listings, via web scraping of
dynamic table content from the CAEN Software website.

# Installation
First, simply clone this repo on your local machine. Then, ensure you have all the dependencies installed (i.e. Flask, 
selenium, bs4, etc.); these can be found in my __init__.py and routes.py files. This can be done via the package manager 
pip (i.e. pip install Flask, pip install selenium, etc.). This can also be determined by running the application and seeing
if it runs successfully or whether you are missing a certain dependency.

# Running the Application
Ensure that the environment variable FLASK_APP=training.py and then execute the command "flask run". This will
run the application. Open up your browser to http://localhost:5000 to view the homepage of the application.
