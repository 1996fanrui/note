# Yarn调度器Scheduler

## 如果存在资源需求，则每个队列对在任何给定时间分配给用户的资源百分比强制实施限制。用户限制可以在最小值和最大值之间变化。前者（最小值）设置为此属性值，后者（最大值）取决于已提交应用程序的用户数。例如，假设此属性的值为25.如果两个用户已将应用程序提交到队列，则任何单个用户都不能使用超过50％的队列资源。如果第三个用户提交应用程序，则任何单个用户都不能使用超过33％的队列资源。对于4个或更多用户，没有用户可以使用超过25％的队列资源。值100表示​​不强加用户限制。默认值为100.值指定为整数。


root角色下使用 capacity策略，root角色下的prod和prior之间是capacity策略
且设置prod不能超过集群资源的80%，保障随时有预留的资源给 prior


root.prod 内部使用 fair策略
root.prior 内部使用 fair策略



hive指定队列
set mapred.job.queue.name=pms;



<allocations>
  <defaultqueueschedulingpolicy>fair</defaultqueueschedulingpolicy>
    <queue name="uat">
      <weight>40<weight>
      <schedulingpolicy>fifo</schedulingpocliy>
      <minResources>100 mb,100 vcores</minResources>
      <maxResources>150 mb,200vcores</maxResources>
      <maxRunningApps>200</maxRunningApps>
      <minSharePreemptionTimeout>300</minSharePreemptionTimeout>
    </queue>

    <queue name="dev">
      <weight>60<weight>
      <minResources>30 mb,30 vcores</minResources>
      <maxResources>50 mb,50vcores</maxResources>
    </queue>

    <queuename="eng" />

    <queuename="science" />

    <queueplacementpolicy>
      <rule name="specified" create="false"></rule>
      <rule name="primarygroup" create="false"></rule>
      <rule name="default" queue="dev.eng"></rule>
    </queueplacementpolicy>

    <user name="userA">
      <maxRunningApps>400</maxRunningApps>
    </user>

    <userMaxAppsDefault>40</userMaxAppsDefault>
    <fairSharePreemptionTimeout>6000</fairSharePreemptionTimeout>
</allocations>



如果存在资源需求，则每个队列对在任何给定时间分配给用户的资源百分比强制实施限制。
用户限制可以在最小值和最大值之间变化。前者（最小值）设置为此属性值，
后者（最大值）取决于已提交应用程序的用户数。例如，假设此属性的值为25.
如果两个用户已将应用程序提交到队列，则任何单个用户都不能使用超过50％的队列资源。
如果第三个用户提交应用程序，则任何单个用户都不能使用超过33％的队列资源。
对于4个或更多用户，没有用户可以使用超过25％的队列资源。值100表示​​不强加用户限制。默认值为100.值指定为整数。





