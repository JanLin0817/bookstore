## Setting

add app: `bookstore/settings.py`
- INSTALLED_APPS: books
- database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'BookstoreDB',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': 3306,
        'HOST': '127.0.0.1',
    }
}
```

## Migrate Table

```bash
# specify app name
❯ python manage.py makemigrations books

❯ python manage.py migrate
```

## Admin

Create
- `python manage.py createsuperuser`

Register model to admin

