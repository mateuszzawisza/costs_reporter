import time
import datetime

class CostsEntry(object):
    def __init__(self, service, operation, usagetype, resource, starttime,
            endtime, usagevalue):
        self.service = service
        self.operation = operation
        self.usagetype = usagetype
        self.resource = resource or None
        self.starttime = self._date_from_string(starttime)
        self.endtime = self._date_from_string(endtime)
        self.usagevalue = usagevalue


    def _date_from_string(self, datestring):
        return datetime.datetime(
                *time.strptime(datestring, "%m/%d/%y %H:%M:%S")[0:6]
                )
