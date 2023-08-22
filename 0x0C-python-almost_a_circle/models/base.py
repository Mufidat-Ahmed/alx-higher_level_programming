#!/usr/bin/python3
"""class defination"""
import json
import csv
import turtle


class Base:
    """
    base class initialization
    private class attribute:
    __nb_objects = 0: number of instantiated base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
        id: identity of the base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a list of dictionaries
        Args:
        list: list  of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
        list_objs: list of classes that inherits from base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string: A JSON str representation of a list of dicts.
        Returns: the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
        **dictionary: double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of files in csv
        Args:
        list_objs: list of inherited base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
