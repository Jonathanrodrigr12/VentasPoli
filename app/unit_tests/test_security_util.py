import unittest
from  app.utils.security.security_util import SecurityUtil,Constants

class test_security_util(unittest.TestCase):
    
    def test_get_key_isValid(self):
        arrange= Constants.secret
        act= SecurityUtil.get_key()
        self.assertIsNotNone(act)
        self.assertEqual(act, arrange)
        
    def test_get_algorithms_isValid(self):
        arrange= Constants.algoritm
        act= SecurityUtil.get_algorithms()
        self.assertIsNotNone(act)
        self.assertEqual(act, arrange)

    def test_get_token_isValid(self):
        arrange= "carlos@ct.dt"        
        act = SecurityUtil.get_token({
                'user': arrange
            })
        self.assertIsNotNone(act)

    def test_validate_token_isNotValid(self):
        expected_code = 401
        expected_msg = "Invalid Token"

        arrange= "Invalid Token 1234"
        with self.assertRaises(Exception) as context:
            SecurityUtil.validate_token(arrange)
        
        exc = context.exception
        self.assertIsNotNone(exc)
        self.assertEqual(context.exception.status, expected_code)
        self.assertEqual(context.exception.details[0]["message"], expected_msg)
    
    def test_validate_token_isNotValidToken(self):
        expected_code = 401
        expected_msg = "Expired token, please send a valid token"

        arrange= {
            'user': "carlos@ct.dt" 
        }        
        arrange = SecurityUtil.get_token(arrange, -200) #-200 of expiration to make token invalid
        with self.assertRaises(Exception) as context:
            SecurityUtil.validate_token(arrange)
        
        exc = context.exception
        self.assertIsNotNone(exc)
        self.assertEqual(context.exception.status, expected_code)
        self.assertEqual(context.exception.details[0]["message"], expected_msg)
    
    def test_validate_token_ValidToken(self):
        expectetVal = {
            'user': "carlos@ct.dt" 
        }
        token = SecurityUtil.get_token(expectetVal)
        arrange = (True, token, expectetVal)

        act = SecurityUtil.validate_token(token)
        self.assertIsNotNone(act)
        self.assertEqual(act[0], arrange[0])
        self.assertEqual(act[1], arrange[1])
        self.assertEqual(act[2], arrange[2])