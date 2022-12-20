from rest_framework import serializers

from api.models import Project, Issue, Comment
from authentication.serializers import UserSerializer


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['pk', 'description', 'created_time']


class CommentDetailSerializer(serializers.ModelSerializer):

    author_user = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()
    issue = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['pk', 'description', 'created_time', 'author_user', 'project', 'issue']

    def get_author_user(self, instance):
        queryset = instance.author_user
        serializer = UserSerializer(queryset)
        return serializer.data

    def get_project(self, instance):
        queryset = instance.issue.project
        serializer = ProjectListSerializer(queryset)
        return serializer.data

    def get_issue(self, instance):
        queryset = instance.issue
        serializer = IssueListSerializer(queryset)
        return serializer.data


class IssueListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['pk', 'title', 'description', 'tag', 'created_time']


class IssueDetailSerializer(serializers.ModelSerializer):

    project = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['pk', 'title', 'description', 'tag', 'priority', 'status', 'created_time', 'project', 'comments']

    def get_project(self, instance):
        queryset = instance.project
        serializer = ProjectListSerializer(queryset)
        return serializer.data

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializer = CommentListSerializer(queryset, many=True)
        return serializer.data


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['pk', 'title', 'description', 'type']


class ProjectDetailSerializer(serializers.ModelSerializer):

    contributors = serializers.SerializerMethodField()
    issues = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['pk', 'title', 'description', 'type', 'contributors', 'issues']

    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializers = UserSerializer(queryset, many=True)
        return serializers.data

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializer = IssueListSerializer(queryset, many=True)
        return serializer.data
