"""
test_strong_password_validator.py - Strong password validator with regexes tests

Written by Sergey Torshin @torshin5ergey
"""

import unittest
from strong_password_validator import strong_password_validator

class TestIsStrongPassword(unittest.TestCase):
    
    def setUp(self) -> None:
        self.strong_passwords = ['Pa55word!', 'Secure123', 'Password1!',
        'HelloWorld9', 'MyP@ssw0rd', 'Adm1nAcc3ss', 'Welcome123',
        'StrongP@ss9', 'P@ssw0rd2024', 'Qwerty1234']
        self.weak_passwords = ['password', 'PASSWORD', '12345678','Passwrd', 
        'helloworld', 'HELLO123', 'Test123', 'abc123!', 'QWERTY!', 'P@ss']
        return super().setUp()

    def test_strong(self):
        """Test strong passwords"""
        for i in self.strong_passwords:
            self.assertTrue(strong_password_validator(i))

    def test_weak(self):
        """Test weak passwords"""
        for i in self.weak_passwords:
            self.assertFalse(strong_password_validator(i))

if __name__ == "__main__":
    unittest.main()