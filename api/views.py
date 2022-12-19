from rest_framework.viewsets import ModelViewSet

from api.models import Project, Issue, Comment
from api.serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'], issue__project=self.kwargs['project_pk'])
