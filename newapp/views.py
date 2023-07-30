from django.shortcuts import render,redirect
from newapp.models import DIRECTORS
from newapp.forms import DIRECTORSFORM

# Create your views here.
def artist(request):
	dir=DIRECTORS.objects.all()
	dirinfo={'dir': dir}
	return render(request,'newapp/abc.html',context=dirinfo)


def create(request):
	form = DIRECTORSFORM()
	if request.method == 'POST':
		form = DIRECTORSFORM(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/newapp/directors')
	return render(request,'newapp/create.html',{'form':form})


def deleteview(request,id):
	dir=DIRECTORS.objects.get(id=id)
	dir.delete()
	return redirect('/newapp/directors')









