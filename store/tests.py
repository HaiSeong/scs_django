import json

import requests
from bs4 import BeautifulSoup
from django.test import TestCase

# Create your tests here.

res = requests.get(
    'https://www.juso.go.kr/addrlink/addrLinkApi.do?confmKey=devU01TX0FVVEgyMDIyMDUxNDE5MzQyMDExMjU2OTQ=&currentPage=1&countPerPage=1&resultType=json&keyword=' + '서울특별시 광진구 광나루로40길 34, 1층 (구의동)')
soup = BeautifulSoup(res.text, 'html.parser')
soup = json.loads(str(soup))
juso = soup["results"]['juso'][0]
print(juso)

res = requests.get(
    'https://www.juso.go.kr/addrlink/addrCoordApi.do?'+'confmKey=devU01TX0FVVEgyMDIyMDUxNDE5MjQ1MzExMjU2OTM=&resultType=json&admCd='+juso['admCd']+'&rnMgtSn='+juso['rnMgtSn']+'&udrtYn='+juso['udrtYn']+'&buldMnnm='+juso['buldMnnm']+'&buldSlno='+juso['buldSlno']
)
soup = BeautifulSoup(res.text, 'html.parser')
soup = json.loads(str(soup))
juso = soup["results"]['juso'][0]
print(juso)
X = float(juso['entX'])
Y = float(juso['entY'])

print(X,Y)


# confmKey	String	Y	-	신청시 발급받은 승인키
# admCd	    String	Y	-	행정구역코드
# rnMgtSn	String	Y	-	도로명코드
# udrtYn	String	Y	-	지하여부
# buldMnnm	Number	Y	-	건물본번
# buldSlno	Number	Y	-	건물부번