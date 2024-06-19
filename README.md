# 🎥 Repofolio
A library for auto-generating a dynamic portfolio from your Github, equipped with repo filtering, prioritization, & demo video properties. 

## Features 
Once you've created your portfolio website using the Repofolio library, you'll enjoy the following features: 
- 🪄 Your portfolio website will auto-update when you update a repo's name, description, homepage, or [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) or when you add a new public repo
- ⏳ Viewers of your website will be able to easily filter repos to find what their interested in (e.g. show me all repos related to 'React')
- ⭐️ You can **highlight** and set the **priority** of repos so they always show up in a certain order on your page
- 🎥 You can optionally associate a **video** & **thumbnail** with each repo
- 🔧 You can optionally add **projects without repos** (e.g. you're not allowed to share the code or you had another career in a past life that wasn't software)
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-1.png" width="500">
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-2.png" width="500">
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-3.png" width="500">
<br></br>


## Setup 
### Installation
1) Install PostgreSQL (for macs install the PostgreSQL app [HERE](https://postgresapp.com/) )
2) Install Python 
3) Install Pipenv `pip install pipenv`  
4) Create a Virtual Environment `pipenv install --python "$PYENV_ROOT/versions/<<version_you_installed_above>>/bin/python"`
5) Install all the dependencies for the Python App `npm install`
6) Create .env file 
```
FLASK_ENV=development
SECRET_KEY=<insert-secret-key-here>
DATABASE_URL=postgresql://repofolio:<insert-database-password-here>@localhost/repofolio
```    
7) Create .flaskenv file `FLASK_APP=repofolio.py`    


### Run the App Locally
1) Create the PostgreSQL database:
cd into the 'repofolio' directory   
```psql```    
```DROP DATABASE repofolio;```    
```DROP USER repofolio;```    
```CREATE USER repofolio WITH PASSWORD '<insert-password-here>';```    
```CREATE DATABASE repofolio WITH OWNER repofolio;```    
you should see output showing that the user & database were created

2) Seed the database: 
```\q``` to exist out of psql
```python database.py``` to seed the database 
```psql```
```SELECT * FROM repos;``` to confirm the data was seeded successfully 
```\q``` to exit out of psql

3) Start the server: 
```pipenv run flask run```
Then click on the link that says something like "Running on http://"...

4) If prompted to log into Github, follow the prompts

## Customizations 
Go to the `customizations` directory and follow all of the instructions where it says **'TODO'**:
1. `added_props_for_existing_repos.py` - optionally add videos, thumbnails, priority rankings, and a highlighted boolean for each repo
2. `customizable_constants.py` - add your profile pic, resume, Github username & LinkedIn username
3. `filters.py` - choose which [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) you want your viewers to be able to filter by 
4. `projects_without_repos.py` - optionally add projects without repos 
5. In the `templates` folder, find `home.html` and add a summary about yourself