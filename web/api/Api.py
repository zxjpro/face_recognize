from . import bp
from flask import request
from face.FaceFit import  FaceFit
from face.FaceFit import known_people_dir
from face.FaceFit import tmp_people_dir
import random
import json
import os

face_fit = FaceFit()

# 一定要上传jpg格式的图片,质量高，文件小
@bp.route("/upload_source/<userTag>" , methods = ['POST'])
def upload_source(userTag):
    print("上传一张数据源图片 " + userTag)

    file = known_people_dir + userTag + ".jpg"

    with open(file,'xb') as f:
        f.write(request.data)

    face_fit.fit(file , userTag)

    return "SUCCESS"


@bp.route("/recognition" , methods = ['POST'])
def recognition():
    print("识别一张图片")
    file = tmp_people_dir + str(random.randrange(1,99999)) + ".jpg"
    with open(file , "xb") as f:
        f.write(request.data)

    res = face_fit.predict(file)
    os.remove(file)
    js = json.dumps(res)
    print("识别结果:" + js)
    return js


    with open(file,'xb') as f:
        f.write(request.data)

    face_fit.fit(file , userTag)

    return "SUCCESS"