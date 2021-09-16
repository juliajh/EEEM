from django.shortcuts import get_object_or_404, render
from .models import communityText
from .models import manner
from .models import newterm

# Create your views here.


def home(request):
    return render(request, "homepage.html")


def community(request):
    community_alltext = communityText.objects.all()
    return render(request, "community.html", {'communities': community_alltext})


def communityDetail(request, id):
    community = get_object_or_404(communityText, pk=id)
    return render(request, 'communityDetail.html', {'community': community})


def trend(request):
    return render(request, "trend.html")


def game(request):
    return render(request, "game.html")


def manners(request):
    manner_alltext = manner.objects.all()
    return render(request, "manner.html", {'manner': manner_alltext})


def mannersDetail(request, id):
    manner_detail = get_object_or_404(manner, pk=id)
    return render(request, "mannersDetail.html", {'mannersdetail': manner_detail})


def newterms(request):
    newterm_quiz = newterm.objects.all()
    return render(request, "newterms.html", {'new_term': newterm_quiz})


def newtermQuiz(request, id):
    term = get_object_or_404(newterm, pk=id)
    return render(request, "newtermQuiz.html", {'term': term})
