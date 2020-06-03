#!/usr/local/bin/python3.7
from unittest import TestCase
from import_getenv.entry_point_command_line import main

class TestConsole(TestCase):
    def test_basic(self):
        main()