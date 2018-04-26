# 调查短信与电话

项目概况
================
在这一项目中，利用一组伪造的短信与电话通信记录，将会完成五个任务。将运用 Python 分析并回答与数据集中的短信与通话记录相关的问题。

学到什么？
---------------------------
完成项目后，可以：

* 设计并编写 Python 程序，完成现实任务
* 在计算机上编写 Python 程序
* 写出符合 [PEP8](https://www.python.org/dev/peps/pep-0008/) 编码规范的 Python 代码，代码具有良好的可读性
* 在 Python 中处理字符串和数值数据
* 选择并使用 Python 的内置数据结构
* 使用互联网资源来帮助你
* 使用 Python 的内置函数，并编写自己的函数
* 使用 Python 中的循环和条件语句

项目内容
================
完成 5 个任务，回答和 2016 年 9 月间的一组电话和短信通信记录相关的问题。

第一步 关于数据
--------

短信和电话数据已由 CSV 文件给出，在每个文件中，数据已经存储为一系列表格。
文本的子列已经整理为如下格式：

```
短信 = [	发送电话号码 (字符串),
	接收电话号码 (字符串),
	短信的时间戳 (字符串)]
```
电话列表中的每个元素都已整理为如下结构:

```
电话 = [	主叫电话号码 (字符串),
	被叫电话号码 (字符串),
	电话开始的时间戳 (字符串),
	电话持续时间（秒) (字符串)]
```

所有电话号码长度都是10位。每个电话号码均以指示位置和/或类型的代号开始。有三种不同的电话号码，每一种都有不同的格式:

* 固定电话以括号内的区号开始。区号的长度不定，但总是以0打头，例如：`(022)40840621`。
* 移动电话不包含括号，通过在数字中间添加一个空格的方式增加可读性。移动电话的移动代码指的是它的前四个数字，并且以 7、 8 或 9 开头。例如：`93412 66159`。
* 电话促销员的号码没有括号或空格 , 但以140开头. 例如: `1402316533`。

第二步 任务内容
----------

| 标准      | 符合规范                                     |
| ------- | :--------------------------------------- |
| 代码品质    | 你的代码应具有良好的结构与可读性，请遵循本课程中所指出的最佳规范。|
|只打印任务要求的内容 | 在开发过程中可以使用其他打印语句，但请在提交之前移除所有要求外的打印语句。提交的文件应该只打印任务要求的内容。|
| 任务0成功完成 | 脚本正确的输出了第一条短信与最后一次电话的信息。                  |
| 任务1成功完成 | 脚本正确的输出了数据集中**不同**的电话号码的数目。                 |
| 任务2成功完成 | 脚本正确的输出了通话时长最长的电话号码，以及通话时间（秒）。 |
| 任务3成功完成 | 脚本正确的输出被叫电话号码区号或移动代码，其主叫为班加罗尔的固定电话；在这些记录中，被叫也是班加罗尔固话所占比例是多少？ |
| 任务4成功完成 | 脚本正确的输出了疑似电话推销员的号码列表。                   |


**任务0:**
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
```
First record of texts, <incoming number> texts <answering number> at time <time>
Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds
```

**任务1:**
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
```
There are <count> different telephone numbers in the records.
```

**任务2:**
哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
```
<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.
```

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。


**任务3:**
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
```
The numbers called by people in Bangalore have codes:
 <list of codes>
```
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
```
<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore.
```
注意：百分比应包含2位小数。


**任务4:**
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
```
These numbers could be telemarketers: 
<list of numbers>
```
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
