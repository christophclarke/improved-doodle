from django.shortcuts import get_object_or_404, render

# Create your views here.
from monstercatalog.models import Author, Book, Monster, MonsterThesis, MonsterThesisScore


def index(request):
    monsters = Monster.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    theses = MonsterThesis.objects.all()
    return render(request, 'monstercatalog/dash_landing.html', {
        'monsters': monsters,
        'books':    books,
        'authors':  authors,
        'theses':   theses
    })


def monster_list(request):
    monsters = Monster.objects.all()
    return render(request, 'monstercatalog/monster_list_page.html', {'monsters': monsters})


def monster_detail(request, monster_id):
    monster = get_object_or_404(Monster, pk=monster_id)
    thesis_scores = MonsterThesisScore.objects.filter(monster_id=monster.id).order_by('thesis_id')
    return render(request, 'monstercatalog/monster_detail_page.html', {'monster': monster, 'scores': thesis_scores})


def books_list(request):
    books = Book.objects.all()
    return render(request, 'monstercatalog/book_list_page.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    monsters = Monster.objects.filter(book_id=book_id)
    return render(request, 'monstercatalog/book_detail_page.html', {'book': book, 'monsters': monsters})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'monstercatalog/author_list_page.html', {'authors': authors})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author_id=author_id)
    return render(request, 'monstercatalog/author_detail_page.html', {'author': author, 'books': books})


def theses_list(request):
    theses = MonsterThesis.objects.all()
    return render(request, 'monstercatalog/thesis_list_page.html', {'theses': theses})


def thesis_detail(request, thesis_id):
    thesis = get_object_or_404(MonsterThesis, pk=thesis_id)
    return render(request, 'monstercatalog/thesis_detail_page.html', {'thesis': thesis})


def thesis_comparison(request):
    theses = MonsterThesis.objects.all().order_by('id')
    scores = MonsterThesisScore.objects.all()
    score_json = monster_scores_to_json(scores)
    return render(request, 'monstercatalog/thesis_compare.html', {'theses': theses, 'scores': scores, 'score_json': score_json})


def monster_scores_to_json(monster_scores):
    score_dict = {}
    for score in monster_scores:
        if score.monster.name in score_dict.keys():
            score_dict[score.monster.name]['scores'][score.thesis.id - 1] = score.score
        else:
            score_dict[score.monster.name] = {
                "name":       score.monster.name,
                "monster_id": score.monster.id,
                "scores":     [0] * 7
            }
            score_dict[score.monster.name]['scores'][score.thesis.id - 1] = score.score

    score_ret = [mons_obj for mons_obj in score_dict.values()]
    print(score_ret)
    return score_ret
