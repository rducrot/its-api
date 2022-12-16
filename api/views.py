from rest_framework.viewsets import ModelViewSet

from api.models import Project, Issue, Comment
from api.serializers import ProjectSerializer, IssueSerialize, CommentSerializer


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerialize

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
