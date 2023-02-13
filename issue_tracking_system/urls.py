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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import ProjectViewSet, IssueViewSet, CommentViewSet, ContributorViewSet
from authentication.views import UserViewSet

API_PATH = 'api/'

# Nested routers allow to build paths such as 127.0.0.1:8000:/projects/1/issues/1/comments/1/
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

contributor_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
contributor_router.register(r'users', ContributorViewSet, basename='user')

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'issues', IssueViewSet, basename='issue')

issue_router = routers.NestedSimpleRouter(project_router, r'issues', lookup='issue')
issue_router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PATH + 'signup/', UserViewSet.as_view({'post': 'create'}), name='signup'),
    path(API_PATH + 'login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(API_PATH + 'login/token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(API_PATH, include(router.urls)),
    path(API_PATH, include(contributor_router.urls)),
    path(API_PATH, include(project_router.urls)),
    path(API_PATH, include(issue_router.urls)),
]
