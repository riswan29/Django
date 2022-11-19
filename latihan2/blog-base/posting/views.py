from django.shortcuts import render
from posting.models import Posting
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    postings = Posting.objects.all()

    return render(request, 'posting/index.html', {'postings': postings})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
