from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactForm
from .serializer import ContactFormSerializer

class ContactFormView(APIView):
    def get(self, request):
        contacts = ContactForm.objects.all()
        serializer = ContactFormSerializer(contacts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactFormDetails(APIView):
    def get_object(self, id):
        try:
            return ContactForm.objects.get(id=id)
        except ContactForm.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        contact = self.get_object(id)
        serializer = ContactFormSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        contact = self.get_object(id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
