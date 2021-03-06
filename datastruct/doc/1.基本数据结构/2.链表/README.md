# 链表

## 介绍

- 通过“指针”将一组零散的内存块串联起来使用

- 数组与链表的内存分布对比
    
    ![](./picture/链表内存分配.jpg)

    - 数组必须申请连续的内存空间，链表利用每个节点的索引找到后续节点，利用起内存中的小空间

- 链表中的概念
    
    - 结点
    
        - 头结点
        - 尾节点
        
    - 后继指针 next

- 单链表

    ![](./picture/单链表.jpg)

    - 单链表的插入和删除数据
    
        ![](./picture/链表插入删除数据.jpg)
        
        - 插入数据x到b和c之间，只需要将x指向c，b指向x即可
        
        - 删除数据b，只需要将a指向c即可，之后jvm中没有引用指向对象b，则b之后会被垃圾回收
        
    - 不能高效地按照下标访问，比如想要访问第k个元素，只能从头开始遍历

- 循环链表

    ![](./picture/循环链表.jpg)

    - 优点是从链尾到链头比较方便
    
    - 适用场景：当业务场景需要让链尾很快找到链头时，可以使用循环链接。比如约瑟夫问题
    

- 双向链表

    ![](./picture/双向链表.jpg)

    - 优点是可以支持双向遍历
    
    - 适用场景：当业务场景需要让节点很快找到前继节点时，可以使用双向链表。
        
        - 比如 链表 a -> b -> c -> d -> e,现在想要删除c结点，直接将b指向d即可，但是单向链表并不能直接知道c的节点是b，所以需要从头遍历，看谁的后继节点是c，效率太低了，这里可以使用双向链表
    
- 双向循环链表 

    ![](./picture/双向循环链表.jpg)

    - 优点是双向链表和循环链表的优点

- 数组与链表时间复杂度对比

    ![](./picture/数组链表对比.jpg)
    
    - 注：数组的随机访问只有按下标访问才是O(1)

- 链表练习题（[源码 click here](../../../src/main/java/fanrui/study/linkedlist)）

    1. [单链表反转](../../../src/main/java/fanrui/study/linkedlist/Reverse.java)
    
    2. [检测链表是否有环](../../../src/main/java/fanrui/study/linkedlist/CheckCircle.java)
    
    3. [删除链表倒数第 k 个结点](../../../src/main/java/fanrui/study/linkedlist/DeleteLastKthNode.java)
    
    4. [求链表的中间结点](../../../src/main/java/fanrui/study/linkedlist/FindMiddleNode.java)
    
    5. [有序链表合并](../../../src/main/java/fanrui/study/linkedlist/MergeSortedLists.java)

### [*back*](../)

### [*last*](../1.数组)

### [*next*](../3.栈)


