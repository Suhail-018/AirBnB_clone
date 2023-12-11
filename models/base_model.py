import models
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['updated_at', 'created_at']:
                        setattr(self, key, datetime.strptime(value,                                       "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        dict_new = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dict_new[key] = value.isoformat()
            else:
                dict_new[key] = value
        dict_new['__class__'] = type(self).__name__
        return dict_new
