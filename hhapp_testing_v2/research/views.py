from rest_framework import generics, viewsets
from rest_framework.decorators import action

# возможно потом можно будет убрать.
from rest_framework.response import Response
from rest_framework.views import APIView
# ----
from django.shortcuts import render, HttpResponse
from .models import Category, ResearchRef
from .serializers import ResearchRefSerializer

#Create your views here.
class ResearchRefViewSet(viewsets.ModelViewSet):
    queryset = ResearchRef.objects.all()
    serializer_class = ResearchRefSerializer

    @action(methods=['get'], detail=False)
    def category(self, request):
        category = Category.objects.all()
        return Response({'category': [c.name for c in category]})


# class ResearchRefAPIList(generics.ListCreateAPIView):
#     queryset = ResearchRef.objects.all()
#     serializer_class = ResearchRefSerializer


# class ResearchRefAPIUpdate(generics.UpdateAPIView):
#     queryset = ResearchRef.objects.all()
#     serializer_class = ResearchRefSerializer


# class ResearchRefAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ResearchRef.objects.all()
#     serializer_class = ResearchRefSerializer



def home(request):
    #return HttpResponse('hello world')
    return render(request, 'index.html', context={})
