from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),

    path("post/project", views.post_project, name="post_project"),
    path('search/', views.project_search, name = "project_search"),
    path('profile/',views.profile, name = "profile"),
    path('project/rate/<int:id>', views.rate_project, name ="rate_project"),
    path('project/votes/<int:id>', views.add_voters, name ="add_voters"),
    path('profile/edit/', views.edit_profile,name= 'edit_profile'),
    # path('api/projects/', views.ProjectList.as_view()),
    # path('api/profiles/', views.ProfileList.as_view()),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
