#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

"""Docstrings for the unittest."""
import sys
import os

from pathlib import Path
import unittest

sys.path.insert(0, str(Path(os.getcwd()).parent))
from prova_new.module1 import func1


class TestFunc1(unittest.TestCase):
    """Unittest for the module1 module"""

    def test_int(self):
        """Test with integers"""
        self.assertAlmostEqual(func1(2, 2), 4) 
    
    def test_float(self):
        """Test with floats"""
        self.assertAlmostEqual(func1(2.5, 2.5), 5.0) 


if __name__ == "__main__":
    unittest.main()
