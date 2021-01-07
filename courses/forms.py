from django import forms
from django.contrib.auth.models import User
from .models import Courses, Modules, Topics

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'
        help_texts = {
            'title': 'Enter Title.',
            'description':'Description of the Course.'
        }

class ModulesForm(forms.ModelForm):
    class Meta:
        model = Modules
        fields = ['module_name','slug', 'course_id']
        help_texts = {
            'module_name': 'Enter Module Name.',
        }
        labels = {
            'module_name':'Titulli i lendes'
        }
        widgets = {'course_id': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics 
        fields = ['slug','topic_name', 'module_id', 'video_url', 'topic_attachment', ]
        help_texts = {
            'topic_name':'Vendosni titullin e mesimit',
            'video_url':'Vendosni ID e videos nga Youtube te cilen do te ngarkoni (<a href="/media/youtube_help.png">ku mund ta gjej ID</a>)',
            'topic_attachment':'Vendosni numrin e pozicionit ose radhen e mesimit '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }