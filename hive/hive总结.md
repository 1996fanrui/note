# 1


[磊哥Wiki](http://wiki.weli.cn/archives/965)

[]()

[]()

[]()

[]()

Hive Beeline开启debug模式 

/data/dmp/cloudera/parcels/CDH/lib/hive/bin/ext/beeline.sh 
文件中将 export HADOOP_CLIENT_OPTS="$HADOOP_CLIENT_OPTS -Dlog4j.configuration=beeline-log4j.properties" 修改为 

export HADOOP_CLIENT_OPTS="$HADOOP_CLIENT_OPTS -Dlog4j.configuration=beeline-log4j.properties -Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=500
5"





