from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from app.views import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='News API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^$', schema_view, name='swagger'),
    path('add-news/', scraper, name='add-news'),
    url(r'^news-retrieve/(?P<slug>[-\w]+)/$', NewsRetrieve.as_view(), name='news-retrieve'),
    path('news-list/', NewsList.as_view(), name='news-list'),
    path('news-update/<int:pk>', NewsUpdate.as_view(), name='news-update'),
    path('news-delete/<int:pk>', NewsDelete.as_view(), name='news-delete'),
]
