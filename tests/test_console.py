#!/usr/bin/python3
"""Module is for TestHBNBCommand class"""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest
import datetime
import sys
import re
import os
from io import StringIO
from unittest.mock import patch

class TestHBNBCommand(unittest.TestCase):

    """Tests HBNBCommand console"""

    attribute_values = {
            str: "footbar108",
            int: 1008,
            float: 1.08
            }

    reset_values = {
            str: "",
            int: 0,
            float: 0.0
            }

    test_random_attributes = {
            "strfoo": "barfoo",
            "intfoo": 248,
            "floatfoo": 9.8
            }

    def setUp(self):
        """Sets up test cases"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
            self.resetStorage()

            def resetStorage(self):
                """This Data FileStorage Rsets"""
                FileStorage._FileStorage__objects = {}
                if os.path.isfile(FileStorage._FileStorage__file_path):
                    os.remove(FileStorage._FileStorage__file_path)

                    def test_help(self):
                        """This tests the help command"""
                        with patch('sys.stdout', new=StringIO()) as f:
                            HBNBCommand().onecmd("help")
                            s = """
                            Documented commands (type help <topic>):
                            =======================================
                            EOF all count create destroy hep quit show update

                            """

                            self.assertEquals(s, f.getvalue())

                            def test_help_EOF(self):
                                """This tests the help command."""
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("help EOF")
                                    s =  'Handles End Of File Character.\n           \n'
                                    self.assertEqual(s, f.getvalue())

                                    def test_help_quit(self):
                                """This tests the help command"""
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("help quit")
                                    s =  'Exits the program.\n           \n'
                                    self.assertEqual(s, f.getvalue())

                                    def test_help_create(self):
                                """This tests the help command."""
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("help create")
                                    s =  'This craetes an instance.\n           \n'
                                    self.assertEqual(s, f.getvalue())

                                    def test_help_show(self):
                                """This tests the help command."""
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("help show")
                                    s =  'This prints the string representation of an instance.\n           \n'
                                    self.assertEqual(s, f.getvalue())

                                    def test_help_destroy(self):
                                """This tests the help command."""
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("help destroy")
                                    s =  'Deletes an instance based on the class name and id.\n           \n'
                                    self.assertEqual(s, f.getvalue())

                                    def test_help_all(self):
                                """This tests the help command."""
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("help all")
                                    s =  'This prints the representation of all the instances.\n           \n'
                                    self.assertEqual(s, f.getvalue())

                                    def test_help_count(self):
                                """This tests the help command."""
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("help count")
                                    s =  'This counts instances of a class.\n           \n'
                                    self.assertEqual(s, f.getvalue())

                                    def test_help_update(self):
                                """This tests the help command."""
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("help update")
                                    s =  'updates instance by updating attribute.\n           \n'
                                    self.assertEqual(s, f.getvalue())
