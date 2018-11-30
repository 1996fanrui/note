# InputFormat相关分析

## InputFormat,InputSplit,RecordReader三者的关系介绍
- 三者都是抽象类  
- 计算切片这一步骤是在客户端完成

### InputFormat
#### 作用
> 验证作业的输入的正确性  
> 将输入文件切分成逻辑的InputSplits，一个InputSplit将被分配给一个单独的Mapper task

#### 类内容介绍-抽象方法
```
1.返回切片信息  
	List<InputSplit> getSplits(JobContext context)
2.返回RecordReader  
	RecordReader<K,V> createRecordReader(InputSplit split, TaskAttemptContext context )
```

#### 默认实现类
> 默认使用`TextInputFormat`类

### InputSplit
#### 作用
> Mappers的输入时一个个的输入分片，称为InputSplit

#### 类内容介绍-抽象方法
```	
1.返回切片大小
	long getLength()
2.按名称获取节点列表，其中拆分数据将是本地的
	String[] getLocations()
3.获取有关输入分割存储在哪些节点以及存储在每个位置的信息
	SplitLocationInfo[] getLocationInfo()
```

### RecordReader
#### 作用
> RecordReader会从InputSplit中正确读出一条一条的Ｋ－Ｖ对供Mapper使用

#### 类内容介绍-抽象方法
```
1.初始化Record Reader，只执行一次
	void initialize(InputSplit split,  TaskAttemptContext context  )
2.类似于迭代器的next()方法，遍历下一条数据(将指针后移)
	boolean nextKeyValue()
3.获取当前指向的Key
	KEYIN getCurrentKey()
4.获取当前指向的Value
	VALUEIN getCurrentValue()
5.返回Record Reader读取数据的进展，返回的值在0到1之间
	float getProgress()
6.Close the record reader
	void close()
```


## FileInputFormat介绍
### 分片规则


### 可以通知分片的参数 
```
1.boolean isSplitable(FileSystem fs, Path filename) 方法控制可否切片，不能切片的block，一个block对应一个split
2.max.size
3.min.size
```





