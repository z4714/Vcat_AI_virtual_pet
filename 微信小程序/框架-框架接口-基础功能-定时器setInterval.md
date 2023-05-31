# 框架-框架接口-基础功能-定时器

## sentInterval



### number setInterval(function callback, number delay, any rest)



设定一个定时器。按照指定的周期（以毫秒计）来执行注册的回调函数

## 参数

### function callback

回调函数

### number delay

执行回调函数之间的时间间隔，单位 ms。

### any rest

param1, param2, ..., paramN 等附加参数，它们会作为参数传递给回调函数。

## 返回值

### number

定时器的编号。这个值可以传递给 [clearInterval](https://developers.weixin.qq.com/miniprogram/dev/reference/api/clearInterval.html) 来取消该定时。