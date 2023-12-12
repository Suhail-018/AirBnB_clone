#!/usr/bin/python3
"""This module defines the entry point of the command interpreter.

It defines one class, `HBNBCommand()`, which sub-classes the `cmd.Cmd` class.
inplace of the  frontend of web

It allows us to interactively and non-interactively:
    - create a data model
    - manage (create, update, destroy, etc) objects via a console / interpreter
    - store and persist objects to a file (JSON file)

Typical usage example:

    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""

import cmd
import shlex  # Add shlex module for splitting command-line arguments
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

curnt_classes = {'BaseModel': BaseModel, 'User': User,
                 'Amenity': Amenity, 'City': City, 'State': State,
                 'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

    def do_quit(self, arg):

        " Quit command to exit the program"
        return True

    def emptyline(self):
        """porints empty line when press enter button witempty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls = eval(args[0])
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = args[1]
                    key = '{}.{}'.format(cls.__name__, obj_id)
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls = eval(args[0])
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = args[1]
                    key = '{}.{}'.format(cls.__name__, obj_id)
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        if args and args[0] not in curnt_classes.keys():
            print("** class doesn't exist **")
        else:
            result = [str(value) for key, value in storage.all().items()]
            print(result)

    def do_update(self, line):
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in curnt_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        instance = storage.all()[key]
        # Assuming 'instance' is a dictionary with the attributes
        instance[attribute_name] = attribute_value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
