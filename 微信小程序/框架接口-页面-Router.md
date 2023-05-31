# 框架接口

## 页面

### Router

页面路由器对象。可以通过 `this.pageRouter` 或 `this.router` 获得当前页面或自定义组件的路由器对象。

#### 路由的相对路径

页面路由器有 `switchTab` `reLaunch` `redirectTo` `navigateTo` `navigateBack` 五个方法，与 wx 对象向同名的五个方法 [`switchTab`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.switchTab.html) [`reLaunch`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.reLaunch.html) [`redirectTo`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.redirectTo.html) [`navigateTo`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html) [`navigateBack`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateBack.html) 功能相同；唯一的区别是，页面路由器中的方法调用时，相对路径永远相对于 `this` 指代的页面或自定义组件。

例如，对于下面这段示例代码：

```js
// index/index.js
Page({
  wxNavAction: function () {
    wx.navigateTo({
      url: './new-page'
    })
  },
  routerNavAction: function () {
    this.pageRouter.navigateTo({
      url: './new-page'
    })
  }
})
```

页面 `index/index` 的 js 代码如上所示。如果此时已经跳转到了一个新页面 `pack/index` ，然后才调用到上面的 `wxNavAction` 方法，跳转的新页面路径将是 `pack/new-page` ；而如果调用的是 `routerNavAction` 方法，跳转的新页面路径仍然是 `index/new-page` 。

换而言之， `this.pageRouter` 获得的路由器对象具有更好的基路径稳定性。通常情况下，使用 `this.pageRouter.navigateTo` 代替 `wx.navigateTo` 是更优的。

#### 相对于自定义组件路径的路由

`this.pageRouter` 和 `this.router` 在页面中将获得同样的页面路由器对象。

但如果在自定义组件中调用， `this.pageRouter` 将相对于自定义组件所在的页面来进行路由跳转，而 `this.router` 相对于自定义组件自身的路径。