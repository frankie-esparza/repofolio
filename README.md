# 🍿 Repofolio
A library that ✨ magically ✨ generates a dynamic portfolio from your Github repos

## Features 
- 🪄 Automatic updates when you add a new public repo
- 💥 Automatic updates when you change a repo's name, description, or homepage
- 🔎 Viewers of your repofolio can easily filter your repos by [topic](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- ⭐️ Draw attention to your favorite repos with **highlights**
- 🏆 Set the **priority** of repos so your favorites show up first
- 🎥 Link a **video** & **thumbnail** with each repo
- 🔧 Add **projects without repos** (e.g. non-disclosable code or non-software projects)
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-1.png" width="700">
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-2.png" width="700">
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-3.png" width="700">
<br></br>

## Setup 
### Installation
1) Install PostgreSQL
2) Install Python 
3) Install Pipenv `pip install pipenv`  
4) Create a Virtual Environment `pipenv install --python "$PYENV_ROOT/versions/<<version_of_python_you_installed>>/bin/python"`
5) Install all the dependencies `npm install`
6) Create `.env` file that contains the following:
```
FLASK_ENV=development
SECRET_KEY=<insert-secret-key-here>
DATABASE_URL=postgresql://repofolio:<insert-database-password-here>@localhost/repofolio
```    
7) Create `.flaskenv` file that contains the following:
```
`FLASK_APP=repofolio.py`    
```

### Run the App Locally
1) Create the PostgreSQL database:
```
cd repofolio
psql    
DROP DATABASE repofolio; 
DROP USER repofolio;  
CREATE USER repofolio WITH PASSWORD '<insert-password-here>';   
CREATE DATABASE repofolio WITH OWNER repofolio;
```  
2) You should see output showing that the user & database were created
3) Seed the database `python database.py`
4) Confirm data was seeded correctly `SELECT * FROM repos;`
5) Exit out of psql `\q` 
6) Start the server: `pipenv run flask run`
7) If prompted to login to Github or create a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) follow the prompts

### Customization  
Go to the `/customizations` directory and follow all of the instructions everywhere it says `TODO`
1. `add_priority_and_highlight.py`
    - 🎥 optionally add videos & thumbnails
    - ⭐️ optionally add highlighted repos & repo priority rankings
2. `settings.py`
    - 📸 add your profile pic, resume, Github username & LinkedIn username
    - 📁 add storage urls (e.g. add details for a Google Cloud Storage bucket)
    - ⏰ set how often you want your repofolio to refresh
3.  `filters.py` 
    - 🔎 choose which [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) you want your viewers to be able to filter by 
4.  `add_projects_without_repos.py` 
    - 🔧 optionally add projects without repos in the 
5.  `/templates/home.html` 
    - 📝 add a summary about yourself
