from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from PIL import Image

# Create your models here.
class Doctors(User):
    phone_number = PhoneNumberField(blank=True)

    class Meta: 
        verbose_name_plural = 'Doctors'

class Paitents():
    pass

class Profile():
    pass
