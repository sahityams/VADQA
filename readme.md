
Prerequisites:

    Python,
    PostgresSQL 

Step 1: Setup Virtual Environment:

    1.  Open your terminal or command prompt.
        Navigate to the directory where you project "sqlgpt" is located.

    2. Create the virtual environment:
        For Windows:
        Copy code
        python -m venv venv
        For macOS or Linux:
        Copy code
        python3 -m venv venv

Step 2: Activate the Virtual Environment

    On Windows:
    Copy code:
    venv\Scripts\activate
    On macOS or Linux:
    bash
    Copy code:
    source venv/bin/activate

Step 3: Install Django and other essential packages

    1. Install Django within the activated virtual environment:
    Copy code:
    pip install django

    2. Install other packages:
    Copy code:
    pip install -r requirements.txt

Step 5: Navigate to Project Directory

    Change into your project directory "sqlgpt":
    bash
    Copy code
    cd sqlgpt

Step 6: Create database in Postgres server using the imdb_database_sql

    1. Import the imdb_database.sql into a Postgres server
    2. Change line 15 in speechtotextApp/view.py to:
    f'postgresql://<username>:<password>@<server>:<port>/3969_HW1_Q3'

Step 7: Add OpenAI API key 

    Add OpenAI API key in line 32 of speechtotextApp/view.py

Step 8: Start the Development Server

    Copy code
    python manage.py runserver

Step 9: Access the UI

    If django is running in localhost:
    Navigate to http://127.0.0.1:8000/chat_view/

    else:
    Navigate to <django_root_url>/chat_view/


