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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', views.home, name="home"),
    path('community/', views.community, name="community"),
    path('community/addCommunity', views.addCommunity, name="addCommunity"),
    path('community/toaddCommunitypage',
         views.toaddCommunitypage, name="toaddCommunitypage"),
    path('community/detail/<str:id>',
         views.communityDetail, name="communityDetail"),
    path('community/detail/<str:id>/addComment/',
         views.addComment, name='addComment'),
    path('community/detail/<str:community_id>/likeup/<comment_id>/',
         views.communityCommentLikeUp, name='communityCommentLikeUp'),
    path('community/detail/<str:community_id>/dislikeup/<comment_id>/',
         views.communityCommentDisLikeUp, name='communityCommentDisLikeUp'),
    path('community/search', views.communitySearch, name="communitysearch"),
    path('trend/', views.trend, name="trend"),
    path('manner/', views.manners, name="manner"),
    path('manner/detail/<str:id>', views.mannersDetail, name='mannersDetail'),
    path('manner/detail/<str:id>/likeup',
         views.mannerLikeUp, name="mannerLikeUp"),
    path('manner/detail/<str:id>/dislikeup',
         views.mannerDisLikeUp, name="mannerDisLikeUp"),
    path('manner/search/', views.search, name="search"),
    path('manner/addmanner/', views.addManner, name="addManner"),
    path('newterms/', views.newterms, name="newterms"),
    path('newtermQuiz/<str:id>/', views.newtermQuiz, name="newtermQuiz"),
    path('newtermQuiz/<str:id>/button1',
         views.newtermButton1, name="newtermButton1"),
    path('newtermQuiz/<str:id>/button2',
         views.newtermButton2, name="newtermButton2"),
    path('newterms/<int:score>/result', views.newtermEnd, name="newtermEnd"),
    path('404/', views.notfound, name="404error"),
    path('newproduct/', views.newproduct, name="newproduct"),
    path('newproductDetail/<str:id>',
         views.newproductDetail, name='newproductDetail'),
    path('newproduct/addProduct', views.addProduct, name="addProduct"),
    path('newproduct/search/', views.newproductSearch, name="newproductSearch"),
    path('newproductDetail/<str:id>/likeup',
         views.productLikeUp, name="productLikeUp"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

