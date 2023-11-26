from django.shortcuts import  redirect
from django.shortcuts import redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

def home(request):
    return JsonResponse({"message": "Hello new User!"})


def get_room_info(request, room):
    username = request.GET.get('username') # henry
    room_details = Room.objects.get(name=room)
    return JsonResponse({
        'username': username,
        'room': room,
        'room_details': room_details.serialize()  # Здесь room_details должен быть сериализован в формат JSON
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    message.save()
    # return HttpResponse("Hi, Message Sent Successfully!!")

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room)
    return JsonResponse({"messages": list(messages.values())})