from django.conf.urls import patterns, url

from puns import views

urlpatterns = patterns('puns.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<pun_id>\d+)/vote/$', 'vote', name='vote'),
    url(r'^(?P<pun_id>\d+)/delete/$', 'delete', name='delete'),
    url(r'^create/$', 'create', name='create')
)
