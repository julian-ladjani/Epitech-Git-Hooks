#!/usr/bin/python3

import unittest
import string
import executetest


class TestNmExecutableFile(unittest.TestCase):

    def setUp(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_nm", "my_objdump")
        self.gnureturn_value, self.gnustdout, self.gnustderr = executetest.execute_program("nm", "my_objdump")

    def test_output_diff_hard_test(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.stdout_list = string.split(self.stdout, '\n')
        self.gnustdout_list = string.split(self.gnustdout, '\n')
        self.gnustdout_list.sort()
        self.stdout_list.sort();
        self.assertTrue(self.stdout_list == self.gnustdout_list)


if __name__ == '__main__':
    executetest.execute_test()
