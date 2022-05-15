import json
import math

from django.shortcuts import render
from django.views import generic
import requests
from bs4 import BeautifulSoup
from pyproj import Proj, transform
from haversine import haversine
from .models import Category, Store


# Create your views here.
def index(reqest):
    home = '서울특별시 광진구 능동로 209 세종대학교'
    res = requests.get(
        'https://www.juso.go.kr/addrlink/addrLinkApi.do?confmKey=devU01TX0FVVEgyMDIyMDUxNDE5MzQyMDExMjU2OTQ=&currentPage=1&countPerPage=1&resultType=json&keyword=' + home)
    soup = BeautifulSoup(res.text, 'html.parser')
    soup = json.loads(str(soup))
    juso = soup["results"]['juso'][0]
    res = requests.get(
        'https://www.juso.go.kr/addrlink/addrCoordApi.do?' + 'confmKey=devU01TX0FVVEgyMDIyMDUxNDE5MjQ1MzExMjU2OTM=&resultType=json&admCd=' +
        juso['admCd'] + '&rnMgtSn=' + juso['rnMgtSn'] + '&udrtYn=' + juso['udrtYn'] + '&buldMnnm=' + juso[
            'buldMnnm'] + '&buldSlno=' + juso['buldSlno']
    )
    soup = BeautifulSoup(res.text, 'html.parser')
    soup = json.loads(str(soup))
    juso = soup["results"]['juso'][0]
    # print(juso)
    X = float(juso['entX'])
    Y = float(juso['entY'])
    proj_grs80 = Proj('epsg:5179')
    proj_wgs84 = Proj('epsg:4326')
    home = transform(proj_grs80, proj_wgs84, X, Y)

    store = Store.objects.order_by("name")[:8]
    for s in store:
        x, y = s.to_x_y(s.address)
        s.x, s.y = transform(proj_grs80, proj_wgs84, x, y)
        s.distance_m = haversine(home, (s.x, s.y), unit='m')
        s.distance_km = haversine(home, (s.x, s.y), unit='km')

    context = {
        "store": store
    }

    return render(reqest, 'index.html', context=context)


class StoreDetailView(generic.DetailView):
    model = Store

# def single(reqest):
#     context = {
#
#     }
#
#     return render(reqest, 'store_detail.html', context=context)