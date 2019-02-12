import face_recognition
import os
import numpy as np

known_people_dir = "/data/face/known/"
tmp_people_dir = "/data/face/tmp/"



class FaceFit():
    __fit__ = False
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls , '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if(self.__fit__ == False):
            self.__fit__ = True
            print("初始化")
            mkdir(known_people_dir)
            mkdir(tmp_people_dir)

            self.fitDir(known_people_dir)

    known_faces_ = []
    known_faces_name_ = []

    #训练目录
    def fitDir(self,path):
        fileList = os.listdir(path)
        print("加载训练文件夹,文件长度:" + str(len(fileList)))
        for index,file in enumerate(fileList):
            print("["+str(index + 1)+"] " + file)
            face_enc = self.load_img_enc(path + file)
            name = file[:file.find(".")]
            self.known_faces_.append(face_enc)
            self.known_faces_name_.append(name)
        print("训练完毕")

    #训练单个文件
    def fit(self,file,label):
        print("训练单个文件: " + file + " " + label)
        face_enc = self.load_img_enc(file)
        self.known_faces_.append(face_enc)
        self.known_faces_name_.append(label)


    def predict(self,path):
        face_enc = self.load_img_enc(path)
        results = np.array(face_recognition.compare_faces(self.known_faces_,face_enc,tolerance=0.5))
        if results.size == 0:
            return None
        else:
            dis = face_recognition.face_distance(self.known_faces_,face_enc)
            sort_index_dis = dis.argsort().argsort()

            #打印结果
            # label = np.array(self.known_faces_name_)[results]
            # #打印距离
            # distance = dis[results]
            #打印根据距离查询
            label = np.array(self.known_faces_name_)[sort_index_dis.argmin()]
            distance = dis[sort_index_dis.argmin()]
            #return {"label" : label , "distance" : distance}
            return {"label" : label , "distance" : distance}


    def load_img_enc(self,path):
        face_np = face_recognition.load_image_file(path)
        face_enc = face_recognition.face_encodings(face_np)[0]
        return face_enc


def mkdir(dir):
    try:
        os.makedirs(dir)
    except IOError:
        pass


