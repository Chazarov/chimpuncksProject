from django.db import models

class Task(models.Model):
    task_id = models.CharField("id задачи", max_length=50) 
    title = models.TextField("Описание")
    name = models.CharField("Имя задачи", max_length=50)

    def __str__(self):
        return self.name
    

class Test(models.Model):
    user_id = models.CharField("ID пользователя", max_length=30)
    task_id = models.CharField("Id задачи", max_length=30)
    resolve = models.TextField("Файл с тестом")
    def __str__(self):
        return self.task_id

    
class Resolve(models.Model):
    user_id = models.CharField("ID пользователя", max_length=30)
    resolve_date = models.CharField("Дата и время", max_length=100)
    resolve_language = models.CharField("Язык", max_length=30)
    task_id = models.CharField("ID задачи", max_length=50)
    resolve = models.TextField("Файл с решением")
    decision_status = models.CharField("Статус решения (верно/неверно)", max_length=30)

    def __str__(self):
        return self.task_id