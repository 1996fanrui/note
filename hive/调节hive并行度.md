
- hive.exec.parallel参数控制在同一个sql中的不同的job是否可以同时运行,默认为false.


- hive.exec.parallel.thread.number就是控制对于同一个sql来说同时可以运行的job的最大值,该参数默认为8.此时最大可以同时运行8个job.(前提是这8个job没有依赖关系)
 	- 对于job很多的，而且不相互依赖，能同时执行的任务有作用
 	- hive on spark 中可以理解为stage的关系，多个stage是否可以并行执行，该参数控制同一个sql同时可以运行的stage的最大值


- 设置map阶段的并行度



- 设置reduce阶段的并行度
	- set mapred.reduce.tasks=8;
	- 在hive on spark场景中，可以吧第一个stage当做map，后续的stage都当做reduce阶段


- 1
	- distribute by field_name 

