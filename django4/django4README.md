# Django4 README

## Django Rest Framework (DRF)

### Steps to Create a Form with Django Rest Framework and OOP
#### ***(example project, app, folders and classes; different from actual files in "django4" folder; AI GENERATED)***

#### 1. Initial Project Setup

1. **Create a Django project:**
   ```
   django-admin startproject myproject
   cd myproject
   ```

2. **Create a Django app:**
   ```bash
   python manage.py startapp myapp
   ```

3. **Install Django Rest Framework:**
   Add `djangorestframework` to your `requirements.txt` file or install directly:
   ```bash
   pip install djangorestframework
   ```

4. **Add `rest_framework` to the `INSTALLED_APPS` in the project's `settings.py`:**
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'myapp',
   ]
   ```

#### 2. Creating the Model

1. **Define your model in the app's `models.py`:**
   ```python
   from django.db import models

   class Contact(models.Model):
       name = models.CharField(max_length=100)
       email = models.EmailField()
       message = models.TextField()

       def __str__(self):
           return self.name
   ```

2. **Run the migrations to create the table in the database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

#### 3. Creating the Serializer

1. **Create a serializer for the `Contact` model in the app's `serializers.py`:**
   ```python
   from rest_framework import serializers
   from .models import Contact

   class ContactSerializer(serializers.ModelSerializer):
       class Meta:
           model = Contact
           fields = '__all__'
   ```

#### 4. Creating the View

1. **Create a class-based view in the app's `views.py`:**
   ```python
   from rest_framework import generics
   from .models import Contact
   from .serializers import ContactSerializer

   class ContactCreateView(generics.CreateAPIView):
       queryset = Contact.objects.all()
       serializer_class = ContactSerializer
   ```

#### 5. Configuring the URL

1. **Add the view's URL to the app's `urls.py`:**
   ```python
   from django.urls import path
   from .views import ContactCreateView

   urlpatterns = [
       path('contact/', ContactCreateView.as_view(), name='contact-create'),
   ]
   ```

2. **Include the app's URLs in the project's `urls.py`:**
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('myapp.urls')),
   ]
   ```
