from django.shortcuts import render
from posting.models import Posting
# Create your views here.
def index(request):
    postings = Posting.objects.all()

    return render(request, 'posting/index.html', {'postings': postings})
