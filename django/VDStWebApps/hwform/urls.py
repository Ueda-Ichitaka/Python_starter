from django.conf.urls import url

from . import views

app_name = 'hwform'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list/$', views.TicketListView.as_view(), name='ticket_list'),
    url(r'^ticket/upload.html$', views.ticket_upload, name='ticket_upload'),
    #url(r'^ticket/(?P<ticket_id>\d+)/detail.html$', views.ticket_detail, name='ticket_detail'),
    url(r'^ticket/(?P<pk>\d+)/detail.html$', views.DetailView.as_view(), name='ticket_detail'),
    url(r'^ticket/form_upload.html$', views.ticket_form_upload, name='ticket_form_upload'),
]