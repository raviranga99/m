from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView,ListView,DetailView

class Aboutview(TemplateView):
    template_name="r.html"

class listv(ListView):
    model=Post
    template_name="r.html"

class detailv(DetailView):
    model=Post
    def get_context_data(self, **kwargs):
        context=super(detailv,self).get_context_data(**kwargs)
	r="hello    ravi"
        context['now'] =r 
        return context
    template_name="blog/list.html"

"""def temp(request):
    p=Post.objects.all()
    context={
        "p1":p
    }
    return render(request,"blog/list.html",context)
"""
