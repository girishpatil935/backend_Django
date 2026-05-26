from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Skill , UserProfile
from .forms import SkillForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SkillSerializer
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from rest_framework import filters

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticated, IsOwner]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterAPIView(
    generics.CreateAPIView
):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer

class SkillViewSet(viewsets.ModelViewSet):

    queryset = Skill.objects.all()

    serializer_class = SkillSerializer

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SkillListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = Skill.objects.all()

        search = self.request.query_params.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset
    
class SkillDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Skill.objects.all()

    serializer_class = SkillSerializer

    lookup_field = 'id'

@api_view(['GET', 'POST'])
def skills_api(request):

    if request.method == 'GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SkillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def skill_detail_api(request, id):

    skill = Skill.objects.get(id=id)

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SkillSerializer(skill, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    if request.method == 'DELETE':
        skill.delete()
        return Response({"message": "Skill deleted successfully"})


def home(request):
    return render(request, 'users/home.html')

def skills_list(request):
   skills = Skill.objects.all()

   form = SkillForm()

   if request.method == "POST":

        form = SkillForm(request.POST)

        if form.is_valid():

           form.save()

           return redirect("skills")

   return render(request, 'users/skills.html', {
        'skills': skills,
        'form': form
    })
def delete_skill(request, id):
    skill = Skill.objects.get(id=id)
    skill.delete()
    return redirect("skills")
def edit_skill(request, id):

    skill = Skill.objects.get(id=id)

    if request.method == "POST":
        new_name = request.POST.get("skill")

        if new_name:
            skill.name = new_name
            skill.save()

        return redirect("skills")

    return render(request, 'edit_skill.html', {
        'skill': skill
    })


def user_skills(request):

    user = UserProfile.objects.get(name="Girish")

    skills = user.skills.all()

    return render(request, 'users/user_skills.html', {
        'user': user,
        'skills': skills
    })
def search_skills(request):
    query = request.GET.get("q")

    if query:
        skills = Skill.objects.filter(name__icontains=query)
    else:
        skills = Skill.objects.all()

    return render(request, "users/search_skills.html", {
        "skills": skills,
        "query": query
    })
