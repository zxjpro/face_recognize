from face.FaceFit import FaceFit
import time

#faceFit = FaceFit()

# faceFit.fitDir("/home/zxj/tmp/face/known_people/")
#
# r = faceFit.predict("/home/zxj/tmp/face/unknown_people/901.jpg")
# print(r)
#
# s = time.time()
# r2 = faceFit.predict("/home/zxj/tmp/face/unknown_people/902.jpg")
# print(r2)
# e = time.time()
# print("use time:" + str(e - s))


from web import create_app

app = create_app()

app.run('0.0.0.0' , 8790)