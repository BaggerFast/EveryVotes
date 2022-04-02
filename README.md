# Project EveryVotes

![Language](https://img.shields.io/badge/Language-Python3.9-yellow.svg?style=flat)
![Platform](https://img.shields.io/badge/Platform-WebSite-red.svg?style=flat)

### Clickable:
[![Documentation](https://img.shields.io/badge/Documentation-Latest-blue.svg?style=flat)](https://everyvotes.readthedocs.io/en/latest/)
[![Framework](https://img.shields.io/badge/Framework-Django-g.svg?style=flat)](https://docs.djangoproject.com/en/4.0/)

## The purpose
Give the user an open source web service where you can quickly create votes, then receive and analyze the opinions of other users

## Technology stack:
- **Languages:**
  - Python 3.9 (main)
  - Hmtl 
  - Css 
  - JavaScript
- **Libraries/Frameworks:**
  - Django 
- **Docs:**
  - Sphinx

## Quick setup:
1. Clone project
2. Open a project in PyCharm with default settings
3. Create a virtual venv(`settings` -> `project` -> `interpreter`)
4. Update pip:
   ```bash
   pip install --upgrade pip
   ```
5. Install the required libraries: 
   ```bash
   pip install -r requirements.txt
   ```
6. Migrate database:
    ```bash
   python3 manage.py migrate
   ```
7. Create run configuration in PyCharm(file `manage.py`, option `runserver`)


## Build documentation:
```
cd docs
make html
cd 
```

## Codestyle:
```
 DJANGO_SETTINGS_MODULE=options.settings pylint application options
```
