from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_create(request):
	context = {
	"title": "create"
	}
	return HttpResponse("<h1>Create!</h1>")



def post_detail(request):
	context = {
	"title": "detail"
	}
	return render(request, "index.html", context)

def post_list(request):
	if request.user.is_authenticated():
		context = {
			"title": "personal list"
		}
		return render(request, "index.html", context)
	else:
		context = {
			"title": "list"
		}
		return render(request, "index.html", context)
	#return HttpResponse("<h1>List!</h1>")

def post_update(request):
	context = {
	"title": "update"
	}
	return HttpResponse("<h1>Update!</h1>")

def post_delete(request):
	context = {
	"title": "Delete"
	}
	return HttpResponse("<h1>Delete!</h1>")