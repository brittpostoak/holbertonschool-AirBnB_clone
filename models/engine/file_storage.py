#!/usr/bin/python3
"""Defines FileStorage class"""
import datetime
import json
from models.base_model import BaseModel


class FileStorage:
    """Represents storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key<obj class name>.id """
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """serializes __objects ti json file"""
        with open(FileStorage.__file_path, "w") as f:
            data = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """deserialize json file to __objects if it exists
        Raise exception: none
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            objdict = json.load(f)
            objdict = {key: self.classes()[v["__class__"]](**value)
                    for key, value in objdict.items()}
            FileStorage.__objects = objdict
