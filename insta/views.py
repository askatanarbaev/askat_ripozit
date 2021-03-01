from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import NewCommentForm, NewPostForm, CreateProfileForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json


class PostListView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		return context


@login_required
def my_profile(request):
	p = request.user.profile
	user_posts = Post.objects.all()
	return render(request, "profile.html", locals())


class NewProfileView(CreateView, LoginRequiredMixin):
	model = Profile
	template_name = 'create_profile.html'
	form_class = CreateProfileForm
	context_object_name = 'new_profile'

	def form_valid(self, form):
		user = form.save(commit=False)
		user.user = self.request.user
		user.save()
		return redirect('my_profile')


def post_create(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            photo = form.instance
            return redirect('my_profile')
    else:
        form = NewPostForm()
    return render(request, 'post_create.html', locals())



