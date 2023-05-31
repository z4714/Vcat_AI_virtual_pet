# 框架-WXS语法参考

# 变量

## 概念

- WXS 中的变量均为值的引用。
- 没有声明的变量直接赋值使用，会被定义为全局变量。
- 如果只声明变量而不赋值，则默认值为 `undefined`。
- var表现与javascript一致，会有变量提升。

```text
var foo = 1;
var bar = "hello world";
var i; // i === undefined
```

上面代码，分别声明了 `foo`、 `bar`、 `i` 三个变量。然后，`foo` 赋值为数值 `1` ，`bar` 赋值为字符串 `"hello world"`。

## 变量名

变量命名必须符合下面两个规则：

- 首字符必须是：字母（a-zA-Z），下划线（_）
- 剩余字符可以是：字母（a-zA-Z），下划线（_）， 数字（0-9）

## 保留标识符

以下标识符不能作为变量名：

```text
delete
void
typeof

null
undefined
NaN
Infinity
var

if
else

true
false

require

this
function
arguments
return

for
while
do
break
continue
switch
case
default
```