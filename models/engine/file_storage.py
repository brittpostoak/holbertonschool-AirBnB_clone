#!/usr/bin/python3
"""
Class: File Storage
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class: File Storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        All file storage
        """
        objects_dictionary = self.__objects.copy()
        return objects_dictionary

    def new(self, obj):
        """
        New file storage
        """
        class_dictionary = obj.to_dict()
        class_name = class_dictionary.get('__class__')
        key = f"{class_name}.{obj.id}"
        self.__objects.update([(key, obj)])

    def save(self):
        """
        Save file storage
        """
        new_dictionary = {}
        for key in self.__objects:
            python_obj = self.__objects.get(key)
            new_dictionary[key] = python_obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(new_dictionary, file)

    def reload(self):
        """
        Reload class
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                loaded = json.load(file)
                for key in loaded:
                    old_value = loaded.get(key)
                    class_name = old_value.get('__class__')
                    new_value = classes[class_name](**old_value)
                    loaded.update([(key, new_value)])
                self.__objects = loaded
        else:
            pass

    def destroy_this(self, key):
        """ removes a key value pair stored in __objects """
        if key in self.__objects:
            self.__objects.pop(key)
        else:
            return
