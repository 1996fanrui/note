# 剖析工业级排序的实现原理

## 介绍

- Java的Arrays.sort(int[] a) 和 Arrays.sort(short[] a)等基本类型排序

	- DualPivotQuicksort

- Java的Arrays.sort(Object[] a) 和 Collections.sort()

	- 用于Java对象排序算法
	
	- TimSort
	
	- 利用数列中的原始顺序，可以提高很多效率

## DualPivotQuicksort

- 快排 （五数取中）

	- 双轴快排，选择两个分区点，pivot1、pivot2

		- 选取两个分区点的方法
	
			- 数组中均匀地找五数并排序，取第2、4个元素做为分区点

		- 数据被两个分区点分成三段

			- |  < pivot1  |  pivot1 <= && <= pivot2  |    ?    |  > pivot2  |
	
	- 若五数中有重复的数据，采用3-way快排
		
		- |  < pivot  |   == pivot   |     ?    |  > pivot  |

		- 有重复数据时，3-way快排会有优化效果

- 归并排序

	- 数组长度大于286，且内部接近有序时使用归并（TimSort）

- 插入排序

	- 跳过最长的升序序列

	- 成对插入排序采用同时插入两个元素的方式提高效率

- 计数排序

	- byte，char，short基本类型数据范围小，会出现大量重复数据

## TimSort

- 归并排序

	- 合并run块（合并两个有序数组）

	- 飞奔模式

	- 逆序变有序

- 插入排序（当run块小于32时使用）

	- 二分插入排序

## 参考链接 

- TimSort源码分析
	
	[JDK1.8源码分析【排序】timsort](https://www.cnblogs.com/warehouse/p/9342279.html)
	
	[读 Java TimSort算法 源码 笔记](https://www.jianshu.com/p/10aa41b780f2)
	
- DualPivotQuicksort 源码分析
	
	[DualPivotQuickSort 双轴快速排序 源码 笔记](https://www.jianshu.com/p/6d26d525bb96)
	
- 快排优化原理

	[单轴快排（SinglePivotQuickSort）和双轴快排（DualPivotQuickSort）及其JAVA实现](https://blog.csdn.net/Holmofy/article/details/71168530)
	
	[QUICKSORTING - 3-WAY AND DUAL PIVOT](https://rerun.me/2013/06/13/quicksorting-3-way-and-dual-pivot/)

### [*back*](../)

### [*last*](../10.各排序性能对比)

### [*next*](../12.案例分析)
