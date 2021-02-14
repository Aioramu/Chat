from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.utils.safestring import mark_safe
import json
from uuid import uuid4
from .models import Chat,Message
# Create your views here.
User = get_user_model()

@login_required
def search(request):

    if request.method != 'POST':
        form=SearchForm()
    else:
        form=SearchForm(data=request.POST)
        try:
            form=form.data.get("search")
            user=User.objects.get(username__iexact=form)
            chats=Chat.objects.all()
            for chat in chats:
                if str(chat.user1)==str(request.user) or str(chat.user2)==str(request.user):
                    if str(chat.user1)==str(user) or str(chat.user2)==str(user):
                        token=chat.token

                        form=SearchForm()
                        return render(request, "search.html",{'form':form,'token':token,'user':user})
            token = uuid4()
            chats.create(token=token,user1=str(request.user),user2=user)
            #room(request,user)
            form=SearchForm()
            return render(request, "search.html",{'form':form,'token':token,'user':user})
            #return render(request,"chat.html",{'room_name':str(user)})
        except:
            return HttpResponse("User Not Found")
    form=SearchForm()
    return render(request, "search.html",{'form':form,'user':' '})

def index(request):
    return render(request, 'index.html')

@login_required
def room(request, room_name):
    chats=Chat.objects.all()
    for chat in chats:
        if str(chat.user1)==str(request.user) or str(chat.user2)==str(request.user):
            return render(request, 'chat.html', {
                'room_name': room_name
            })
    return render(request, "search.html",{'form':form,'token':token,'user':user})
