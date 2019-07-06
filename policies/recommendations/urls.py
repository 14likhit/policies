from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PoliciesView

urlpatterns = {
    url(r'^policies/$', PoliciesView, name="get_policies")
}

urlpatterns = format_suffix_patterns(urlpatterns)
