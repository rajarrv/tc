#this can become another package
# Create your models here.
import pymongo
from pymongo import MongoClient
import os


def mydb():
    client = MongoClient()
    return client['test_db']

class Model(object):
    #my_db = mydb()

    def insert(self,*args,**kwargs):
        self.my_db=mydb()
        self.my_db[self.model_name].ensure_index([(self.index_field, pymongo.ASCENDING)])
        self.my_db[self.model_name].save(kwargs) 


    def find(self,*args,**kwargs):
        self.my_db=mydb()
        for each in self.my_db[self.model_name].find(kwargs):
            return each
        return None
    
    def findall(self,*args,**kwargs):
        self.my_db=mydb()
        totlist=[]
        for each in self.my_db[self.model_name].find(kwargs):
            for each_sec in self.secure_field:
                each.pop(each_sec)
            totlist.append(each)
        return totlist

class User(Model):
    model_name='user_model'
    index_field='user_name'
    secure_field=['_id','pass_word']
    def __init__(self,*args,**kwargs):
        self.user_name=''
        self.pass_word=''
        self.city=''
        self.address=''
        self.education=''
    def encode(self,*args,**kwargs):
        self.user_name=kwargs['user_name']
        self.pass_word=kwargs['pass_word']
        self.city=kwargs.get('city')
        self.address=kwargs.get('address')
        self.education=kwargs.get('education')
        
class Showfiles(object):
    model_name='user_path'
    def __init__(self,*args,**kwargs):
        self.path=kwargs.get('path')
    def find(self,*args,**kwargs):
        self.path=kwargs['path']
        if os.path.exists(self.path):
            return os.listdir(self.path)
        else:
            return ['path not exists']

class Services(object):
    model_name='services_status'
    def mongo_status(selfself,*args,**kwargs):
        import subprocess
        try:
            p = subprocess.Popen("service mongod status", stdout=subprocess.PIPE, shell=True)
            return p.communicate()
        except:
            return 'service not responding'