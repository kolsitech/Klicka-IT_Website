Job Portal - Read Me
This is a Django-based job portal project. The following are the instructions to download, install, and run the project.

This is a Django-based Job Portal application that allows employers to post job openings and job seekers to search and apply for jobs.

Installation
To install the Job Portal application, follow the steps below:

1. Clone the repository using the command: https://github.com/Sany07/Job-Portal.git. Alternatively, you can download the application using the URL: https://github.com/Sany07/Job-Portal.git.

2. Install dependencies using the command sudo apt install libpq-dev. This is an important software that is required for the application to run.

3.Create a virtual environment using the command virtualenv env.

4.Install required modules using the command pip install -r requirements.txt. In case there are failed installations listed in the requirements.txt file, you can install them manually using the command pip install <module-name>.

5.Set up the database from the settings.py file.

6.Migrate the database using the commands python manage.py makemigrations and python manage.py migrate.

7.Collect all static files in your apps using the command python manage.py collectstatic.

8.Finally, run the server using the command python manage.py runserver.
  
Screenshots
Screenshots of the application can be found in the screenshots folder in the repository.
  
Thank You
Thank you for using the Job Portal application.
