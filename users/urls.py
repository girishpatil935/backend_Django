from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
path(
    'api/register/',
    views.RegisterAPIView.as_view(),
),
path(
    'api/token/',
    TokenObtainPairView.as_view(),
    name='token_obtain_pair',
),
path(
    'api/token/refresh/',
    TokenRefreshView.as_view(),
    name='token_refresh',
),
] + router.urls