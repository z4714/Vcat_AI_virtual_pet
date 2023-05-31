# 框架接口

## 自定义组件

### Behavior



### Behavior(Object object)

注册一个 `behavior`，接受一个 `Object` 类型的参数。



## 参数

#### Object object

| 定义段           | 类型         | 是否必填 | 描述                                                         | 最低版本                                                     |
| :--------------- | :----------- | :------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| properties       | Object Map   | 否       | 组件的对外属性，是属性名到属性设置的映射表                   |                                                              |
| data             | Object       | 否       | 组件的内部数据，和 `properties` 一同用于组件的模板渲染       |                                                              |
| observers        | Object       | 否       | 组件数据字段监听器，用于监听 properties 和 data 的变化，参见 [数据监听器](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/observer.html) | [2.6.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| methods          | Object       | 否       | 组件的方法，包括事件响应函数和任意的自定义方法，关于事件响应函数的使用，参见 [组件间通信与事件](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html) |                                                              |
| behaviors        | String Array | 否       | 类似于mixins和traits的组件间代码复用机制，参见 [behaviors](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/behaviors.html) |                                                              |
| created          | Function     | 否       | 组件生命周期函数-在组件实例刚刚被创建时执行，注意此时不能调用 `setData` ) |                                                              |
| attached         | Function     | 否       | 组件生命周期函数-在组件实例进入页面节点树时执行)             |                                                              |
| ready            | Function     | 否       | 组件生命周期函数-在组件布局完成后执行)                       |                                                              |
| moved            | Function     | 否       | 组件生命周期函数-在组件实例被移动到节点树另一个位置时执行)   |                                                              |
| detached         | Function     | 否       | 组件生命周期函数-在组件实例被从页面节点树移除时执行)         |                                                              |
| relations        | Object       | 否       | 组件间关系定义，参见 [组件间关系](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/relations.html) |                                                              |
| lifetimes        | Object       | 否       | 组件生命周期声明对象，参见 [组件生命周期](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) | [2.2.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| pageLifetimes    | Object       | 否       | 组件所在页面的生命周期声明对象，参见 [组件生命周期](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) | [2.2.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| definitionFilter | Function     | 否       | 定义段过滤器，用于自定义组件扩展，参见 [自定义组件扩展](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/extend.html) | [2.2.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

```js
// my-behavior.js
module.exports = Behavior({
  behaviors: [],
  properties: {
    myBehaviorProperty: {
      type: String
    }
  },
  data: {
    myBehaviorData: {}
  },
  attached: function(){},
  methods: {
    myBehaviorMethod: function(){}
  }
})
```