import time
import datetime

class CostsEntry(object):
    def __init__(self, service, operation, usagetype, resource, starttime,
            endtime, usagevalue):
        self.service = service
        self.operation = operation
        self.usagetype = usagetype
        self.resource = resource
        self.starttime = starttime
        self.endtime = endtime
        self.usagevalue = usagevalue

    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, resource):
        if not resource:
            self.__resource = None
        else:
          self.__resource = resource

    @property
    def starttime(self):
        return self.__starttime

    @starttime.setter
    def starttime(self, starttime):
        self.__starttime = self._date_from_string(starttime)

    @property
    def endtime(self):
        return self.__endtime

    @endtime.setter
    def endtime(self, endtime):
        self.__endtime = self._date_from_string(endtime)

    def _date_from_string(self, datestring):
        return datetime.datetime(
                *time.strptime(datestring, "%m/%d/%y %H:%M:%S")[0:6]
                )
