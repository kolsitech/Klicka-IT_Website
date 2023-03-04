# Job Portal
Django Job Portal.       
,,

Installation
To download the project, you can either:

Use the terminal and type the following command: https://github.com/Sany07/Job-Portal.git
Download it manually from this URL: https://github.com/Sany07/Job-Portal.git
After downloading, install the dependencies by running the following command in the terminal:

#bash

sudo apt install libpq-dev
virtualenv env ( # Activate Virtual Enviroment)
pip install django
pip install -r requirements.txt

Note: If any requirements fail to install from the requirements.txt file, you can install them manually, such as pip install django-ckeditor.

#Database
You can set up the database from settings.py file.

#Migrate the Database
To migrate the database, open the terminal in the project directory and run the following commands:

#Copy code
python manage.py makemigrations
python manage.py migrate
Collect Static Files
To collect all the static files in your apps, run the following command in the terminal:

#Copy code
python manage.py collectstatic
Run the Server
To run the server, use the following command:

#Copy code
python manage.py runserver
Screenshots
The following are the screenshots of the project:

Home Page:
Home Page Screenshot

Jobs Page:
Jobs Page Screenshot

Job Detail Page:
Job Detail Page Screenshot

Create Job Page:
Create Job Page Screenshot

Dashboard Page:
Dashboard Page Screenshot

Employer Job Applicants Page:
Employer Job Applicants Page Screenshot

Thank you for using this job portal project.,,