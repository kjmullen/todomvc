from django.conf.urls import url

from api.views import list_create_todo, DetailUpdateDeleteTodo

urlpatterns = [
    url(r'^todos/$', list_create_todo, name="list_create_todo"),
    url(r"^todos/(?P<pk>\d+)/$", DetailUpdateDeleteTodo.as_view(),
        name="detail_update_delete_todo"),
]
