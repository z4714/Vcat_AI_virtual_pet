# 框架接口

## 模块化

### module



#### Object module

当前模块对象

## 属性

| 属性    | 类型   | 说明                                                  |
| :------ | :----- | :---------------------------------------------------- |
| exports | Object | 模块向外暴露的对象，使用`require`引用该模块时可以获取 |

## 示例代码

```js
// common.js
function sayHello(name) {
  console.log(`Hello ${name} !`)
}
function sayGoodbye(name) {
  console.log(`Goodbye ${name} !`)
}

module.exports.sayHello = sayHello
exports.sayGoodbye = sayGoodbye
```