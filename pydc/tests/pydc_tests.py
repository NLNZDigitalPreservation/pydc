from nose.tools import *
from pydc.pydc import DCRecord as DCR
from lxml import etree as ET


def test_basic_record():
    """Basic three-field record"""
    record = DCR()
    d = {"dc:title": "Test title", "dcterms:series": "5565",
    		"dcterms:bibliographicCitation": "2016-05-01"}
    for key in d.keys():
    	record.add_field(key, d[key])
    tag_list = list(record)
    assert(len(tag_list) == 3)


def test_basic_record_with_xsi_attrib():
    """Basic single-field record with an xsi-namespaced attrib"""
    record = DCR()
    record.add_field("dc:identifier xsi:type=SampleIdentifier", "Test ID")
    # tag_list = record.get_children()
    tag_list = list(record)
    assert(len(tag_list) == 1)