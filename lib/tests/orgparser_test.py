#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2013-08-20 17:24:43 vk>

import unittest
from lib.utils import *
from lib.orgparser import *
import pickle ## for serializing and storing objects into files
from os import remove

class TestOrgParser(unittest.TestCase):

    ## FIXXME: (Note) These test are *not* exhaustive unit tests. They only
    ##         show the usage of the methods. Please add "mean" test cases and
    ##         borderline cases!

    logging = None


    def setUp(self):
        verbose = False
        quiet = False
        self.logging = Utils.initialize_logging(verbose, quiet)


    def tearDown(self):
        pass


    def test_simple_org_to_blogdata(self):

            ## format of the storage file
            ## pickle offers, e.g., 0 (ASCII; human-readable) or pickle.HIGHEST_PROTOCOL (binary; more efficient)
            #PICKLE_FORMAT = pickle.HIGHEST_PROTOCOL
        PICKLE_FORMAT = 0

        testfile_org = "simple.org"  ## manually written Org-mode file; has to be placed in "lib/tests/"
        testfile_temp_output = "simple_org_-_lastrun.pk"
        testfile_temp_reference = "simple_org_-_reference.pk"

        self.assertTrue(os.path.isfile(testfile_org))  ## check, if test input file is found

        ## make sure that no old output file is found:
        if os.path.isfile(testfile_temp_output):
            remove(testfile_temp_output)
            
        blog_data = []  ## initialize the empty list
        parser = OrgParser(testfile_org, self.logging)

        ## parse the example Org-mode file:
        blog_data.extend(parser.parse_orgmode_file())

        ## write data to dump file:
        with open(testfile_temp_output, 'wb') as output:
            pickle.dump(blog_data, output, PICKLE_FORMAT)

        ## check, if dump file was created:
        self.assertTrue(os.path.isfile(testfile_temp_output))

        reference_blog_data = None

        ## read reference data from file:
        with open(testfile_temp_reference, 'r') as fileinput:
            reference_blog_data = pickle.load(fileinput)

        self.assertEqual(reference_blog_data, blog_data)

        ## optionally clean up:
        #remove(testfile_temp_output)

