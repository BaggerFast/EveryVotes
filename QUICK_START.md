#QUICK_START

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
cd ..
```

## Codestyle:
```
 DJANGO_SETTINGS_MODULE=options.settings pylint application options
```

## If django-debug-toolbar don't work:
[View problem solution](https://www.youtube.com/watch?v=1LrWRY_buxE)
