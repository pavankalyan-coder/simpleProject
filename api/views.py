from django.http import JsonResponse
from .models import Message

def get_message(request):
    message = Message.objects.first()
    return JsonResponse({
        "message": message.text
    })