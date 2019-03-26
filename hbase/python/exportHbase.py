#!/usr/bin/env python
# coding:utf8
import sys
import os
from optparse import OptionParser

# azkaban机器 root用户执行
# cd /data/dmp/test/test/hbase_export
# python exportHbase.py -t table_name -s start_timestamp -e end_timestamp
if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-t", help="hbase tablename")
    parser.add_option("-s", help="start timestamp")
    parser.add_option("-e", help="end timestamp")
    (options, args) = parser.parse_args()

    if options.t is None:
        print '没有指定 hbase tableName，直接结束程序'
        sys.exit(0)

    if options.s is None:
        print '没有指定 开始时间戳，直接结束程序'
        sys.exit(0)

    if options.e is None:
        print '没有指定 结束时间戳，直接结束程序'
        sys.exit(0)

    tableName = options.t
    startTimeStamp = options.s
    endTimeStamp = options.e

    
    status = os.system( 'hdfs dfs -rm -r /tmp/hbase_export_test/{tableName}'.format(tableName=tableName) )
    
    status = os.system( 'ssh root@node51.ikh.bigdata.dmp.com "hbase org.apache.hadoop.hbase.mapreduce.Export {tableName} /tmp/hbase_export_test/{tableName} 1 {startTimeStamp} {endTimeStamp}"'.format(tableName=tableName,startTimeStamp=startTimeStamp,endTimeStamp=endTimeStamp) )
    
    if status > 0 :
        sys.exit(1)
    
    os.system( 'rm -rf /data/dmp/test/test/hbase_export/{tableName}'.format(tableName=tableName) )

    os.system( 'rm -f /data/dmp/test/test/hbase_export/{tableName}.zip'.format(tableName=tableName) )

    status = os.system( 'hdfs dfs -get /tmp/hbase_export_test/{tableName}'.format(tableName=tableName) )
    
    if status > 0 :
        sys.exit(1)
    
    status = os.system( 'zip -r {tableName}.zip ./{tableName}'.format(tableName=tableName) )
    
    if status > 0 :
        sys.exit(1)
    
    status = os.system( 'sz {tableName}.zip'.format(tableName=tableName) )
    
    if status > 0 :
        sys.exit(1)

    os.system( 'rm -rf /data/dmp/test/test/hbase_export/{tableName}'.format(tableName=tableName) )

    os.system( 'rm -f /data/dmp/test/test/hbase_export/{tableName}.zip'.format(tableName=tableName) )

    print 'done'

