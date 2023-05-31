# 框架-WXS语法参考

# WXS 模块

WXS 代码可以编写在 wxml 文件中的 `<wxs>` 标签内，或以 `.wxs` 为后缀名的文件内。

## 模块

每一个 `.wxs` 文件和 `<wxs>` 标签都是一个单独的模块。

每个模块都有自己独立的作用域。即在一个模块里面定义的变量与函数，默认为私有的，对其他模块不可见。

一个模块要想对外暴露其内部的私有变量与函数，只能通过 `module.exports` 实现。

## .wxs 文件

在**微信开发者工具**里面，右键可以直接创建 `.wxs` 文件，在其中直接编写 WXS 脚本。

**示例代码：**

```text
// /pages/comm.wxs

var foo = "'hello world' from comm.wxs";
var bar = function(d) {
  return d;
}
module.exports = {
  foo: foo,
  bar: bar
};
```

上述例子在 `/pages/comm.wxs` 的文件里面编写了 WXS 代码。该 `.wxs` 文件可以被其他的 `.wxs` 文件 或 WXML 中的 `<wxs>` 标签引用。

### module 对象

每个 `wxs` 模块均有一个内置的 `module` 对象。

#### 属性

- `exports`: 通过该属性，可以对外共享本模块的私有变量与函数。

**示例代码：**

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/KYgu1Km36pZP)

```text
// /pages/tools.wxs

var foo = "'hello world' from tools.wxs";
var bar = function (d) {
  return d;
}
module.exports = {
  FOO: foo,
  bar: bar,
};
module.exports.msg = "some msg";
<!-- page/index/index.wxml -->

<wxs src="./../tools.wxs" module="tools" />
<view> {{tools.msg}} </view>
<view> {{tools.bar(tools.FOO)}} </view>
```

页面输出：

```text
some msg
'hello world' from tools.wxs
```

### require函数

在`.wxs`模块中引用其他 `wxs` 文件模块，可以使用 `require` 函数。

引用的时候，要注意如下几点：

- 只能引用 `.wxs` 文件模块，且必须使用相对路径。
- `wxs` 模块均为单例，`wxs` 模块在第一次被引用时，会自动初始化为单例对象。多个页面，多个地方，多次引用，使用的都是同一个 `wxs` 模块对象。
- 如果一个 `wxs` 模块在定义之后，一直没有被引用，则该模块不会被解析与运行。

**示例代码：**

```text
// /pages/tools.wxs

var foo = "'hello world' from tools.wxs";
var bar = function (d) {
  return d;
}
module.exports = {
  FOO: foo,
  bar: bar,
};
module.exports.msg = "some msg";
// /pages/logic.wxs

var tools = require("./tools.wxs");

console.log(tools.FOO);
console.log(tools.bar("logic.wxs"));
console.log(tools.msg);
<!-- /page/index/index.wxml -->

<wxs src="./../logic.wxs" module="logic" />
```

控制台输出：

```text
'hello world' from tools.wxs
logic.wxs
some msg
```

## `<wxs>` 标签

| 属性名 | 类型   | 默认值 | 说明                                                         |
| :----- | :----- | :----- | :----------------------------------------------------------- |
| module | String |        | 当前 `<wxs>` 标签的模块名。必填字段。                        |
| src    | String |        | 引用 .wxs 文件的相对路径。仅当本标签为**单闭合标签**或**标签的内容为空**时有效。 |

### module 属性

module 属性是当前 `<wxs>` 标签的模块名。在单个 wxml 文件内，建议其值唯一。有重复模块名则按照先后顺序覆盖（后者覆盖前者）。不同文件之间的 wxs 模块名不会相互覆盖。

module 属性值的命名必须符合下面两个规则：

- 首字符必须是：字母（a-zA-Z），下划线（_）
- 剩余字符可以是：字母（a-zA-Z），下划线（_）， 数字（0-9）

**示例代码：**

```html
<!--wxml-->

<wxs module="foo">
var some_msg = "hello world";
module.exports = {
  msg : some_msg,
}
</wxs>
<view> {{foo.msg}} </view>
```

页面输出：

```text
hello world
```

上面例子声明了一个名字为 `foo` 的模块，将 `some_msg` 变量暴露出来，供当前页面使用。

### src 属性

src 属性可以用来引用其他的 `wxs` 文件模块。

引用的时候，要注意如下几点：

- 只能引用 `.wxs` 文件模块，且必须使用相对路径。
- `wxs` 模块均为单例，`wxs` 模块在第一次被引用时，会自动初始化为单例对象。多个页面，多个地方，多次引用，使用的都是同一个 `wxs` 模块对象。
- 如果一个 `wxs` 模块在定义之后，一直没有被引用，则该模块不会被解析与运行。

**示例代码：**

```js
// /pages/index/index.js

Page({
  data: {
    msg: "'hello wrold' from js",
  }
})
<!-- /pages/index/index.wxml -->

<wxs src="./../comm.wxs" module="some_comms"></wxs>
<!-- 也可以直接使用单标签闭合的写法
<wxs src="./../comm.wxs" module="some_comms" />
-->

<!-- 调用 some_comms 模块里面的 bar 函数，且参数为 some_comms 模块里面的 foo -->
<view> {{some_comms.bar(some_comms.foo)}} </view>
<!-- 调用 some_comms 模块里面的 bar 函数，且参数为 page/index/index.js 里面的 msg -->
<view> {{some_comms.bar(msg)}} </view>
```

页面输出：

```text
'hello world' from comm.wxs
'hello wrold' from js
```

上述例子在文件 `/page/index/index.wxml` 中通过 `<wxs>` 标签引用了 `/page/comm.wxs` 模块。

## 注意事项

- `<wxs>` 模块只能在定义模块的 WXML 文件中被访问到。使用 `<include>` 或 `<import>` 时，`<wxs>` 模块不会被引入到对应的 WXML 文件中。
- `<template>` 标签中，只能使用定义该 `<template>` 的 WXML 文件中定义的 `<wxs>` 模块。