#from django.conf.urls import url
from django.urls import path,re_path
from django.contrib import admin
from gms.views import log_in,log_out,authenticated,course,addexam,setcriteria,update_exam
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',log_in,name='log_in'),
    path('',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    path('authenticated/',authenticated,name='authenticated'),
    re_path(r'^authenticated/(?P<course_no>[0-9]+)/$',course,name='course'),
    re_path(r'^authenticated/(?P<course_no>[0-9]+)/addexam/$',addexam,name='addexam'),
    re_path(r'^authenticated/(?P<course_no>[0-9]+)/setcriteria/$',setcriteria,name='setcriteria'),
    re_path(r'^authenticated/(?P<course_no>[0-9]+)/(?P<exam_no>[0-9]+)/$',update_exam,name='update_exam'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
