from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

def post_create(request):
	if request.user.is_authenticated():
		form = PostForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			print form.cleaned_data.get("title")
			instance.save()
			messages.success(request, "Your post has been published.", extra_tags='html_safe')
			return HttpResponseRedirect(instance.get_absolute_url())
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
		"object_list": "LOG IN!",
		"title": "The List"
		}
	return render(request, "base.html", context)

def post_update(request, id=None):
		if request.user.is_authenticated():
			instance = get_object_or_404(Post, id=id)
			form = PostForm(request.POST or None, instance=instance)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				messages.success(request, "Edits saved.", extra_tags= 'html_safe')
				return HttpResponseRedirect(instance.get_absolute_url())
			context = {
			"title": instance.title,
			"instance": instance,
			"form": form,
			"button": 'Update'
		}
		else:
			context = {
			"title": "Log in!",
			"instance": "Log in!",
			"form": "log in!",
			"button": "Log in!",
		}
		return render(request, "post_form.html", context)


def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")





