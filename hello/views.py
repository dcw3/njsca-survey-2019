from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import Greeting

AB_KEY = "ab_value"

# Create your views here.
def index(request):
	if request.session.get(AB_KEY, None) is None:
		ab_test_val = random.randint(0, 1)
		request.session[AB_KEY] = ab_test_val

	return render(request, "index.html")
	# # TO TURN OFF A/B TESTING:
	# # replace this if/else section with a simple `return render(request, "index.html")`
	# # and then modify the index.html file in the ./templates folder to make it the way you want
	# if request.session[AB_KEY] == 0:
	# 	return render(request, "index.html")
	# else:
	# 	return render(request, "indexB.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
