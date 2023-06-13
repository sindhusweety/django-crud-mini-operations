from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Continents, Country, State
from .serializers import ContinentSerializer, CountrySerializer, StateSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

class ContinentList(APIView):
    """
    List all continents or create a new snippet
    """
    def get(self, request, format = None):
        continents = Continents.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContinentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContinentDetail(APIView):
    """
    Retrieve, update or delete a continent instance.
    """
    def get_object(self, pk):
        try:
            return Continents.objects.get(pk=pk)
        except Continents.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        continent = self.get_object(pk)
        serializer = ContinentSerializer(continent)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        continent = self.get_object(pk)
        serializer = ContinentSerializer(continent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        continent = self.get_object(pk)
        continent.delete()
        return Response({"result":"successfully deleted"})

class CountryList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CountryDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StateList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StateDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

