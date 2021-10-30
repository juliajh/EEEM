"""gyeongsoton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from main import views
from account import views as account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', views.home, name="home"),
    path('community/', views.community, name="community"),
    path('community/detail/<str:id>',
         views.communityDetail, name="communityDetail"),
    path('community/detail/<str:id>/addComment/',
         views.addComment, name='addComment'),
    path('community/detail/<str:community_id>/likeup/<comment_id>/',
         views.communityCommentLikeUp, name='communityCommentLikeUp'),
    path('community/detail/<str:community_id>/dislikeup/<comment_id>/',
         views.communityCommentDisLikeUp, name='communityCommentDisLikeUp'),
    path('trend/', views.trend, name="trend"),
    path('manner/', views.manners, name="manner"),
    path('manner/detail/<str:id>', views.mannersDetail, name='mannersDetail'),
    path('manner/detail/<str:id>/likeup',
         views.mannerLikeUp, name="mannerLikeUp"),
    path('manner/detail/<str:id>/dislikeup',
         views.mannerDisLikeUp, name="mannerDisLikeUp"),
    path('newterms/', views.newterms, name="newterms"),
    path('newtermQuiz/<str:id>/', views.newtermQuiz, name="newtermQuiz"),
    path('newtermQuiz/<str:id>/button1',
         views.newtermButton1, name="newtermButton1"),
    path('newtermQuiz/<str:id>/button2',
         views.newtermButton2, name="newtermButton2"),
    path('newterms/<int:score>/result', views.newtermEnd, name="newtermEnd"),
    path('manner/search/', views.search, name="search"),
]
