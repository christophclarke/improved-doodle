from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    born = models.DateField(null=True, blank=True)
    died = models.DateField(null=True, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title


class MonsterThesis(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Thesis {self.id}: {self.title}"


class Monster(models.Model):
    name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class MonsterThesisScore(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name='thesis_score')
    thesis = models.ForeignKey(MonsterThesis, on_delete=models.CASCADE, related_name='monster_score')
    score = models.FloatField()
    description = models.TextField(blank=True)
    quote = models.TextField(blank=True)

    def __str__(self):
        return f"{self.monster.name} {self.thesis.id} Score"
