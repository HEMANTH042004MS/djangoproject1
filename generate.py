import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newproject.settings')

import django
django.setup()

from newapp.models import *
from faker import Faker
from random import *
faker = Faker()


def generate(n):
    for i in range(n):
        fdirno =  randint(1,1000)
        fdirname = faker.name()
        fdirsalary = randint(54656,78964)
        fdirMOVIE = faker.city()
        Dir_record = DIRECTORS.objects.get_or_create(dirno=fdirno,dirname=fdirname,dirsalary=fdirsalary,dirMOVIE=fdirMOVIE)

generate(100)