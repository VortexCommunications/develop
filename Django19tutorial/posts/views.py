from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post
def post_create(request):
	context = {
	"title": "Your create function"
	}
	return render(request, "index.html", context)



def post_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": "instance.title"
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	if request.user.is_authenticated():
		queryset = Post.objects.all()
		context = {
			"object_list": queryset,
			"title": "The list"
		}
	else:
		context = {
		"object_list": "You're not authenticated. Shame.",
		"title": "The List"
		}
#		return render(request, "index.html", context)
#	else:
#		context = {
#			"title": "The list view"
#		}
	return render(request, "index.html", context)
	#return HttpResponse("<h1>List!</h1>")

def post_update(request):
	context = {
	"title": "The update function"
	}
	return render(request, "index.html", context)

def post_delete(request):
	context = {
	"title": "Your delete function"
	}
	return render(request, "index.html", context)