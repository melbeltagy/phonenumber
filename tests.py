from unittest import TestCase, main

from phonenumber import PhoneNumber


class TestPhoneNumber(TestCase):
    def test_1(self):
        ph = PhoneNumber("+1(858)775-2868")

        self.assertEqual("+1(858)775-2868", ph.original_value)
        self.assertEqual("+18587752868", ph.stripped_value)
        self.assertEqual("(858)775-2868", ph.get_value_as_north_america())
        self.assertEqual("+1.858.775.2868", ph.get_value_as_international())

    def test_2(self):
        ph = PhoneNumber("+1(858)775-2868x123")

        self.assertEqual("+1(858)775-2868x123", ph.original_value)
        self.assertEqual("+18587752868x123", ph.stripped_value)
        self.assertEqual("(858)775-2868x123", ph.get_value_as_north_america())
        self.assertEqual("+1(858)775-2868x123",
                         ph.get_value_as_international())

    def test_3(self):
        ph = PhoneNumber("+598.123.4567x858")

        self.assertEqual("+598.123.4567x858", ph.original_value)
        self.assertEqual("+5981234567x858", ph.stripped_value)
        self.assertEqual("", ph.get_value_as_north_america())
        self.assertEqual("+598.123.456.7x858",
                         ph.get_value_as_international())

    def test_4(self):
        ph = PhoneNumber("+27 1234 5678 ext 4")

        self.assertEqual("+27 1234 5678 ext 4", ph.original_value)
        self.assertEqual("+2712345678x4", ph.stripped_value)
        self.assertEqual("", ph.get_value_as_north_america())
        self.assertEqual("+27 1234 5678 ext 4",
                         ph.get_value_as_international())

    def test_5(self):
        ph = PhoneNumber("858-775-2868")

        self.assertEqual("858-775-2868", ph.original_value)
        self.assertEqual("+18587752868", ph.stripped_value)
        self.assertEqual("(858)775-2868", ph.get_value_as_north_america())
        self.assertEqual("+1.858.775.2868",
                         ph.get_value_as_international())

    if __name__ == '__main__':
        main()
