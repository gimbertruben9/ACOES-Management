# ACOES-Management

## Configuring Frontend 

1. npm install @angular/cli
2. ng new frontend
3. cd frontend
4. ng serve (for running frontend in http://localhost:4200/)

For creating a new component (view) go to frontend/src/app and run:
- ng generate component component-name (generates the directory of the new component with 4 files)

## Configuring Backend

0. If you haven't got Python, install it on your computer (I use Python 3.7).
1. Create a new Flask Virtual Environment (preferably outside the project's directory):
    - python3 -m venv directory-name
2. Install dependencies by running the following command in the same directory of requirements.txt: pip install -r requirements.txt
3. To initialize database, inside backend's directory run:
    - flask --app app db init or flask db init
    - flask --app app db migrate -m "Initial migration" or flask db migrate -m "Initial migration"
    - flask --app app db upgrade or flask db upgrade
4. For running the app.py: python3 app.py

## Executing all in one server

1. cd frontend and npm run build
2. cd backend and python3 app.py

## Add data to DB

1. cd backend
2. Initialise database -> flask db init; flask db migrate -m "Initial migration"; flask db upgrade;
3. python3 add_data.py
