# -*- coding:utf8 -*-
import unittest

from elasticsearch import Elasticsearch


class TestIndexSettings(unittest.TestCase):
    """
        https://www.elastic.co/guide/en/elasticsearch/reference/5.6/index-modules.html
        "number_of_shards" : 3,
        "number_of_replicas" : 2
        "index.write.wait_for_active_shards": "2"
    """

    def setUp(self):
        self.es = Elasticsearch()
        self.indexes = 'resources'

    def tearDown(self):
        print "do something after test.Clean up."