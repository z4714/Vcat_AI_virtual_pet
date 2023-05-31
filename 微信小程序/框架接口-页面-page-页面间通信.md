# 框架接口

## 页面

### page

#### 页面间通信

如果一个页面由另一个页面通过 [`wx.navigateTo`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html) 打开，这两个页面间将建立一条数据通道：

- 被打开的页面可以通过 `this.getOpenerEventChannel()` 方法来获得一个 `EventChannel` 对象；
- `wx.navigateTo` 的 `success` 回调中也包含一个 `EventChannel` 对象。

这两个 `EventChannel` 对象间可以使用 `emit` 和 `on` 方法相互发送、监听事件。