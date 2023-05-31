# 框架接口

## 小程序App

## getApp

**参数**

**Object object**

| 属性         | 类型    | 默认值 | 必填 | 说明                                                         | 最低版本                                                     |
| :----------- | :------ | :----- | :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| allowDefault | boolean | false  | 否   | 在 `App` 未定义时返回默认实现。当App被调用时，默认实现中定义的属性会被覆盖合并到App中。一般用于[独立分包](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/independent.html) | [2.2.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

**示例代码**

```js
// other.js
var appInstance = getApp()
console.log(appInstance.globalData) // I am global data
```

**注意事项**！！！

- 不要在定义于 `App()` 内的函数中，或调用 `App` 前调用 `getApp()` ，使用 `this` 就可以拿到 app 实例。
- 通过 `getApp()` 获取实例之后，不要私自调用生命周期函数。