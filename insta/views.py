from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import NewCommentForm, NewPostForm
from django.views.generic import ListView, UpdateView, DeleteView
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