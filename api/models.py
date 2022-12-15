from django.db import models
from django.conf import settings


class Project(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=4096)

    class Type(models.TextChoices):
        BACK_END = 'BE'
        FRONT_END = 'FE'
        IOS = 'IO'
        ANDROID = 'AN'

    type = models.CharField(choices=Type.choices, max_length=5)

    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Contributor',
                                          related_name='contributions')


class Issue(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=4096)

    class Tag(models.TextChoices):
        BUG = 'BU'
        UPGRADE = 'UP'
        TASK = 'TA'

    class Priority(models.TextChoices):
        LOW = 'LO'
        MEDIUM = 'ME'
        HIGH = 'HI'

    class Status(models.TextChoices):
        NEW = 'NE'
        PROCESSING = 'PR'
        SOLVED = 'SO'

    tag = models.CharField(choices=Tag.choices, max_length=5)
    priority = models.CharField(choices=Priority.choices, max_length=5)
    status = models.CharField(choices=Status.choices, max_length=5)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='issues')
    assignee_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                      related_name='assigned_issues')

    created_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):

    description = models.CharField(max_length=4096)

    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')

    created_time = models.DateTimeField(auto_now=True)


class Contributor(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Permission(models.TextChoices):
        AUTHOR = 'AU'
        CONTRIBUTOR = 'CO'

    permission = models.CharField(choices=Permission.choices, max_length=5)
    role = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'project')
