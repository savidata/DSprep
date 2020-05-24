from django.db import models

class PythonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Subtopic='Python')

class SqlManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Subtopic='SQL')
        
class Flashcard(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    Term = models.CharField(max_length=100)
    Definition = models.CharField(max_length=500)
    Subtopic = models.CharField(max_length=100)

    objects = models.Manager()
    python_flash = PythonManager()
    sql_flash = SqlManager()

    class Meta:
        managed = False
        db_table = 'flashcards'

class User(models.Model):
    Username = models.CharField(max_length=50)
    Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'

class Topic(models.Model):
    Name = models.CharField(primary_key=True, max_length=100)
    Description = models.CharField(max_length=500)
    
    class Meta:
        managed = False
        db_table = 'topic'

class Subtopic(models.Model):
    Name = models.CharField(primary_key=True, max_length=100)
    Topic = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'subtopic'

class Question(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    Question = models.CharField(max_length=500)
    ChoiceA = models.CharField(max_length = 500)
    ChoiceB = models.CharField(max_length = 500)
    ChoiceC = models.CharField(max_length = 500)
    Answer = models.CharField(max_length=500)
    Level = models.CharField(max_length=50)
    Topic = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'questions'

class Interview(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    Question = models.CharField(max_length=500)
    Hint = models.CharField(max_length = 500)
    Subtopic = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'interview'