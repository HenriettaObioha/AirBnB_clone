#!/usr/bin/python3
"""This module is for entry point of command interpreter"""

import cmd
import re
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb)"

    def default(self, line):
        """Catch commands if nothing else matches then"""
        # print("DEF:::", line)
        self._precmd(line)

        def _precmd(self, line):
            """Intercepts commands to test for class.syntax()"""
            # print("DEF:::", line)
            self._precmd(line)

            def  _precmd(self, line):
                """This intercepts commands to test for class.syntax()"""
                # print("PRECMD:::", line)
                match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
                if not match:
                    return line
                classname = match.group(1)
                method = match.group(2)
                args = match.group (3)
                match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
                if match_uid_and_args:
                    uid = match_uid_and_args.group(1)
                    attr_or_dict = match_uid_and_args.group(2)
                else:
                    uid = args
                    attr_or_dict = False


