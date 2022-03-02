from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_judge = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.username


class Project(models.Model):
    title = models.CharField(blank=False, max_length=200, null=False, unique=True)
    shortDescription = models.CharField(blank=False, max_length=100)
    mainDescription = models.TextField(blank=False)
    videoLink = models.TextField(blank=False)
    pdfLink = models.TextField(blank=False)
    image = models.ImageField(blank=False)
    likes = models.IntegerField(default=0)
    CATEGORY = [('1', 'Software'), ('2', 'Hardware'), ('3', 'Research Corner')]
    category = models.CharField(max_length=50, choices=CATEGORY, default=1)

    def __str__(self):
        return self.title

class ProjectScore(models.Model):
    project = models.ForeignKey(to=Project,blank=False, on_delete=models.DO_NOTHING )
    score = models.IntegerField(default=0)
    judgedBy = models.ForeignKey(to=CustomUser, blank=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.project)

class ProjectLike(models.Model):
    project = models.ForeignKey(to=Project,blank=False, on_delete=models.DO_NOTHING )
    likedBy = models.ForeignKey(to=CustomUser, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project)