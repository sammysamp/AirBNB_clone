#!/usr/bin/python3i
'''Define class FileStorage'''
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
Classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "Amenity": Amenity, "Place": Place, "City": City, "Review": Review}


class FileStorage:
    '''Class FileStorage'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns _objects dictionary\
                at the beggining
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''add obj object to __objects dict'''
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        jsondict = {}
        # print("This is the dictionary __objects in method save")
        # print(self.__objects)
        # expand object (self) to dict
        for key in self.__objects:
            jsondict[key] = self.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(jsondict, f)

    def reload(self):
        try:
            jsondict = {}
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                jn = json.load(f)
                # print("jn IS CREATED IN THE RELOAD METHOD")
                # print(type(jn))
                # print(jn)
                for key in jn:
                    b = jn[key]["__class__"]
                    self.__objects[key] = Classes[b](**jn[key])
                # print(type(self.__objects))
                # print(self.__objects)

        except Exception as f:
            # print(f)
            pass
