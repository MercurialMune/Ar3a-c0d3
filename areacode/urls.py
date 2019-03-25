from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from area import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('area.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^search-biz/$', views.search_business, name='search-biz'),
    url(r'^search-area/$', views.search_locations, name='search-area'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
