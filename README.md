# VADQA Project Setup Guide

This README provides detailed instructions on how to set up the VADQA Django project on your local environment, including dependencies, virtual environment setup, and starting the development server.

## Prerequisites

Before you begin, ensure you have the following installed:
- **Python**
- **PostgreSQL**

## Step 1: Setup Virtual Environment

1. **Open your terminal or command prompt** and navigate to the directory where your project "VADQA" is located.

2. **Create the virtual environment:**
   - For Windows:
     ```
     python -m venv venv
     ```
   - For macOS or Linux:
     ```
     python3 -m venv venv
     ```

## Step 2: Activate the Virtual Environment

- On Windows:
`venv\Scripts\activate`

- On macOS or Linux:
`source venv/bin/activate`


## Step 3: Install Django and Other Essential Packages

1. **Install Django** within the activated virtual environment:
`pip install django`


2. **Install other required packages**:
`pip install -r requirements.txt`


## Step 5: Navigate to Project Directory

- Change to your project directory "VADQA":
`cd VADQA`


## Step 6: Create Database in PostgreSQL Server

1. **Import the `imdb_database.sql` into a PostgreSQL server.**
2. **Modify the database connection string** on line 15 in `speechtotextApp/view.py` to match your database credentials:
`postgresql://<username>:<password>@<server>:<port>/3969_HW1_Q3`


## Step 7: Add OpenAI API Key

- Insert your OpenAI API key on line 32 of `speechtotextApp/view.py`.

## Step 8: Start the Development Server

- Run the following command to start the Django development server:
`python manage.py runserver`


## Step 9: Access the UI

- If Django is running on localhost, navigate to:
`http://127.0.0.1:8000/chat_view/`

- Otherwise, navigate to:
`<django_root_url>/chat_view/`
