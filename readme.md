# Django Ecommerce Site

![Django](https://img.shields.io/badge/django-4.1.1-blue)
![Python](https://img.shields.io/badge/python->=3.9-green)
![Licence](https://img.shields.io/badge/License-MIT-blue)
### Installation

1. Clone this repository
2. Install the required Python packages
```shell
pip install -r requirements
```
4. Start the application
```shell
python manage.py runserver
```
5. Checkout the application at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Usage

To enter the admin panel, go to:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

The credentials are:
```
user:       admin
password:   training685
```
### Exercises

After creating models in `models.py`, run the following 
commands from the terminal:
```shell
python manage.py makemigrations
python manage.py migrate
```

### Tests

```shell
python manage.py test --exclude="to be implemented"
```
