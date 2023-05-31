# 框架接口

## 页面

### page(Object object)

注册小程序中的一个页面。接受一个 `Object` 类型参数，其指定页面的初始数据、生命周期回调、事件处理函数等。

#### **参数**

**Object object**

| 属性                                                         | 类型         | 默认值 | 必填 | 说明                                                         |
| :----------------------------------------------------------- | :----------- | :----- | :--- | :----------------------------------------------------------- |
| [data](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#data) | Object       |        |      | 页面的初始数据                                               |
| options                                                      | Object       |        |      | 页面的组件选项，同 [`Component` 构造器](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Component.html) 中的 `options` ，需要基础库版本 [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| [behaviors](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/behaviors.html) | String Array |        |      | 类似于mixins和traits的组件间代码复用机制，参见 [behaviors](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/behaviors.html)，需要基础库版本 [2.9.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| [onLoad](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onLoad-Object-query) | function     |        |      | 生命周期回调—监听页面加载                                    |
| [onShow](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onShow) | function     |        |      | 生命周期回调—监听页面显示                                    |
| [onReady](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onReady) | function     |        |      | 生命周期回调—监听页面初次渲染完成                            |
| [onHide](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onHide) | function     |        |      | 生命周期回调—监听页面隐藏                                    |
| [onUnload](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onUnload) | function     |        |      | 生命周期回调—监听页面卸载                                    |
| [onRouteDone](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onRouteDone) | function     |        |      | 生命周期回调—监听路由动画完成                                |
| [onPullDownRefresh](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onPullDownRefresh) | function     |        |      | 监听用户下拉动作                                             |
| [onReachBottom](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onReachBottom) | function     |        |      | 页面上拉触底事件的处理函数                                   |
| [onShareAppMessage](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onShareAppMessage-Object-object) | function     |        |      | 用户点击右上角转发                                           |
| [onShareTimeline](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onShareTimeline) | function     |        |      | 用户点击右上角转发到朋友圈                                   |
| [onAddToFavorites](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onAddToFavorites-Object-object) | function     |        |      | 用户点击右上角收藏                                           |
| [onPageScroll](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onPageScroll-Object-object) | function     |        |      | 页面滚动触发事件的处理函数                                   |
| [onResize](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onResize-Object-object) | function     |        |      | 页面尺寸改变时触发，详见 [响应显示区域变化](https://developers.weixin.qq.com/miniprogram/dev/framework/view/resizable.html#在手机上启用屏幕旋转支持) |
| [onTabItemTap](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onTabItemTap-Object-object) | function     |        |      | 当前是 tab 页时，点击 tab 时触发                             |
| [onSaveExitState](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onSaveExitState) | function     |        |      | 页面销毁前保留状态回调                                       |
| 其他                                                         | any          |        |      | 开发者可以添加任意的函数或数据到 `Object` 参数中，在页面的函数中用 `this` 可以访问。**这部分属性会在页面实例创建时进行一次深拷贝**。 |

**示例代码**

```js
//index.js
Page({
  data: {
    text: "This is page data."
  },
  onLoad: function(options) {
    // Do some initialize when page load.
  },
  onShow: function() {
    // Do something when page show.
  },
  onReady: function() {
    // Do something when page ready.
  },
  onHide: function() {
    // Do something when page hide.
  },
  onUnload: function() {
    // Do something when page close.
  },
  onPullDownRefresh: function() {
    // Do something when pull down.
  },
  onReachBottom: function() {
    // Do something when page reach bottom.
  },
  onShareAppMessage: function () {
    // return custom share data when user share.
  },
  onPageScroll: function() {
    // Do something when page scroll
  },
  onResize: function() {
    // Do something when page resize
  },
  onTabItemTap(item) {
    console.log(item.index)
    console.log(item.pagePath)
    console.log(item.text)
  },
  // Event handler.
  viewTap: function() {
    this.setData({
      text: 'Set some data for updating view.'
    }, function() {
      // this is setData callback
    })
  },
  customData: {
    hi: 'MINA'
  }
})
```

#### data

`data` 是页面第一次渲染使用的**初始数据**。

页面加载时，`data` 将会以`JSON`字符串的形式由逻辑层传至渲染层，因此`data`中的数据必须是可以转成`JSON`的类型：字符串，数字，布尔值，对象，数组。

渲染层可以通过 [WXML](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/index.html) 对数据进行绑定。

**示例代码：**

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/2PeBsKmn6EZ9)

```html
<view>{{text}}</view>
<view>{{array[0].msg}}</view>
Page({
  data: {
    text: 'init data',
    array: [{msg: '1'}, {msg: '2'}]
  }
})
```