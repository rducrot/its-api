from rest_framework import serializers

from api.models import Project, Issue, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description', 'author_user', 'issue']


class IssueListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'status', 'project']


class IssueDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'status', 'project', 'comments']

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'contributors']


class ProjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'contributors', 'issues']

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializer = IssueListSerializer(queryset, many=True)
        return serializer.data
