from ..costsentry import CostsEntry
import unittest
import datetime

class TestCostsEntry(unittest.TestCase):
    def setUp(self):
        self.costsentry = CostsEntry("AmazonEC2","RunInstances",
                "EU-BoxUsage:c3.large","", "07/01/15 00:00:00",
                "07/02/15 00:00:00","48")

    def test_init_service_set_properly(self):
        self.assertEqual(self.costsentry.service, "AmazonEC2")

    def test_init_operation_set_properly(self):
        self.assertEqual(self.costsentry.operation, "RunInstances")

    def test_init_usagetype_set_properly(self):
        self.assertEqual(self.costsentry.usagetype, "EU-BoxUsage:c3.large")

    def test_init_resource_set_properly(self):
        self.assertEqual(self.costsentry.resource, None)

    def test_init_starttime_set_properly(self):
        self.assertEqual(self.costsentry.starttime,
                datetime.datetime(2015,07,01,0,0,0))

    def test_init_endtime_set_properly(self):
        self.assertEqual(self.costsentry.endtime,
                datetime.datetime(2015,07,02,0,0,0))
