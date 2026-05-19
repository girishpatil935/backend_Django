from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    'api/viewset/skills',
    views.SkillViewSet,
    basename='skill-viewset'
)

urlpatterns = [
    path('',views.home),
    path('skills/',views.skills_list,name="skills"),
    path('delete/<int:id>/', views.delete_skill, name="delete_skill"),
    path('edit/<int:id>/', views.edit_skill, name="edit_skill"),
    path('user-skills/',views.user_skills),
    path('search/',views.search_skills,name="search_skills"),
    path('api/skills/', views.skills_api, name='skills_api'),
    path('api/skills/<int:id>/', views.skill_detail_api, name='skill_detail_api'),
    path(
    'api/generic/skills/',
    views.SkillListCreateAPIView.as_view(),
),

path(
    'api/generic/skills/<int:id>/',
    views.SkillDetailAPIView.as_view(),
),
] + router.urls