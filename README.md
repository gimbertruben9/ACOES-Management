# ACOES-Management

## Configuring Frontend 

1. npm install @angular/cli
2. ng new frontend
3. cd frontend
4. ng serve (for running frontend in http://localhost:4200/)

For creating a new component go to frontend/src/app and run:
- ng generate component component-name (generates the directory of the new component with 4 files)

## Configuring Backend

0. If you haven't got Python, install it on your computer (I use Python 3.7).
1. Create a new Flask Virtual Environment (preferably outside the project directory)
2. Install dependencies by running the following command in the main directory of the project: pip install -r requirements.txt
3. To initialize database, inside backend's directory run:
    - flask --app app db init
    - flask --app app db migrate -m "Initial migration"
    - flask --app app db upgrade
4. For running the app.py: python3 app.py

