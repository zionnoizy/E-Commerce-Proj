import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import JsonResponse


from . import models
from . import forms
# Create your views here.

def index(request):
    return render(request, 'chat_app/waiting_room.html', {})


def chat(request, room_name):
    if request.method == 'POST':
        my_form = forms.Chat_form(request.POST)
        if my_form.is_valid():
            conversation = models.Chat_model(
                conversation=my_form.cleaned_data["conversation"]
            )
            conversation.save()
            my_form=forms.Chat_form()
    else:
        my_form=forms.Chat_form()
    conversation = models.Chat_model.objects.all()
    context = {
        "my_form":my_form,
        "conversation":conversation,
        'room_name': mark_safe(json.dumps(room_name)),
    }
    return render(request, "chat_app/chat_.html", context=context)


def rest_chat(request):
    if request.method == 'GET':
        conversation = models.Chat_model.objects.all()
        list_of_conversation = []
        for x in conversation:
            list_of_conversation+=[{
                "conversation":x.conversation,
                "id":x.id
            }]
        return JsonResponse({"conversation":list_of_conversation},safe=False)
    else:
        return HttpResponse("Invalid HTTP Method")
