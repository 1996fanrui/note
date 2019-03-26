#!/usr/bin/env python
# coding:utf8
import sys
import os
from optparse import OptionParser


# Mac执行  root用户执行
# su root
# python /Users/fanrui/Documents/note/hbase/python/importHbase.py -t tablename
if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-t", help="hbase tablename")
    (options, args) = parser.parse_args()

    if options.t is None:
        print '没有指定 hbase tableName，直接结束程序'
        sys.exit(0)

    tableName = options.t

    status = os.system( 'ssh root@node101.bigdata.dmp.local.com "rm -f /root/test/tmp/{tableName}.zip"'.format(tableName=tableName) )
    
    status = os.system( 'scp /Users/fanrui/Downloads/{tableName}.zip root@node101.bigdata.dmp.local.com:/root/test/tmp'.format(tableName=tableName) )

    status = os.system( 'ssh root@node101.bigdata.dmp.local.com "rm -rf /root/test/tmp/{tableName}"'.format(tableName=tableName) )

    if status > 0 :
        sys.exit(1)

    status = os.system( 'ssh root@node101.bigdata.dmp.local.com "cd /root/test/tmp; unzip /root/test/tmp/{tableName}.zip"'.format(tableName=tableName) )
    
    if status > 0 :
        sys.exit(1)
    
    status = os.system( 'ssh root@node101.bigdata.dmp.local.com "hdfs dfs -rm -r /tmp/hbase_import_test/{tableName}"'.format(tableName=tableName) )

    status = os.system( 'ssh root@node101.bigdata.dmp.local.com "hdfs dfs -mkdir -p /tmp/hbase_import_test/{tableName}"'.format(tableName=tableName) )

    if status > 0 :
        sys.exit(1)
    
    status = os.system( 'ssh root@node101.bigdata.dmp.local.com "hdfs dfs -put /root/test/tmp/{tableName}/* /tmp/hbase_import_test/{tableName}"'.format(tableName=tableName) )
    
    if status > 0 :
        sys.exit(1)
    
    status = os.system( 'ssh root@node101.bigdata.dmp.local.com "hbase org.apache.hadoop.hbase.mapreduce.Import {tableName} /tmp/hbase_import_test/{tableName}"'.format(tableName=tableName) )
    
    if status > 0 :
        sys.exit(1)

    os.system( 'mv /Users/fanrui/Downloads/{tableName}.zip /Users/fanrui/Downloads/recycle_bin'.format(tableName=tableName) )

    print 'done'

