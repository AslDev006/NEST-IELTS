from django.contrib import admin
from .models import *

admin.site.register([Course_Models, Certificate_Model, Subject_Model, Teacher_Model])