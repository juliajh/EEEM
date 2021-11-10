from typing import Text
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q, Count
from .models import communityText
from .models import manner
from .models import newterm
from .models import communityComment
from .models import product
from django.utils import timezone
from django.contrib import messages
import datetime
import random

# Create your views here.


def home(request):
    return render(request, "homepage.html")

#community
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


def addCommunity(request):
    if request.user.is_authenticated:
        community = communityText()
        community.date = timezone.datetime.now()
        community.like = 0
        community.dis_like = 0
        community.text = request.POST.get("communitytext")
        community.user = request.user
        community.title = request.POST.get("communitytitle")
        if request.POST.get('matching', False):
            print('in')
        if community.text and community.title:
            community.save()
        return redirect("communityDetail", community.id)
    else:
        return redirect("404error")


def toaddCommunitypage(request):
    if request.user.is_authenticated:
        return render(request, "addCommunity.html")
    else:
        return redirect("404error")


def communityCommentLikeUp(request, community_id, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(communityComment, pk=comment_id)
        comment.like += 1
        comment.save()
        return redirect("communityDetail", community_id)
    else:
        return redirect("404error")


def communityCommentDisLikeUp(request, community_id, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(communityComment, pk=comment_id)
        comment.dis_like += 1
        comment.save()
        return redirect("communityDetail", community_id)
    else:
        return redirect("404error")

def toEditCommunitypage(request,id):
    edit_community=communityText.objects.get(pk=id)
    return render(request,'editCommunity.html',{'community':edit_community})

def communityEdit(request,id):
    edit_community=communityText.objects.get(pk=id)
    edit_community.text=request.POST.get('text',False)
    edit_community.title=request.POST.get('title',False)
    edit_community.date=timezone.datetime.now()
    edit_community.writer=request.user
    edit_community.save()
    return redirect('communityDetail',edit_community.id)

def communityDelete(request, id):
    community = get_object_or_404(communityText, pk=id)
    if request.user != community.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('communityDetail', id=community.id)
    community.delete()
    return redirect('community')

def trend(request):
    return render(request, "trend.html")

#매너를 지켜쥬
def manners(request):
    manner_alltext = manner.objects.all()
    manner_alltext = manner.objects.order_by('-date')
    return render(request, "manner.html", {"manner": manner_alltext})


def mannerOrder(request):
    manner_alltext = manner.objects.all()
    manner_alltext = manner.objects.order_by('-like')
    return render(request, "mannerorder.html", {"manner": manner_alltext})


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


def mannerSearch(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        result = manner.objects.all().filter(
            Q(hashtag_me__icontains=query) |
            Q(hashtag_you__icontains=query)
        )
    return render(request, "mannerSearch.html", {'query': query, 'result': result})


def addManner(request):
    return render(request, "addmanner.html")


def mannerCreate(request):
    if(request.method == 'POST'):
        post = manner()
        post.user = request.user
        post.text = request.POST['title']
        post.hashtag_me = request.POST['hashtagMe']
        post.hashtag_you = request.POST['hashtagYou']
        post.hashtag_situation = request.POST['body']
        post.like = 0
        post.dis_like = 0
        post.save()
    return redirect('manner')


def mannerdelete(request, id):
    question = get_object_or_404(manner, pk=id)
    if request.user != question.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('manner', id=question.id)
    question.delete()
    return redirect('manner')

def toEditMannerpage(request,id):
    edit_manner=manner.objects.get(pk=id)
    return render(request,'editManner.html',{'manner':edit_manner})

def mannerEdit(request,id):
    edit_manner=manner.objects.get(pk=id)
    edit_manner.text=request.POST.get('text',False)
    edit_manner.hashtag_situation=request.POST.get('hashtag_situation',False)
    edit_manner.date=timezone.datetime.now()
    edit_manner.writer=request.user
    edit_manner.save()
    return redirect('mannersDetail',edit_manner.id)

#newterms
def newterms(request):
    newterm_quiz = newterm.objects.all()
    tYear = datetime.datetime.today().year
    return render(request, "newterms.html", {"new_term": newterm_quiz, "year": tYear})


def newtermQuiz(request, id):
    newtermCount = newterm.objects.count()-1
    if id == 0:
        term = get_object_or_404(newterm, pk=id)
    else:
        previousTerm = get_object_or_404(newterm, pk=id)
        termId = int(id) + 1
        term = get_object_or_404(newterm, pk=termId)
        term.score = previousTerm.score
    term.randanswer = random.randint(0, 1)
    term.save()

    if term.randanswer == 0:
        return render(
            request,
            "newtermQuiz.html",
            {"term": term, "choice_1": term.answer,
                "choice_2": term.non_answer, "newtermCount": newtermCount},
        )
    else:
        return render(
            request,
            "newtermQuiz.html",
            {"term": term, "choice_1": term.non_answer,
                "choice_2": term.answer, "newtermCount": newtermCount},
        )


def newtermEnd(request, score):
    tYear = datetime.datetime.today().year
    now = datetime.datetime.now()
    newtermCount = newterm.objects.count()-1
    if score > newtermCount*0.5:
        if score > newtermCount*0.7:
            level = 3
        else:
            level = 2
    else:
        level = 1
    return render(request, "newtermEnd.html", {"score": score, "newtermCount": newtermCount, "year": tYear, "now": now, "level": level})


def newtermButton1(request, id):
    term = get_object_or_404(newterm, pk=id)
    newtermCount = newterm.objects.count()
    if term.randanswer == 0:
        term.correct = True
        term.score += 1
        term.save()
    else:
        term.correct = False
        term.save()
    c = newtermCount
    if int(id) < c:
        return redirect("newtermQuiz", id)
    else:
        return redirect("newtermEnd", term.score)


def newtermButton2(request, id):
    term = get_object_or_404(newterm, pk=id)
    newtermCount = newterm.objects.count()
    if term.randanswer == 1:
        term.correct = True
        term.score += 1
        term.save()
    else:
        term.correct = False
        term.save()
    c = newtermCount
    if int(id) < c:
        return redirect("newtermQuiz", id)
    else:
        return redirect("newtermEnd", term.score)


def addComment(request, id):
    if request.user.is_authenticated:
        comment = communityComment()
        comment.date = timezone.datetime.now()
        comment.like = 0
        comment.dis_like = 0
        comment.text = request.POST.get("commenttext")
        comment.user = request.user
        if comment.text:
            comment.communitytext = get_object_or_404(communityText, pk=id)
            comment.save()
        return redirect("communityDetail", id)
    else:
        return redirect("404error")


def notfound(request):
    return render(request, "404error.html")

#신문물
def newproduct(request):
    new_product = product.objects.all()
    new_product = product.objects.order_by('-date')
    now = datetime.datetime.now()  # 현재 시간. ~분전 하고 싶어서 .!
    return render(request, "newproduct.html", {'products': new_product, 'now': now})


def newproductOrder(request):
    new_product = product.objects.all()
    new_product = product.objects.order_by('-like')
    now = datetime.datetime.now()  # 현재 시간. ~분전 하고 싶어서 .!
    return render(request, "newproductorder.html", {'products': new_product, 'now': now})


def newproductDetail(request, id):
    product_detail = get_object_or_404(product, pk=id)
    return render(request, "newproductDetail.html", {"productDetail": product_detail})


def communitySearch(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        result = communityText.objects.all().filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
        )
    return render(request, "communitySearch.html", {'query': query, 'result': result})

def newproductSearch(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        result = product.objects.all().filter(
            Q(productName__icontains=query)
        )
    return render(request, 'newProductSearch.html', {'query': query, 'result': result})

def productLikeUp(request, id):
    productDetail = get_object_or_404(product, pk=id)
    productDetail.like += 1
    productDetail.save()
    return redirect("newproductDetail", id)

def addProduct(request):
    return render(request, "addProduct.html")


def productCreate(request):
    if(request.method == 'POST'):
        post = product()
        post.user = request.user
        post.date = timezone.datetime.now()
        post.productName = request.POST['productName']
        post.productText = request.POST['productText']
        post.like = 0
        if 'image' in request.FILES:
            post.image=request.FILES['image']
            post.save()
            return redirect('newproductDetail',post.id)
    else:
        return redirect('newproduct')