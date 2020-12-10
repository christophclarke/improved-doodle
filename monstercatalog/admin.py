from django.contrib import admin

from .models import Author, Book, Monster, MonsterThesis, MonsterThesisScore

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(MonsterThesis)
admin.site.register(Monster)
admin.site.register(MonsterThesisScore)
