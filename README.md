# User authentication template for Django ~~and Reactjs~~ applications

## 1.Introduction
This template has *basic* features/functionalities for a **user authentication** oriented application plus a **user note example**. This template was created following this [JWT token reference](https://www.youtube.com/watch?v=xjMP0hspNLE&t=3375s&ab_channel=DennisIvy) and this [Djoser endpoints reference](https://www.youtube.com/watch?v=QFDyXWRYQjY&list=PLJRGQoqpRwdfoa9591BcUS6NmMpZcvFsM&ab_channel=BryanBrkic)

## 2.How to install
### 2a.Backend
> [!WARNING]
> Remember to create virtualenv using **virtualenv env** before installing these packages

> [!WARNING]
> Remember to enter virtualenv using **env\Scripts\activate** before installing these packages
```
    pip install djangorestframework djangorestframework-simplejwt django-cors-headers djoser
```
```
    python manage.py makemigrations
```
```
    python manage.py migrate
```
> [!WARNING]
> Remember to enter backend folder before runservre
```
    python manage.py runserver
```

## 3.Attention
- Customized emails can be modified in backend/account/templates/emails and backend/account/email.py (and settings.py)
- Django data can be deleted using "python manage.py flush"
- Create superuser using "python manage.py createsupauser" (after cd into backend) to create superuser (credentials: nhien/1234)

## 4.All features
All the features that have been added to this template
- User authentication actions
    + Login/Logout
    + Sign up
    + Reset password
    + A user note example 
