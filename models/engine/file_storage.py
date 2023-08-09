#!/usr/bin/python3
"""This defines the FileStorage class"""
import json
json os.path #checks if a file exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This represents instances to a JSON file and
        deserializes the JSON files to instances
    """

    # Private Class Attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """This sets in __objects the obj with key"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """This serializes __objects to the JSON file path"""
        srlzd = {key: obj.to_dict() for (key, obj) in self.__objects.items()}

        with open(self.__file_path, "w") as f:
            json.dump(srlzd, f)

    def reload(self):
        """This deseriaizes the JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                myFile = json.load(f)

                for key, value in myFile.items():
                    classname, obj_id = key.split('.')
                    self.__objects[key] = eval(classname)(**value)
