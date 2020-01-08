from django.conf.urls import url
from tutorial import views 

app_name = 'tutorial'
urlpatterns = [ 
  # The home view ('/tutorial/') 
  url(r'^$', views.home, name='home'), 
  # Explicit home ('/tutorial/home/') 
  url(r'^home/$', views.home, name='home'), 
  # Redirect to get token ('/tutorial/gettoken/')
  url(r'^gettoken/$', views.gettoken, name='gettoken'),
  # Mail view ('/tutorial/mail/')
  url(r'^mail/$', views.mail, name='mail'),
  # Events view ('/tutorial/events/')
  url(r'^events/$', views.events, name='events'),
  # Contacts view ('/tutorial/contacts/')
  url(r'^contacts/$', views.contacts, name='contacts'),
]