#!/usr/bin/python3
"""Air bnb proyect!!!"""
import models
import uuid
from datetime import datetime


# Date format
date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        self.id = str(uuid.uuid4())
        if kwargs is not None and kwargs != {}:
            for key in kwargs.keys():
                if key != '__class__':
                    setattr(self, key, kwargs[key])
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], date)
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], date)
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                          self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Instance to_dictionary"""
        dictionary = self.__dict__.copy()
        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(date)
        if "updated_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(date)
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
