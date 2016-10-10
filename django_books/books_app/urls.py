from django.conf.urls import url
from .views import HomeView, ResultView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^result/$', ResultView.as_view(), name='result'),
]
