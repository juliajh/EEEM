from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .models import communityText
from .models import manner
from .models import newterm
from .models import communityComment
from django.utils import timezone
import random

# Create your views here.


def home(request):
    return render(request, "homepage.html")


def community(request):
    community_alltext = communityText.objects.all()
    return render(request, "community.html", {"communities": community_alltext})


def communityDetail(request, id):
    community = get_object_or_404(communityText, pk=id)
    allComments = communityComment.objects.filter(communitytext=community)
    return render(
        request,
        "communityDetail.html",
        {"community": community, "comments": allComments},
    )


def communityCommentLikeUp(request, community_id, comment_id):
    comment = get_object_or_404(communityComment, pk=comment_id)
    comment.like += 1
    comment.save()
    return redirect("communityDetail", community_id)


def communityCommentDisLikeUp(request, community_id, comment_id):
    comment = get_object_or_404(communityComment, pk=comment_id)
    comment.dis_like += 1
    comment.save()
    return redirect("communityDetail", community_id)


def trend(request):
    return render(request, "trend.html")


def manners(request):
    manner_alltext = manner.objects.all()
    return render(request, "manner.html", {"manner": manner_alltext})


def mannersDetail(request, id):
    manner_detail = get_object_or_404(manner, pk=id)
    return render(request, "mannersDetail.html", {"mannersdetail": manner_detail})


def mannerLikeUp(request, id):
    manner_detail = get_object_or_404(manner, pk=id)
    manner_detail.like += 1
    manner_detail.save()
    return redirect("mannersDetail", id)


def mannerDisLikeUp(request, id):
    manner_detail = get_object_or_404(manner, pk=id)
    manner_detail.dis_like += 1
    manner_detail.save()
    return redirect("mannersDetail", id)


def newterms(request):
    newterm_quiz = newterm.objects.all()
    return render(request, "newterms.html", {"new_term": newterm_quiz})


def newtermQuiz(request, id):
    if id == 0:
        term = get_object_or_404(newterm, pk=id)
    else:
        previousTerm = get_object_or_404(newterm, pk=id)
        termId = int(id) + 1
        term = get_object_or_404(newterm, pk=termId)
        term.score = previousTerm.score
    term.radanswer = random.randint(0, 1)
    term.save()
    if term.randanswer == 0:
        return render(
            request,
            "newtermQuiz.html",
            {"term": term, "choice_1": term.answer, "choice_2": term.non_answer},
        )
    else:
        return render(
            request,
            "newtermQuiz.html",
            {"term": term, "choice_1": term.non_answer, "choice_2": term.answer},
        )


def newtermEnd(request, score):
    return render(request, "newtermEnd.html", {"score": score})


def newtermButton1(request, id):
    term = get_object_or_404(newterm, pk=id)
    if term.randanswer == 0:
        term.correct = True
        term.score += 1
        term.save()
    else:
        term.correct = False
        term.save()
    if int(id) < 5:
        return redirect("newtermQuiz", id)
    else:
        return redirect("newtermEnd", term.score)


def newtermButton2(request, id):
    term = get_object_or_404(newterm, pk=id)
    if term.randanswer == 1:
        term.correct = True
        term.score += 1
        term.save()
    else:
        term.correct = False
        term.save()
    if int(id) < 5:
        return redirect("newtermQuiz", id)
    else:
        return redirect("newtermEnd", term.score)


def addComment(request, id):
    comment = communityComment()
    comment.date = timezone.datetime.now()
    comment.like = 0
    comment.dis_like = 0
    comment.text = request.POST.get("commenttext")
    if comment.text:
        comment.communitytext = get_object_or_404(communityText, pk=id)
        comment.save()
    return redirect("communityDetail", id)


def search(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        result = manner.objects.all().filter(
            Q(hashtag_me__icontains=query) |
            Q(hashtag_you__icontains=query)
        )
    # if 'kw2' in request.GET:
    #     query2 = request.GET.get('kw2')
    #     result = manner.objects.all().filter(
    #         Q(hashtag_me__icontains=query2) |
    #         Q(hashtag_you__icontains=query2)
    #     )
    return render(request, "mannerSearch.html", {'query': query, 'result': result})
