# 框架接口

## 页面

### page

#### 生命周期回调函数

**onLoad(Object query)**

页面加载时触发。一个页面只会调用一次，可以在 onLoad 的参数中获取打开当前页面路径中的参数。

**参数：**

| 名称  | 类型   | 说明                     |
| :---- | :----- | :----------------------- |
| query | Object | 打开当前页面路径中的参数 |

**onShow()**

页面显示/切入前台时触发。

**onReady()**

页面初次渲染完成时触发。一个页面只会调用一次，代表页面已经准备妥当，可以和视图层进行交互。

注意：对界面内容进行设置的 API 如[wx.setNavigationBarTitle](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.setNavigationBarTitle.html)，请在`onReady`之后进行。详见[生命周期](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page-life-cycle.html)

**onHide()**

页面隐藏/切入后台时触发。 如 [wx.navigateTo](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html) 或底部 `tab` 切换到其他页面，小程序切入后台等。

**onUnload()**

页面卸载时触发。如[wx.redirectTo](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.redirectTo.html)或[wx.navigateBack](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateBack.html)到其他页面时。

**onRouteDone()**

路由动画完成时触发。如 [wx.navigateTo](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html) 页面完全推入后 或 [wx.navigateBack](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateBack.html) 页面完全恢复时。

## 