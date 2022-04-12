# QUICK_START

1. Clone project
2. Open a project in PyCharm with default settings
3. Create a virtual venv(`settings` -> `project` -> `interpreter`)
4. Update pip:
   ```
   pip install --upgrade pip
   ```
5. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```
6. Migrate database and create super user:
    ```
   python manage.py migrate
   python manage.py create_admin
   ```
7. Create run configuration in PyCharm(file `manage.py`, option `runserver`)

## Build documentation:
```
cd docs
make html
cd ..
```

## Codestyle:
```
DJANGO_SETTINGS_MODULE=config.settings pylint *_app config --fail-under 7.5
```

## If django-debug-toolbar don't work:
[View problem solution](https://www.youtube.com/watch?v=1LrWRY_buxE)
