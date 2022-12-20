"""issue_tracking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework_nested import routers

from api.views import ProjectViewSet, IssueViewSet, CommentViewSet
from authentication.views import UserViewSet

API_PATH = 'api/'

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

user_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
user_router.register(r'users', UserViewSet, basename='user')

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'issues', IssueViewSet, basename='issue')

issue_router = routers.NestedSimpleRouter(project_router, r'issues', lookup='issue')
issue_router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PATH, include(router.urls)),
    path(API_PATH, include(user_router.urls)),
    path(API_PATH, include(project_router.urls)),
    path(API_PATH, include(issue_router.urls)),
]
