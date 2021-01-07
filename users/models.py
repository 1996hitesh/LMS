from django.db import models
from django.contrib.auth.models import User
from courses.models import Courses
from labs.models import RdpLab
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class CourseEnrolled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

class LabEnrolled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rdp_lab = models.ForeignKey(RdpLab, related_name="rdp_labs",null=True, blank=True, on_delete=models.CASCADE, default=None)
    url_lab = models.ForeignKey(RdpLab, related_name="url_labs",null=True, blank=True, on_delete=models.CASCADE, default=None)
