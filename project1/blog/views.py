#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from models import Blog
from forms import AddForm
def list(request):
    list = Blog.objects.all()
    return render_to_response('blog/list.html',RequestContext(request,{'list':list}))
def add(request):
    if request.method=='POST':
        form = AddForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return HttpResponseRedirect(reverse('blog_list'))
    return render_to_response('blog/add.html',RequestContext(request,{'form':AddForm()}))
def update(request,id):
    blog = get_object_or_404(Blog,pk=int(id))
    if request.method == 'POST':
        form = AddForm(request.POST,instance=blog)
        if form.is_valid():
            blog = form.save()
            return HttpResponseRedirect(reverse("blog_list"))
    return render_to_response('blog/add.html',RequestContext(request,{'form':AddForm(instance=blog)}))
def delete(request,id):
    blog = get_object_or_404(Blog,pk=int(id))
    blog.delete()
    return HttpResponseRedirect(reverse('blog_list'))




