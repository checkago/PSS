from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about-us/', views.about, name='about'),
    path('service/', views.services, name='services'),

    path('projects/', views.projects, name='projects'),
    path('projects/gos', views.gos, name='gos'),
    path('projects/infra', views.infra, name='infra'),
    path('projects/prom', views.prom, name='prom'),
    path('projects/jil', views.jil, name='jil'),
    path('projects/torg', views.torg, name='torg'),
    path('projects/admin', views.admin, name='admin'),

    path('news-list/', views.news_list, name='news_list'),
    path('news/<str:news_slug>/', views.news, name='news'),
    path('apply-from/', views.vacancies, name='vacancies'),
    path('contact/', views.contact, name='contact'),

]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += staticfiles_urlpatterns()
