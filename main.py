import requests
import numpy as np
from PIL import Image
from io import BytesIO
import cv2
from tqdm import tqdm
url = 'https://gac-geo.googlecnapps.cn/maps/vt?lyrs=s%40817&hl=zh-CN&gl=CN&x={}&y={}&z=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',

}
x = 866845
y = 450194
u = 100
v = 100
canvas = np.zeros(((u) * 256, (v) * 256, 3), dtype=np.uint8)

for i in tqdm(range(u)):
    for j in tqdm(range(v)):

        response = requests.get(url.format(x+i,y+j))
        # print(response)
        with open("imgs/{}_{}.jpg".format(x+i,y+j),"wb") as file:
            file.write(response.content)
        img = Image.open(BytesIO(response.content))
        canvas[j*256:(j+1)*256,i*256:(i+1)*256] = img

        # cv2.imshow("1",canvas)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
Image.fromarray(canvas).save('all2.jpg')
cv2.waitKey(0)
cv2.destroyWindow()

