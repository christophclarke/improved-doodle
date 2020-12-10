import json

from django.shortcuts import get_object_or_404, render

# Create your views here.
from monstercatalog.models import Monster, MonsterThesis, MonsterThesisScore


def index(request):
    return render(request, 'monstercatalog/landing.html', {})


def monster_detail(request, monster_id):
    monster = get_object_or_404(Monster, pk=monster_id)
    thesis_scores = MonsterThesisScore.objects.filter(monster_id=monster.id).order_by('thesis_id')
    return render(request, 'monstercatalog/monster_detail_page.html', {'monster': monster, 'scores': thesis_scores})


def thesis_detail(request, thesis_id):
    thesis = get_object_or_404(MonsterThesis, pk=thesis_id)
    return render(request, 'monstercatalog/thesis_detail.html', {'thesis': thesis})


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
                "name": score.monster.name,
                "monster_id": score.monster.id,
                "scores": [0] * 7
            }
            score_dict[score.monster.name]['scores'][score.thesis.id - 1] = score.score

    score_ret = [mons_obj for mons_obj in score_dict.values()]
    print(score_ret)
    return score_ret
