#!/usr/bin/env python

import sys
import unittest2

class TestBareBones(unittest2.TestCase):
    def test2_one_equals_one(self):
        self.assertEquals(1,1,"1!=1")
        
if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('test24', 'test_bare_bones', TestBareBones)
