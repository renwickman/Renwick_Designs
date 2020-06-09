from django.db import models
import re
import bcrypt
from datetime import *


class UserManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        get_email = User.objects.filter(email=requestPOST['email'])
        EMAIL_REGEX = re.compile(r'^[A-Za-z0-9]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(requestPOST['first_name']) < 2:
            errors['fname_length'] = "First name is too short"
        if len(requestPOST['last_name']) < 2:
            errors['lname_length'] = "Last name is too short"
        if len(requestPOST['password']) == 0:
            errors['no_password'] = "Please enter your password."
        if len(requestPOST['password']) < 8:
            errors['password'] = "Password is too short"
        if requestPOST['password'] != requestPOST['password_conf']:
            errors['no_match'] = "Password and Password Confirmation must match"
        if len(get_email) > 0:
            errors["email_exists"] = "Email already exists"
        if len(requestPOST['password_conf']) == 0:
            errors["not_confirmed"] = "Please confirm your password."
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors["email_regex"] = "Email must be valid email"
        if not (requestPOST['first_name'].isalpha()):
            errors["alpha"] = "Name cannot contain numbers!"
        if not (requestPOST['last_name'].isalpha()):
            errors["alpha"] = "Name cannot contain numbers!"
        return errors

class LocationManager(models.Manager):
    def location_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['address']) < 7:
            errors['address'] = "Address is too short"
        if not (requestPOST['city'].isalpha()):
            errors['city_num'] = "City cannot contain numbers!"
        if len(requestPOST['city']) < 3:
            errors['city_short'] = "City is too short"
        if not (requestPOST['state'].isalpha()):
            errors["state_num"] = "State cannot contain numbers!"
        if len(requestPOST['state']) < 1:
            errors['state'] = "State is too short"
        if not (requestPOST['zip_code'].isnumeric()):
            errors["state"] = "Zip Code cannot contain letters!"
        if len(requestPOST['zip_code']) < 4:
            errors['state'] = "Zip Code is too short"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Location(models.Model):
    address =  models.CharField(max_length=150)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = LocationManager()

class Design(models.Model):
    context = models.CharField(max_length=60, null=True)
    consultation = models.DateTimeField(null=True)
    fee = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    charge = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    grand_total = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    project = models.CharField(max_length=60, null=True)
    guests = models.CharField(max_length=60, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)



# Create your models here.
