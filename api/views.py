from rest_framework.viewsets import ModelViewSet

from api import serializers
from api.models import Project, Issue, Comment


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        # Notre mixin détermine quel serializer à utiliser
        # même si elle ne sait pas ce que c'est ni comment l'utiliser
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            # Si l'action demandée est le détail alors nous retournons le serializer de détail
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = serializers.ProjectListSerializer
    detail_serializer_class = serializers.ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = serializers.IssueListSerializer
    detail_serializer_class = serializers.IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])


class CommentViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = serializers.CommentListSerializer
    detail_serializer_class = serializers.CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'], issue__project=self.kwargs['project_pk'])

