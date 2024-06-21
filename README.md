# 🍿 Repofolio
A library that generates a dynamic portfolio that ✨ updates itself ✨ whenver you update your Github repos. 

## Features 
- 🪄 Automatic updates when you add a new public repo
- ✨ Automatic updates when you change a repo's name, description, or homepage
- 🔎 Viewers of your repofolio can easily filter your repos by [topic](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- ⭐️ Draw attention to your favorite repos with **highlights**
- 🏆 Set the **priority** of repos so your favorites show up first
- 🎥 Link a **video** & **thumbnail** with each repo
- 🔧 Add **projects without repos** (e.g. non-disclosable code or non-software projects)
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-1.png" width="700">

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-2.png" width="700">

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-3.png" width="700">

## Setup 
### Installation
1) Install PostgreSQL
2) Install Python 
3) Install Pipenv `pip install pipenv`  
4) Create a Virtual Environment `pipenv install --python "$PYENV_ROOT/versions/<<version_of_python_you_installed>>/bin/python"`
5) Install all the dependencies `npm install`
6) Create `.env` file following the format of the `.env.example` file
7) Create `.flaskenv` file that contains the following: `FLASK_APP=repofolio.py`

### Run the App Locally
1) Create the PostgreSQL database:
```sql
cd repofolio
psql    
DROP DATABASE repofolio; 
DROP USER repofolio;  
CREATE USER repofolio WITH PASSWORD '<insert-password-here>';   
CREATE DATABASE repofolio WITH OWNER repofolio;
```  
2) You should see output showing that the user & database were created
3) Seed the database `python database.py` (Note: also run this command if you make any changes to the database structure i.e. you modify the `models.py` file)
4) Confirm data was seeded correctly `SELECT * FROM repos;`
5) Exit out of psql `\q` 
6) Start the server: `pipenv run flask run`
7) If prompted to login to Github or create a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) follow the prompts
<br></br>

## Customize your Repofolio  
1) ✅ Go to the `/customizations` directory and follow all of the instructions everywhere it says `TODO`
2) 🪄 Sit back and relax as your Repofolio automatically updates itself whenever you make updates in Github.
<br></br>

## Contact
💭 Have questions or feedback? I'd love to hear them! Send me (Frankie, she/her) a message at fwesparza@gmail.com 
