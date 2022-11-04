from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
import openai
import environ
import re

# Create your views here.

env = environ.Env()

def generate_prompt_result(question):
    """Generates the OpenAI prompt to determine the result from a question."""
    return f"""Perform the following word mathematical operations:

Question: Can you please add the following numbers together -13 and 25.
Output: 12

Question: What is the product of 5 and -12.
Output: -60

Question: Please subtract the numbers 5 and 12.
Output: -7

Question: What is the difference between 20 and 35?
Output: -15

Question: {question}"""


def generate_prompt_operation(question):
    """Generates the OpenAI prompt to determine the operation type from a question."""
    return f"""Tell me the mathematical operation performed:

Question: Can you please add the following numbers together - 13 and 25.
Output: addition

Question: What is the product of 5 and -12.
Output: multiplication

Question: Please subtract the numbers 5 and 12
Output: subtraction

Question: What is the difference between 20 and 35?
Output: subtraction

Question: Please calculate the sum of 15 and -8?
Output: addition

Question: If you multiply 2 and 6 and then add 8 to the result what's the answer
Output: addition

Question: {question}.
"""


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
        return response 

    def post(self, request):
        data = request.data
        operation_type = data["operation_type"]
        if operation_type.lower() in ["add", "addition", "+"]:
            x = data["x"]
            y = data["y"]
            result = x + y
        elif operation_type.lower() in ["sub", "subtraction", "-"]:
            x = data["x"]
            y = data["y"]
            result = x - y
        elif operation_type.lower() in ["mul", "multiplication", "*"]:
            x = data["x"]
            y = data["y"]
            result = x * y
        else:
            openai.api_key = env("OPENAI_API_KEY")

            result_response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt_result(operation_type),
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0
            )

            operation_response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt_operation(operation_type),
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0
            )

            result_output = result_response["choices"][0]["text"]
            result_pattern = re.compile(r"(-?\d+)$")
            result = result_pattern.search(result_output).group()

            operation_output = operation_response["choices"][0]["text"]
            operation_pattern = re.compile(r"(addition|Addition|subtraction|Subtraction|multiplication|Multiplication)")
            operation = operation_pattern.search(operation_output).group()

            return Response(
                {
                    "slackUsername": "michael_ikoko",
                    "result": int(result),
                    "operation_type": operation
                }
            )
        
        return Response(
            {
                "slackUsername": "michael_ikoko",
                "result": int(result),
                "operation_type": operation_type
            }
        )
