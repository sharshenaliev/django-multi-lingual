from ..serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
import requests


class OurTeam(ListAPIView):
    serializer_class = OurTeamSerializers
    queryset = OurTeam.objects.all()


class Feedback(CreateAPIView):

    def post(self, request, *args, **kwargs):
        token = '5503825161:AAHSBtZDP_JIkzXLjb6wwT3r6EuXJZu3LK4'
        chat_id = "826921885"

        message = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'phone': request.data.get('phone'),
            'email': request.data.get('email'),
            'group': request.data.get('group'),
            'question': request.data.get('question')
        }

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)
        return Response("Feedback was sent")