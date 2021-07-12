##from PIL import Image
##import requests
##from io import BytesIO
##url="http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm"
##response=requests.get(url)
##img=Image.open(BytesIO(response.content))
##img.save('img1.jpg')

#link = "http://sonidos-primitivos1.blogspot.com/"
#f = requests.get(link)
#print(f.text)

import io
import requests
from PIL import Image
r = requests.get('https://images.freeimages.com/images/large-previews/0f8/bench-in-paris-1423180.jpg', stream=True)
aux_im = Image.open(io.BytesIO(r.content))
aux_im.save('banquito.jpg')