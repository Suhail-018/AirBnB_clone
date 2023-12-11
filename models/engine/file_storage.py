import json
import os


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):

        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
