from django.contrib import admin

from api.models import Project, Issue, Comment, Contributor


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'type')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'tag', 'priority', 'status', 'author_user', 'assignee_user')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'issue', 'project', 'author_user')

    @admin.display(description='Project')
    def project(self, obj):
        return obj.issue.project


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'permission', 'role')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contributor, ContributorAdmin)
