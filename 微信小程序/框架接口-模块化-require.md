# 框架接口

## 模块化

### require

# require

引入模块。返回模块通过 [`module.exports`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/module.html) 或 `exports` 暴露的接口。

需要引入其他分包的模块的时候，可以通过配置 `callback` 回调函数来异步获取指定模块。异步获取失败的时候，将会触发 `error` 回调函数。

## 参数

| 名称     | 类型     | 必填 | 说明                                                         |
| :------- | :------- | :--- | :----------------------------------------------------------- |
| path     | string   | 是   | 需要引入模块文件相对于当前文件的相对路径，或npm模块名，或npm模块路径。默认不支持绝对路径，可通过配置 `resolveAlias` 自定义路径映射。 |
| callback | function | 否   | 异步加载成功回调函数，该回调函数参数为成功加载的模块。       |
| error    | function | 否   | 异步加载失败回调函数，该回调函数参数为错误信息和模块名。     |

## require.async 链式调用

可以通过链式调用的方式使用。

```javascript
require
    .async('path/to/mod')
    .then((mod) => {
        console.log(mod)
    })
    .catch(({ errMsg, mod }) => {
        console.error(`path: ${mod}, ${errMsg}`)
    })
```

## 示例代码

### 同一包内调用

```javascript
// common.js
function sayHello(name) {
  console.log(`Hello ${name} !`)
}
function sayGoodbye(name) {
  console.log(`Goodbye ${name} !`)
}

module.exports.sayHello = sayHello
exports.sayGoodbye = sayGoodbye
var common = require('common.js')
Page({
  helloMINA: function() {
    common.sayHello('MINA')
  },
  goodbyeMINA: function() {
    common.sayGoodbye('MINA')
  }
})
```

### 跨分包异步调用

```javascript
// subpackage/common.js 分包 common 文件
export const sayHello = () => console.log("hello")
// pages/index.js 主包页面

let common;
require('../../subpackage/common.js', (mod) => {
    common = mod
}, ({ errMsg, mod }) => {
    console.error(`path: ${mod}, ${errMsg}`)
})

Page({
    sayHello() {
        common && common.sayHello()
    }
})
```