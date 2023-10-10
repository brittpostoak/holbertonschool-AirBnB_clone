#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
