# Steps: 

1. django-admin startproject storefront .
2. python manage.py runserver { port }
3 Settings >> Installed apps >> these are where modules or functionalities are installed as 'apps'
e.g. admin, auth, content, sessions, messages, staticfiles. provides functionality.

4. Python manage.py startapp

Register new app in settings
What we call a 'view' in django is a template in other frameworks.

## Note: 

DJ is modular built in components can be replaced. 
DJ is better used to build APIs that return data. 

dont really use Django for Templating, but to build APIs that return data.

## How to debug using jango & VS code
1. VS code >> Debug >> Django 
- Set break points ect. view variables.

2. Install debug toolbar >
- https://www.google.com/search?client=firefox-b-d&q=django+debug+toolbar
- only works on full html documents.

## Models -->
Define what entitites you need. 
This example is a e-commerce store.
Entities: 
1. Product  1-many >> many-many
2. Cart  1-many >> many-many
3. Customer  1-many orders
4. Order many-many (order/product)
5. Tag many-many (product/tag)

Create models within an app. 

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
```

Create migrations:
`python manage.py makemigrations`

Migrate:
`python manage.py migrate`

## Apps 

Each DJ app has different functionality and needs a data model.

Each app should do one thing and do it well. >> 4 apps >> products, customers, arts, orders. 

Create an app with the command: 
`python manage.py startapp <app_name>`

### Admin

`python manage.py createsuperuser`

This command will create a superuser in the database, which can be used with the admin panel.

> Third party apps and your own.
> Python manage.py startapp products .ect

