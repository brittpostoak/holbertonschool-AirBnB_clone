#!/usr/bin/python3
"""
Object: Console
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import theClasses
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNB for command lines
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Empty line, does nothing"""
        pass

    def do_create(self, args):
        """Creates new instance"""
        if len(args) == 0:
            print("** Class name missing **")
            return
        token = args.split()

        try:
            newInstance = eval(token[0])()
            newInstance.save()
            print(newInstance.id)
        except:
            print("** Class does not exist **")

    def do_show(self, args):
        """Prints string representation of instance"""
        token = args.split()

        if len(token) == 0:
            print("** Class name missing **")
            return
        if len(token) == 1:
            print("** Instance id missing **")
            return
        try:
            eval(token[0])
        except:
            print("** Class does not exist **")

        objDict = storage.all()
        keyId = token[0] + "." + token[1]

        try:
            value = objDict[keyId]
            print(value)
        except KeyError:
            print("** No instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on class name"""
        token = args.split()

        if len(args) == 0:
            print("** Class name missing **")
            return
        if token[1] == 0:
            print("** Instance id missing **")

        try:
            eval(token[0])
        except:
            print("** Class does not exist **")
        objDict = storage.all()
        keyId = token[0] + "." + token[1]

        try:
            del objDict[keyId]
        except:
            print("** No instance found **")
        storage.save()

    def do_all(self, arg):
        """ Prints string represention of instances of a given class """

        if not arg:
            print("** Class name missing **")
            return

        token = arg.split()

        if token[0] not in theClasses:
            print("** Class does not exist **")
        else:
            all_objs = storage.all()
            newList = []

            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                if ob_name == token[0]:
                    newList += [val.__str__()]
            print(newList)

    def do_update(self, args):
        """ Updates an instance based on class name and id """

        if not args:
            print("** class name missing **")
            return

        token = args.split()

        if token[0] not in theClasses:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == token[0] and ob_id == token[1].strip('"'):
                    if len(token) == 2:
                        print("** attribute name missing **")
                    elif len(token) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, token[2], token[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_EOF(self, args):
        """End of file"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()
