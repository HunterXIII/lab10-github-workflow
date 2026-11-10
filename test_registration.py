import unittest

from registration import is_valid_email


class EmailValidationTests(unittest.TestCase):
    def test_valid_addresses(self):
        for email in ("student@example.com", "first.last+lab@my-domain.example.org"):
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_addresses(self):
        for email in ("student.example.com", "student@", "student@example"):
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    def test_empty_and_whitespace(self):
        for email in ("", "student name@example.com", "student@example.com "):
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    def test_invalid_dots_and_hyphens(self):
        for email in (
            ".student@example.com",
            "student.@example.com",
            "first..last@example.com",
            "student@-example.com",
            "student@example-.com",
        ):
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    def test_accepts_tagged_address(self):
        self.assertTrue(is_valid_email("student+seminar@example.com"))
