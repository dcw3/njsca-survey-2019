from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import Greeting

# Create your views here.
def index(request):
	int ab_test_val = random.randint(0, 1);
	if ab_test_val == 0:
    	return render(request, "index.html")
    else:
    	return HttpResponse("hi I am B version")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
