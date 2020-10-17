import requests
from bs4 import BeautifulSoup as bs
from PIL import Image,ImageFile
from io import BytesIO as b
import random
import urllib.request as re
data= input('what are you looking for ? ')
data= data.split(' ')
data='+'.join(data)
n_images=input('how many images do you want ? ')
bing_image='https://bing.com/images/search?q=' + data  + '&count=' + n_images
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
headers = {"user-agent": USER_AGENT}
response=requests.get(bing_image,headers=headers)
html=response.text
soup=bs(html,'html.parser')
fortitles=soup.findAll('a',{"class":"thumb"})
results=soup.findAll('a',class_='iusc')
ImageFile.LOAD_TRUNCATED_IMAGES = True
print('start searching ...')
a=0
for i in results:
	if a<int(n_images):
		try:
			url = str(eval(i['m'])['murl'])
			re.urlretrieve(url, './images/'+f'{a+1}.jpg')
			a=a+1
		except:
			pass
	else:
		break

print(f'we found {a} images')



