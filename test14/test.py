#!/usr/bin/env python

import sys
import unittest1

class TestBareBones(unittest1.TestCase):
    def test1_one_equals_one(self):
        self.assertEquals(1,1,"1!=1")
        
if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('test14', 'test_bare_bones', TestBareBones)
