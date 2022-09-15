import os
import random
from flask import request,jsonify
import requests
from app import app
from utils import GifUtils

@app.route('/getgif',methods=["POST"])
def get_GIF():
    img1 = request.json.get("img1")
    img2 = request.json.get("img2")
    img3 = request.json.get("img3")

    img_url_list = [img1,img2,img3]

    img_path = "static/img/"
    img_dic = {}
    #整理类别
    for fileName in os.listdir(img_path):
        typeName = fileName.split("-")[0]
        img_dic[typeName] = img_dic.get(typeName,[])
        img_dic[typeName].append(img_path+fileName)

    #被选中的贴纸
    choiced_type = list(img_dic.keys())[random.randint(0, len(img_dic.keys())-1)]
    choiced_img = random.sample(img_dic.get(choiced_type),3)

    #保存图片到本地
    webImg_path = "static/webimg/"
    web_img = []
    if not os.path.exists(webImg_path):
        os.makedirs(webImg_path)
    for url in img_url_list:
        response = requests.get(url)
        web_img.append(webImg_path+str(img_url_list.index(url))+".jpg")
        with open(webImg_path+str(img_url_list.index(url))+".jpg","wb") as fp:
            fp.write(response.content)

    #转gif
    mergeImg_path = "static/mergeImg/"
    gif_name = 'res.gif'
    duration = 0.5
    if not os.path.exists(mergeImg_path):
        os.makedirs(mergeImg_path)
    GifUtils.preProcess(choiced_img)
    GifUtils.merge(choiced_img, web_img, mergeImg_path)

    mergeImg_list = [mergeImg_path + img for img in os.listdir(mergeImg_path)]
    GifUtils.create_gif(mergeImg_list , gif_name, duration)

    return jsonify({
        "code":200,
        "msg":"SUCCESS"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=18088)
