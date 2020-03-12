#!/usr/bin/python3

import sipmap_pb2

historyheader = sipmap_pb2.HistoryHeader()
historyheader.somethingusefull = 5
print(historyheader.__str__())

f = open('hh', "wb")
f.write(historyheader.SerializeToString())
f.close()


trace = sipmap_pb2.Trace()
trace.traceheader.ssp="hallo"
tracedata= trace.tracedata32.add()
tracedata.data=1.2434
tracedata= trace.tracedata32.add()
tracedata.data=1.2434
print(trace.__str__())

f = open('th', "wb")
f.write(historyheader.SerializeToString())
f.close()


historyheader_read = sipmap_pb2.HistoryHeader()
f = open("hh", "rb")
historyheader_read.ParseFromString(f.read())
f.close()
print(historyheader.__str__())


trace_read = sipmap_pb2.Trace()
f = open("th", "rb")
trace_read.ParseFromString(f.read())
f.close()
print(trace.__str__())




