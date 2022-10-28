from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class MainView(APIView):
    """The view for the only API endpoint that returns a JSON response containing an object."""

    def get(self, request):
        response = Response(
            { 
                "slackUsername": "michael_ikoko", 
                "backend": True, 
                "age": 19, 
                "bio": "I am Michael Ikoko. I am a student and I am currently learing Backend web development." 
            }
        )
        response["Access-Control-Allow-Origin"] = "*"
        return response
