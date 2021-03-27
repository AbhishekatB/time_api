from django.shortcuts import render
from bs4 import BeautifulSoup
import time, urllib.request, requests


from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


@permission_classes([AllowAny, ])
class GetNewsletter(APIView):

    def get(self, request):
        url = 'https://time.com/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        context = []
        for i in soup.find('section', class_='homepage-module latest').ol.find_all('a'):
            dic = {}
            dic['title'] = i.text
            dic['link'] = url+i['href']
            context.append(dic)
        return Response(context)

