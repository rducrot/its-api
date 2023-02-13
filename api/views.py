from rest_framework.viewsets import ModelViewSet

from api.permissions import ProjectPermission, IssuePermission, CommentPermission, ContributorPermission
from api import serializers
from api.models import Project, Issue, Comment, Contributor


class MultipleSerializerMixin:
    """
    Mixin that returns a serializer depending on list or detail view.
    """
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    View set for projects with a filter that only returns projects where the user is a contributor.
    """

    permission_classes = [ProjectPermission]

    serializer_class = serializers.ProjectListSerializer
    detail_serializer_class = serializers.ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.filter(contributors=self.request.user)


class ContributorViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    View set that returns the contributors of a project.
    """

    permission_classes = [ContributorPermission]

    serializer_class = serializers.ContributorListSerializer
    detail_serializer_class = serializers.ContributorDetailSerializer

    lookup_field = 'user_id'

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        serializer.save(project=Project.objects.get(id=self.kwargs['project_pk']),
                        permission=Contributor.Permission.CONTRIBUTOR)


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    View set that returns the issues of a project.
    """

    permission_classes = [IssuePermission]

    serializer_class = serializers.IssueListSerializer
    detail_serializer_class = serializers.IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'], project__contributors=self.request.user)

    def perform_create(self, serializer):
        serializer.save(project=Project.objects.get(id=self.kwargs['project_pk']),
                        author_user=self.request.user)


class CommentViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    View set that returns the comments of an issue.
    """

    permission_classes = [CommentPermission]

    serializer_class = serializers.CommentListSerializer
    detail_serializer_class = serializers.CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'], issue__project=self.kwargs['project_pk'],
                                      issue__project__contributors=self.request.user)

    def perform_create(self, serializer):
        serializer.save(issue=Issue.objects.get(id=self.kwargs['issue_pk']),
                        author_user=self.request.user)
