from django.http import HttpResponse
from django.shortcuts import render,render_to_response,get_object_or_404,redirect
from .models import Mform
from .form import A
from django.template import RequestContext
from django.contrib import messages

def newpost(request):
    if request.method=="POST":
        form=A(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
    else:
        form=A()
    return render(request,"index1.html",{"form":form})
def update(request,id):
    #if request.method=="POST":
        instance = get_object_or_404(Mform, id=id)
        form=A(request.POST or None,instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully update")
    #else:
    #    form=A()
        return render(request,"index1.html",{"form":form})


def list(request):
    a=Mform.objects.all()
    context={"a":a,}
    return render(request,"indexlist.html",context)


def post_delete(request, id):
	#if not request.user.is_staff or not request.user.is_superuser:
		#raise Http404
	instance = get_object_or_404(Mform,id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("list")
