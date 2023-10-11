#!/usr/bin/python3
"""
Class: FileStorage
"""

from json import loads, dumps
from os.path import exists


class FileStorage():
    """ serializes / deserializes from a JSON file

        Attributes:
            __file_path (str): File path to JSON
            __objects (dict): Stores objects by class.id
    """
    __file_path = "file.json"  # string - File path to JSON
    __objects = {}  # dictionary - Stores objects by class.id

    def all(self):
        """ returns dictionary of all saved objects """
        return self.__objects

    def new(self, obj):
        """
        stores obj in __objects dictionary:
                key = "<obj class name>.id"
                value = obj.to_dict()

            Args:
                obj (:obj:`BaseModel`): Adds to __objects
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """ serializes __object to the JSON file """
        dict_of_dicts = {}
        for key, value in self.__objects.items():
            dict_of_dicts[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(dumps(dict_of_dicts))

    def reload(self):
        """ deserializes JSON file to __objects

        Note:
            if JSON file (__file_path) does not exist, nothing is done.
        """

        if exists(self.__file_path) is False:
            return

        with open(self.__file_path, 'r') as f:
            dicts = loads(f.read())

        from .known_objects import classes

        self.__objects = {}
        for id, dict in dicts.items():
            cls_name = id.split('.')[0]
            cls = classes[cls_name]
            self.__objects[id] = cls(**dict)
