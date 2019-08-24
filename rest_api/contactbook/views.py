# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Person, Detail
from rest_framework.views import APIView
from rest_framework.response import Response
import io
from .serializers import PersonSerializers, DetailSerializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
# Create your views here.
class ContactBookList(APIView):
    """
    List of all Persons Details , or create a new Person details
    """
    def post(self, request, format=None):
        p_data = request.data
        obj = PersonSerializers(data=p_data)
        if obj.is_valid():
            obj.save()
            # person = obj.save()
            # n_data = DetailSerializers(data=p_data)
            # if n_data.is_valid():
            #     n_data.save(name=person)
            #msg = {'msg' : "Contact created"}
            return Response(obj.data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(obj.errors, status=400)
                
    def get(self, request, format=None):
        qs = Person.objects.all()
        serializer = PersonSerializers(qs, many=True)
        return Response(serializer.data)  

class ContactBookDetail(APIView):
    """
    Retrieve, Update and delete Person Instance
    """
    def get_object(self, id=None):
        try:
            return Person.objects.get(pk=id)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        Person = self.get_object(id)
        serializer = PersonSerializers(Person)
        return Response(serializer.data)
    
    def put(self, request, id=None, format=None):
        Person = self.get_object(id)
        serializer = PersonSerializers(Person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Person = self.get_object(id)
        Person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
            

    