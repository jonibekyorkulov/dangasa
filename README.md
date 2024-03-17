# Dangasa

Dangasa, Django REST frameworkida CRUD (Create, Read, Update, Delete) operatsiyalarni tezroq yaratishga yordam beradigan avtomatlashtirilgan kutubxona. Faqat tayyor modellar uchun xizmat qiladi.

## Foydalanish
Dangasa kutubxonasini ishlatish uchun foydalanuvchi quyidagi qadamlarni amalga oshirishi kerak:

# O'rnatish
Birinchi navbatda, quidagi kutubxonalarni o'rnatishingiz kerak:

`pip install django`

`pip install djangorestframework`

`pip install dangasa`

`pip install typing-extensions`

# Loyihani yaratish
Loyihani yaratish uchun quyidagi qadam-larni bajaring: (yaratilayotgan loyiha 'core'  bo'lishi shart)

`django-admin startproject core .`

`python manage.py startapp home`


# settings.py faylini o'zgartirish
Loyiha sozlamalarini o'zgartirish uchun quyidagi qadam-larni bajaring:

```python
INSTALLED_APPS = [
    ...
    'home',
]
```

# urls.py faylini o'zgartirish
Loyiha sozlamalarini o'zgartirish uchun quyidagi qadam-larni bajaring:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('home.urls')),
]
```

# endi esa home app ga  model yozamiz
```python
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```
# yaratilgan modellarni migratsiya qilamiz
```bash
python manage.py makemigrations
python manage.py migrate
```


# manage.py faylini quidagicha o'zgartiring

```python
import os
import sys
import dangasa

def main():
    if '--d' in sys.argv:
        dangasa.main()
    else:
        """Run administrative tasks."""
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```



# dangasa ni ishlatish
```bash
python manage.py --d <app_name> <model_name>
```

## hozirgi holatda

```bash
python manage.py --d home Contact
```

# loyihani ishga tushurish va tekshirish
```bash
python manage.py runserver
```

