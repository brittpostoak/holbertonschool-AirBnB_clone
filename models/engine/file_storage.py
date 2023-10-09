#!/usr/bin/python3
"""Defines FileStorage class"""
import datetime
import json
import os


class FileStorage:
    """Class that stores and retrieves data"""
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
        opendict = FileStorage.__objects
        objdict = {obj: opendict[obj].to_dict() for obj in opendict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserialize json file to __objects
        Raise exception: none
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
