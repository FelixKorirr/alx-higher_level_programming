#!/usr/bin/python3
"""Define base superclass"""

import json
import csv


class Base:
    """Represent superclass"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON serialization of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON serialization of a list of objects to a file"""
        name = cls.__name__ + ".json"
        with open(name, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns deserialization of a JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_dict = cls(1, 1)
            else:
                new_dict = cls(1)
            new_dict.update(**dictionary)
            return new_dict

    @classmethod
    def load_from_file(cls):
        """Returns list of classes instantiated from file of JSON strings"""
        name = str(cls.__name__) + ".json"
        try:
            with open(name, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file"""
        name = cls.__name__ + ".csv"
        with open(name, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]
                else:
                    field = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, field=field)
                for o in list_objs:
                    writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated from a CSV file"""
        name = cls.__name__ + ".csv"
        try:
            with open(name, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]
                else:
                    field = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, field=field)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []