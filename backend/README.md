# Lunch Service

Lunch service app

## Run Locally

1. Go to the directory

```bash
  cd lunch_place/backend
```

2. Create virtual enviroment

```bash
  python -m venv venv
```

3. Install dependencies

```bash
  pip install -r requirements.txt
```

4. Go to the project directory

```bash
  cd lunch_place/backend/lunch_place
```

```bash
  python manage.py makemigrations
```

```bash
  python manage.py migrate
```

```bash
  python manage.py runserver
```

## Running Tests

- Discover and run all tests from the current directory

```bash
  python -m pytest

  flake8 --config=setup.cfg --exclude venv --max-line-length 99
```

- Explicitly print the result of each test as it is run

```bash
 python -m pytest -v
```

You can use <py_client> for testing endpoints.

5. Run

```bash
docker compose up
```
