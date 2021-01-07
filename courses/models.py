from django.db import models
from django.urls import reverse

# Create your models here.
class Courses(models.Model):    
    title = models.CharField( max_length=250)
    description = models.TextField()
    def __str__(self):
        return self.title

class Modules(models.Model):
    module_name = models.CharField(max_length=250)
    slug = models.SlugField(default='NULL')
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.module_name

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

class Topics(models.Model):
    topic_name = models.CharField(max_length=250)
    slug = models.SlugField(default='NULL')
    topic_attachment = models.CharField(max_length=150)
    video_url = models.CharField(max_length=250)
    module_id = models.ForeignKey(Modules, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_name

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"course_slug": self.module_id.slug, "topic_slug":self.slug})