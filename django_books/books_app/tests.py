import unittest
from django.test import TestCase
from .models import Page
from .tasks import *

# Create your tests here.


class TestTasks(unittest.TestCase):

    def test_send_email(self):
        self.assertEqual(
            send_email('Hello World.', 'n.a.s.t.y.a28v@gmail.com'), True)

    def test_letter_information(self):
        pages = Page.objects.filter(id=1)
        self.assertEqual(
            letter_formation(pages, 'ru', 'n.a.s.t.y.a28v@gmail.com'), True)


if __name__ == '__main__':
    unittest.main()
