#!/usr/bin/python3
"""
Script for the class Base
"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            pass
        else:
            if not isinstance(list_dictionaries, list):
                raise TypeError("Dictionary List should be a list")
            for dic in list_dictionaries:
                if not isinstance(dic, dict):
                    raise TypeError("List should contain valid dictionary")
        return json.dumps(list_dictionaries if
                          list_dictionaries is not None else [])

    @staticmethod
    def from_json_string(json_string):
        if not isinstance(json_string, str) and json_string is not None:
            raise TypeError("Expecting a json string")
        try:
            return json.loads(json_string)
        except:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        if not isinstance(list_objs, list):
            raise TypeError("Expecting a list of objects")
        for obj in list_objs:
            if not isinstance(obj, cls):
                raise TypeError(f"{obj} is not of instance {cls.__name__}")
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())

        f = cls.to_json_string(list_dict)
        with open(f"{cls.__name__}.json", "w", encoding="UTF8") as fp:
            fp.write(f)

    @classmethod
    def create(cls, **dictionary):
        newobj = cls(1, 1, 1, 1)
        newobj.update(**dictionary)
        return newobj

    @classmethod
    def load_from_file(cls):
        try:
            instlist = []
            with open(f"{cls.__name__}.json", "r", encoding="UTF8") as fp:
                from_dict = json.load(fp)
            for instdict in from_dict:
                inst = cls.create(**instdict)
                instlist.append(inst)
            return instlist
        except Exception as e:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        csv_list = []
        if cls.__name__ == "Rectangle":
            for obj in list_objs:
                csv_list.append(f"""{obj.id},{obj.width},
                                {obj.height},{obj.x},{obj.y}""")
        if cls.__name__ == "Square":
            for obj in list_objs:
                csv_list.append(f"{obj.id},{obj.size},{obj.x},{obj.y}")
        csv_str = "\n".join(csv_list)
        with open(f"{cls.__name__}.csv", "w", encoding="UTF8") as fp:
            fp.write(csv_str)

    @classmethod
    def load_from_file_csv(cls):
        with open(f"{cls.__name__}.csv", "r", encoding="UTF8") as fp:
            csv_str = fp.read()

        objs_attr_list_str = csv_str.split("\n")

        dict_list = []
        if cls.__name__ == "Rectangle":
            for obj_attr_list_str in objs_attr_list_str:
                rec_keys = ["id", "width", "height", "x", "y"]
                attr_vals = [int(y) for y in obj_attr_list_str.split(',')]
                obj_dict = {x: y for x, y in zip(rec_keys, attr_vals)}
                dict_list.append(obj_dict)

        if cls.__name__ == "Square":
            for obj_attr_list_str in objs_attr_list_str:
                sq_keys = ["id", "size", "x", "y"]
                attr_vals = [int(y) for y in obj_attr_list_str.split(',')]
                obj_dict = {x: y for x, y in zip(sq_keys, attr_vals)}
                dict_list.append(obj_dict)

        obj_list = []
        for ob_dict in dict_list:
            obj_list.append(cls.create(**ob_dict))

        return obj_list
