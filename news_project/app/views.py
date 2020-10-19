from django.shortcuts import render
from .models import News
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .scrapper import news_scrap
from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import status
from .serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


@api_view(['POST', 'GET'])
def scraper(request):
    """get the json data and convert into python dictionary which pass to news_scrap function after
    correcting url for further processing
    allowed methods : GET, POST
    """
    data = {}
    raw_data = JSONParser().parse(request)
    for key, value in raw_data.items():
        if str(value['link']).startswith('https://') or str(value['link']).startswith('http://'):
            data[key] = value['link']
        else:
            data[key] = 'https://' + str(value['link'])
    news_scrap(data)
    content = {"scraping data": "please go to list view"}
    return Response(content, status=status.HTTP_200_OK)


class NewsRetrieve(APIView):

    """Return News objects present in database base on search keyword after Authentication
    allowed methods : GET
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        key = kwargs['slug']
        news = News.objects.filter(Q(Title__icontains=key) | Q(Details__icontains=key)).order_by('Id')
        serialize_data = NewsSerializer(news, many=True).data
        return Response(serialize_data)


class NewsList(generics.ListAPIView):

    """Return the list of all News objects present in database after Authentication
    allowed methods : GET
    """

    permission_classes = (IsAuthenticated,)
    queryset = News.objects.all().order_by("Id")
    serializer_class = NewsSerializer


class NewsDelete(generics.DestroyAPIView):
    """ delete news object base on id after Authentication
    allowed methods : DELETE
    """

    permission_classes = (IsAuthenticated,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsUpdate(generics.UpdateAPIView):
    """ Update news object base on id after Authentication
    allowed methods : PUT and PATCH
    """

    permission_classes = (IsAuthenticated,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer
