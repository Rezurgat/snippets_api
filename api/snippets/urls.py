from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# urlpatterns = [
#     path('', views.api_root),
#
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
#
#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight', views.SnippetHighlighted.as_view(), name='snippet-highlight')
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)