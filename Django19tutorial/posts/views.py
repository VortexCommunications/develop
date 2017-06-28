from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

def post_create(request):
	if request.user.is_authenticated():
		form = PostForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			print form.cleaned_data.get("title")
			instance.save()
		context = {
		"form": form, 
		"title": "Your create function",
		"theTitle": "Write post",
		"button": "Submit post"
		}
		return render(request, "post_form.html", context)
	else:
		context= {
		"form": "Log in",
		"title": "log in"
		}


def post_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
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
		"shame": "You haven't logged in!",
		"object_list": "shame",
		"title": "The List"
		}
	return render(request, "index.html", context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
		"button": 'Update post'
	}
	return render(request, "post_form.html", context)


def post_delete(request):
	context = {
	"title": "Your delete function"
	}
	return render(request, "index.html", context)