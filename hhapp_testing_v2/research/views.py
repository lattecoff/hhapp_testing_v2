from rest_framework import generics, viewsets
from rest_framework.decorators import action

# возможно потом можно будет убрать.
from rest_framework.response import Response
from rest_framework.views import APIView
# ----
from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages
from .models import Category, ResearchRef
from .serializers import ResearchRefSerializer

from .forms import ResearchRefForm, UserRegisterForm

#Create your views here.
class ResearchRefViewSet(viewsets.ModelViewSet):
    queryset = ResearchRef.objects.all()
    serializer_class = ResearchRefSerializer
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
    serialized_data = ResearchRef.objects.all()
    #serialized_data = ResearchRefSerializer
    return render(request, template_name='index.html', context={"serialized_data": serialized_data})


def create_research(request):
    if request.method == 'POST':
        form = ResearchRefForm(request.POST)
        if form.is_valid():
            research = form.save()
            return redirect(research)
    else:
        form = ResearchRefForm()

    return render(request, template_name='create_research.html', context={'form': form,})
    #return render(request, template_name='create_research.html', context={'message': "Hello world", })


def register(request):
    '''
    Представление которое отвечает за отображение формы Регстрации нового пользователя.
    :param request:
    :return: сообщение об успешной регистрации.
    :return: форму с ошибкой при регстрации.
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register is success')
            return redirect('login')
        else:
            messages.error(request, 'Register is fail')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')