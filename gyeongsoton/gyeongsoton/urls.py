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
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('community/', views.community, name="community"),
    path('community/detail/<str:id>',
         views.communityDetail, name="communityDetail"),
    path('community/detail/<str:id>/addComment/',views.addComment,name='addComment'),
    path('trend/', views.trend, name="trend"),
    path('manner/', views.manners, name="manner"),
    path('manner/detail/<str:id>', views.mannersDetail, name='mannersDetail'),
    path('newterms/', views.newterms, name="newterms"),
    path('newtermQuiz/<str:id>/', views.newtermQuiz, name="newtermQuiz"),
    path('newtermQuiz/<str:id>/next/',views.newtermNext,name = "newtermNext"),
]
