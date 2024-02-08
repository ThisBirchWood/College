import unittest

class myTests(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


'''
#?([a-f0-9]{6}|[a-f0-9]{3})\b
[0-9]{3}-[CD]-[0-9]{1, 6}

[\w\.-]+@[\w\.-]+

\(\+\d{3}\)-\d{2}-\d{7}

(\d{3})-(\d{3})-{(\d{4})}|\(\d{3}\) \d{3} \d{4}

\b
'''
