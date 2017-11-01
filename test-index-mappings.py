# -*- coding:utf8 -*-
import unittest

from elasticsearch import Elasticsearch


class TestIndexMappings(unittest.TestCase):
    """
    https://www.elastic.co/guide/en/elasticsearch/reference/5.6/mapping.html
    """
    def setUp(self):
        self.es = Elasticsearch()
        self.indexes = 'resources'

    def tearDown(self):
        print "do something after test.Clean up."
        pass

    def testBasicMapping(self):
        common = {
            "title": {
                "type": "text",
                # "analyzer": "jieba",
                # "search_analyzer": "jieba"
            },
            "source": {
                "type": "keyword"
            },
            "file_size": {
                "type": "long"
            },
            "file_type": {
                "type": "keyword",
            },
            "taked_time": {
                "type": "date"
            },
            "download_times": {
                "type": "long",
            },
            "url": {
                "type": "text",
                "index": False,
                "store": True
            },
            "user_id": {
                "type": "keyword"
            },
            "user_name": {
                "type": "keyword"
            },
            "extensions": {
                "type": "keyword"
            },
            # TODO 最近检测时间
            "last_checkup_time": {
                "type": "date"
            }
        }

        bok_mappings = {
            'tags': {
                'type': 'text',
                'index': 'not_analyzed'
            },
            'year': {
                'type': 'long'
            },
            'language': {
                'type': 'keyword'
            },
            'authors': {
                'type': 'text',
                'index': 'not_analyzed'
            }
        }
        bok = common.copy()
        bok.update(bok_mappings)
        if not self.es.indices.exists(index=self.indexes):
            self.es.indices.create(index=self.indexes, body={"mappings": {'weipan': {'properties': bok}}})

    def testMappings(self):
        self.es.index("resources", "weipan", {
            "authors": ["hello", "elastic", "search"]
        })

    def testCreating(self):
        self.es.indices.create(index="other_indexes", body={
            "mappings": {
                "doc1": {"properties": {"name": {"type": 'long'}}},
                "doc2": {"properties": {"name": {"type": 'long'}}}
            }})

    def testSettings(self):
        # http://www.elastic.co/guide/en/elasticsearch/reference/current/indices-update-settings.html
        print self.es.indices.get_settings(index=self.indexes)
        self.es.indices.put_settings(index=self.indexes, body={"index": {
            # "number_of_shards": 3,
            "number_of_replicas": 2
        }})

        print self.es.indices.get_settings(index=self.indexes)
    def testUpdateMappings(self):
        self.es.indices.put_mapping(index=self.indexes, doc_type="weipan",
                                    body={"properties": {"hello": {"type": "text"}}})

    def testDoctypeUpdateMappings(self):
        self.es.indices.put_mapping(index=self.indexes, doc_type="baidu",
                                    body={"properties": {"hello": {"type": "text"}}})