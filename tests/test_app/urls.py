from django.contrib import admin
from django.urls import re_path

urlpatterns = [
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    re_path(r"^admin/", admin.site.urls),
]
