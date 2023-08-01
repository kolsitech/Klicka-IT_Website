Welcome to the Django-based Job Portal application, designed to simplify the job search process for both employers and job seekers. With this application, employers can effortlessly post job openings, while job seekers can conveniently search and apply for their desired positions.

To get started with the Job Portal application, follow the straightforward installation steps outlined below:

1.First, clone the repository by executing the following command in your terminal: git clone https://github.com/Sany07/Job-Portal.git. Alternatively, if you prefer not to use Git, you can download the application directly using this URL: https://github.com/Sany07/Job-Portal.git.

2.Before proceeding, make sure to install a crucial software dependency by executing sudo apt install libpq-dev. This software is essential for the application to function correctly.

3.Next, create a virtual environment to keep the application isolated from your system's global Python environment. Use the command virtualenv env to create the virtual environment.

4.Now, it's time to install the necessary Python modules required for the Job Portal application to run smoothly. Execute pip install -r requirements.txt in your terminal. If any module installations fail and are listed in the requirements.txt file, you can manually install them one by one using the command pip install <module-name>.

5.The next step is to set up the database configuration. Navigate to the settings.py file and configure the database settings according to your needs.

6.With the database settings in place, migrate the database by running python manage.py makemigrations followed by python manage.py migrate.

7.It's important to collect all static files related to your apps using the command python manage.py collectstatic. This ensures that the application's static assets are properly managed and served.

8.You're almost there! To launch the Job Portal application, run the development server with the command python manage.py runserver. The application will now be accessible through your web browser.

9.Feel free to explore the various features of the Job Portal application and create a seamless experience for both employers and job seekers. Should you encounter any issues, don't hesitate to refer to the screenshots folder in the repository for visual aids and guidance.

10.Thank you for choosing the Job Portal application. We hope it streamlines your job search and recruitment process, making it more efficient and user-friendly. Should you have any questions or feedback, please don't hesitate to reach out. Happy job hunting!
