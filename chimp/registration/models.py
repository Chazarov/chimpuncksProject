from django.db import models

class User(models.Model):
    user_type = models.CharField('Студент/препод/гость', max_length=30)
    login = models.CharField('login', max_length=30)
    pasw = models.TextField('pasw')
    code = models.TextField('code', default='')

    def __str__(self):
        return self.login

class EnterPass(models.Model):
    user_type = models.CharField('Студент/препод/гость', max_length=30)
    password = models.CharField('Enter password', max_length=30, primary_key=True)

    def __str__(self):
        return self.password