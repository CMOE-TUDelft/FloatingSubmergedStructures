from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .rag import answer_question
from .utils import send_message_to_mattermost
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def query_view(request):
    question = request.data.get('question')
    # Call your answer_question function here
    answer = answer_question(question)
    return Response({"answer": answer})

@csrf_exempt
def mattermost_webhook(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    try:
        data = json.loads(request.body)
        # Extract message text and channel info from Mattermost event payload
        user_id = data.get("user_id")
        channel_id = data.get("channel_id")
        text = data.get("text")
        if not text or not channel_id:
            return HttpResponseBadRequest("Missing text or channel")

        # Generate answer via your RAG pipeline
        answer = answer_question(text)

        # Send answer back to Mattermost channel via REST API
        send_message_to_mattermost(channel_id, answer)

        # Respond quickly to webhook call
        return JsonResponse({"status": "ok"})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")