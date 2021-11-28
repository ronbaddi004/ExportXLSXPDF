# Django rest application for XLSX and PDF export

### This application demos the XLSX and PDF export functionality from DRF by implementing BaseRenderers

Steps:
1. Create a virtual environment using `python -m venv env`
2. For windows, to activate env `.\env\Scripts\activate` and For Ubuntu, source `env\bin\activate`
3. The environment will be activated and your commandline will show `(env) ` as prefix. Run `pip install -r requirements.txt`
4. After installing the requirements, run `python manage.py migrate` to setup the database.
5. Create a superuser with `python manage.py createsuperuser {preferred_username}`. Optional: add more users
6. Run the application using `python manage.py runserver`
7. Navigate to the url http://localhost:8000/admin/ for the admin.
8. Navigate to the url http://localhost:8000/api/ for the api.

That's all folks!
