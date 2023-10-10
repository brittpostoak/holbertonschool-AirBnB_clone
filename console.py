#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """command interpreter class"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exits"""

        return True

    def do_EOF(self, line):
        """exits program"""

        print()
        return True

    def emptyline(self):
        """doesnt execute anything"""
        pass

   def do_create(self, arg):
       """creates an instance of BaseModel saves to file and prints id"""
       args = arg.split()
       if args is None or args == []:
           print("** class name missing **")
           return
       elif (args[0] not in ["BaseModel", "User", "City", "Place", "State", 
           "Amenity", "Review"]):
           print("** class doesn't exist **")
           return
       else:
           new_instance = eval(f"{args[0]}()")
           new_instance.save()
           print(new_instance.id)

    def do_show(self, arg):
        """prints string rep of an instance based on cls name and id"""
        args = arg.split()
        if args is None or args == []:
            print("** class name missing **")
            return
        elif (args[0] not in ["BaseModel", "User", "City", 
            "Place", "State", "Amenity", "Review"]):
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            for key, value in models.storage.all().items():
                if key == f"{args[0].{args[1]}}":
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        if args is None or args == []:
            print("** class name missing **")
            return
        elif (args[0] not in ["BaseModel", "User", "City", 
            "Place", "State", "Amenity", "Review"]):
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("**instance id missing **")
            return
        else:
            for key in models.storage.all().keys():
                if key == f"{args[0]}.{args[1]}":
                    del models.storage.all()[key]
                    models.storage.save()
                    return
                print("** no instance found **")

    def do_all(self, args):
        """prints string rep of all instances"""
        args = arg.split()
        if args is None or args == []:
            obj_list = ([str(value) for value in
                models.storage.all().values()])
            print(obj_list)
        else:
            if (args[0] not in ["BaseModel", "User", "City",
                 "Place", "State", "Amenity", "Review"]):
                print("** class doesn't exist **")
                return
        else:
            obj_list = []
            for key in models.storage.all():
                if args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print(obj_list)

    def do_update(self, arg):
        """updates instance based on cls name and id"""
        args = arg.split()
        if args is None or args == []:
            print("** class name missing **")
            return
        elif (args[0] not in ["BaseModel", "User", "City",
             "Place", "State", "Amenity", "Review"]):
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(arg) < 4:
            print("** value missing **")
            return
        else:
            for key in models.storage.all():
                if key == f"{args[0]}.{args[1]}":
                    if type(args[3]) is str:
                        setattr(models.storage.all()[key],
                                args[2], str(args[3]))
                        models.storage.save()
                        return
                    elif type(args[3] is int:
                            setattr(models.storage.all()[key], 
                                args[2], str(args[3])))
                            models.storage.save()
                            return
                    elif type(args[3]) is float:
                        setattr(models.storage.all()[key], 
                                args[2], float(args[3]))                               
                        models.storage.save()
                        return
                print("** no instance found **")

    do default(self, line):
        return super().default(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
