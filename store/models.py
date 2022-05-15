import json

from django.db import models
import requests
from bs4 import BeautifulSoup

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    img_url = models.URLField()
    category = models.ManyToManyField(Category)
    x = models.FloatField()
    y = models.FloatField()
    distance_m = models.FloatField()
    distance_km = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store", args=[str(self.id)])

    def to_x_y(self, address):
        res = requests.get(
            'https://www.juso.go.kr/addrlink/addrLinkApi.do?confmKey=devU01TX0FVVEgyMDIyMDUxNDE5MzQyMDExMjU2OTQ=&currentPage=1&countPerPage=1&resultType=json&keyword=' + address)
        soup = BeautifulSoup(res.text, 'html.parser')
        soup = json.loads(str(soup))
        juso = soup["results"]['juso'][0]
        # print(juso)

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

        return (X, Y)
