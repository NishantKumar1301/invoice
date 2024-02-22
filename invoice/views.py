from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from PIL import Image
import google.generativeai as genai
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from django.middleware.csrf import get_token
import os
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@api_view(['POST'])
@method_decorator(csrf_exempt, name='dispatch')
def upload_question_and_image(request):
    if request.method == 'POST':
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Get the uploaded image
            uploaded_image = serializer.instance.image

            # Get the question
            question = request.data.get('question')

            # Process the uploaded image and question
            response = process_image_and_question(uploaded_image, question)

            # Get CSRF token
            csrf_token = get_token(request)

            # Return the response with CSRF token
            return Response({"response": response, "csrf_token": csrf_token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def process_image_and_question(image, question):
    # Process the image and question here using your preferred method
    # For example, you can use Google's generative AI model
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-pro-vision')
    input_prompt = f"""
                   {question}
                   """
    response = model.generate_content([input_prompt, image, ""])

    # Return the response text
    return response.text
