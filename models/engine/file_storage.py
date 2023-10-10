#!/usr/bin/python3
"""Defines FileStorage class"""
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
        objname = f"{obj.__class__.__name__}.{obj.id"}
        FileStorage.__objects[objname] = obj

    def save(self):
        """serializes __objects ti json file"""
        objdict = FileStorage.__objects
        f_objdict = {obj: objdict[obj]. to_dict() for obj in objdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(f_objdict, f)

    def reload(self):
        """deserialize json file to __objects if it exists
        Raise exception: none
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for val in objdict.values():
                    cls_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(cls_name)(**val))
        except FileNotFoundError:
            return
