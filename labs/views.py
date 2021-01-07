from django.shortcuts import render
from django.views import generic
from .models import RdpLab,UrlLab
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import LabEnrolled

# Create your views here.


def labs(request):
    return render(request, 'labs/labs.html')

class RdpDownloadView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'labs/labs.html'
    context_object_name = 'labs_list' 
    queryset = RdpLab.objects.all()

    def get(self, request):
        userid = request.user.id
        lab_enrolled = LabEnrolled.objects.filter(user = userid).all()
        print(lab_enrolled)
        return render(request, self.template_name, {"labs": lab_enrolled})


    def get_context_data(self, **kwargs):
        context = super(RdpDownloadView, self).get_context_data(**kwargs)
        context['labs_list'] = UrlLab.objects.all()
        # And so on for more models
        return context
