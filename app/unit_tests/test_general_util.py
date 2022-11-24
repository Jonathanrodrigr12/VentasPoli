import unittest
from app.utils.general.general_util import Utils

class test_general_util(unittest.TestCase):
    
    def test_validate_string_validString(self):
        arrange= "valid string"
        act= Utils.validate_string(None, arrange)
        self.assertIsNone(act)

    def test_validate_string_invalidString(self):
        arrange= ""
        act= Utils.validate_string(None, arrange)
        self.assertFalse(act)

    def test_validate_string_invalidValue(self):
        arrange= None
        act= Utils.validate_string(None, arrange)
        self.assertFalse(act)