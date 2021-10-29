# Django-CRM

### Setup
1. Create a folder and put all the files inside it.
2. Create a virtual environtment - `py -m venv env`
3. Activate VirtualENV - ubuntu : `source env/bin/activate` || windows : `. .\env\Scripts\activate`
4. Run requirements.txt - `pip install -r requirements.txt`
5. create env file and initialize variables
    * `MAIL` - email from partner mail service gmail
    * `PASSWORD` - password of email
    * `KEY` - Django secret key
    * `SERVER_NAME` - name of the server
6. Migrate - `py manage.py migrate`
7. Run the Application - `python manage.py runserver`