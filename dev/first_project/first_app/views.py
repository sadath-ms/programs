from django.shortcuts import render,get_object_or_404,HttpResponse
from first_app.models import NameModel
from first_app.forms import nameForm
from django.urls import reverse_lazy

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

"""def index(request):
    names=NameModel.objects.all()
    context={
        'names':names
    }
    return render(request,'index.html',context)
"""

class index(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return NameModel.objects.all()

"""
def details(request,id):
    detail=get_object_or_404(NameModel,id=id)
    return render(request,'details.html',{'detail':detail})
"""

class details(DetailView):
    model = NameModel
    template_name = 'details.html'


def formView(request):
    form=nameForm()

    if request.method == 'POST':

        form=nameForm(request.POST)

        if form.is_valid():
           data=NameModel(name=form.cleaned_data['name'],age=form.cleaned_data['age'],location=form.cleaned_data['location'])
           data.save()
           return HttpResponse('Data updated successfully....')




    return render(request,'forms_input.html',{'form':form})


class create(CreateView):
    model = NameModel
    fields = '__all__'
    template_name = 'forms_input.html'


class update(UpdateView):
    model = NameModel
    fields = '__all__'
    template_name = 'forms_input.html'



class delete(DeleteView):
    model = NameModel
    template_name = 'delete_form.html'
    success_url = reverse_lazy('first_project:index')


