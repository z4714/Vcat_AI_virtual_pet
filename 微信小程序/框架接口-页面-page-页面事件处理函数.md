# 框架接口

## 页面

### page

**页面事件处理函数**

**onPullDownRefresh()**

监听用户下拉刷新事件。

- 需要在`app.json`的[`window`](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app.html#window)选项中或[页面配置](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/page.html)中开启`enablePullDownRefresh`。
- 可以通过[wx.startPullDownRefresh](https://developers.weixin.qq.com/miniprogram/dev/api/ui/pull-down-refresh/wx.startPullDownRefresh.html)触发下拉刷新，调用后触发下拉刷新动画，效果与用户手动下拉刷新一致。
- 当处理完数据刷新后，[wx.stopPullDownRefresh](https://developers.weixin.qq.com/miniprogram/dev/api/ui/pull-down-refresh/wx.stopPullDownRefresh.html)可以停止当前页面的下拉刷新。

**onReachBottom()**

监听用户上拉触底事件。

- 可以在`app.json`的[`window`](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app.html#window)选项中或[页面配置](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/page.html)中设置触发距离`onReachBottomDistance`。
- 在触发距离内滑动期间，本事件只会被触发一次。

**onPageScroll(Object object)**

监听用户滑动页面事件。

**参数 Object object**:

| 属性      | 类型   | 说明                                 |
| :-------- | :----- | :----------------------------------- |
| scrollTop | Number | 页面在垂直方向已滚动的距离（单位px） |

**注意：请只在需要的时候才在 page 中定义此方法，不要定义空方法。以减少不必要的事件派发对渲染层-逻辑层通信的影响。** **注意：请避免在 onPageScroll 中过于频繁的执行 `setData` 等引起[逻辑层-渲染层通信](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/tips.html)的操作。尤其是每次传输大量数据，会影响通信耗时。**

**onAddToFavorites(Object object)**

监听用户点击右上角菜单“收藏”按钮的行为，并自定义收藏内容。

**参数 Object object**:

| 参数       | 类型   | 说明                                                         |
| :--------- | :----- | :----------------------------------------------------------- |
| webViewUrl | String | 页面中包含[web-view](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html)组件时，返回当前[web-view](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html)的url |

此事件处理函数需要 return 一个 Object，用于自定义收藏内容：

| 字段     | 说明                              | 默认值             |
| :------- | :-------------------------------- | :----------------- |
| title    | 自定义标题                        | 页面标题或账号名称 |
| imageUrl | 自定义图片，显示图片长宽比为 1：1 | 页面截图           |
| query    | 自定义query字段                   | 当前页面的query    |

**示例代码**

```javascript
Page({
  onAddToFavorites(res) {
    // webview 页面返回 webViewUrl
    console.log('webViewUrl: ', res.webViewUrl)
    return {
      title: '自定义标题',
      imageUrl: 'http://demo.png',
      query: 'name=xxx&age=xxx',
    }
  }
})
```

**onShareAppMessage(Object object)**

监听用户点击页面内转发按钮（[button](https://developers.weixin.qq.com/miniprogram/dev/component/button.html) 组件 `open-type="share"`）或右上角菜单“转发”按钮的行为，并自定义转发内容。

**注意：只有定义了此事件处理函数，右上角菜单才会显示“转发”按钮**

**参数 Object object**:

| 参数       | 类型   | 说明                                                         | 最低版本                                                     |
| :--------- | :----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| from       | String | 转发事件来源。 `button`：页面内转发按钮； `menu`：右上角转发菜单 | [1.2.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| target     | Object | 如果 `from` 值是 `button`，则 `target` 是触发这次转发事件的 `button`，否则为 `undefined` | [1.2.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| webViewUrl | String | 页面中包含[web-view](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html)组件时，返回当前[web-view](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html)的url | [1.6.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

此事件处理函数需要 return 一个 Object，用于自定义转发内容，返回内容如下：

| 字段     | 说明                                                         | 默认值                                    | 最低版本                                                     |
| :------- | :----------------------------------------------------------- | :---------------------------------------- | :----------------------------------------------------------- |
| title    | 转发标题                                                     | 当前小程序名称                            |                                                              |
| path     | 转发路径                                                     | 当前页面 path ，必须是以 / 开头的完整路径 |                                                              |
| imageUrl | 自定义图片路径，可以是本地文件路径、代码包文件路径或者网络图片路径。支持PNG及JPG。显示图片长宽比是 5:4。 | 使用默认截图                              | [1.5.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| promise  | 如果该参数存在，则以 resolve 结果为准，如果三秒内不 resolve，分享会使用上面传入的默认参数 |                                           | [2.12.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

**示例代码**

```javascript
Page({
  onShareAppMessage() {
    const promise = new Promise(resolve => {
      setTimeout(() => {
        resolve({
          title: '自定义转发标题'
        })
      }, 2000)
    })
    return {
      title: '自定义转发标题',
      path: '/page/user?id=123',
      promise 
    }
  }
})
```

**onShareTimeline()**

监听右上角菜单“分享到朋友圈”按钮的行为，并自定义分享内容。

**注意：只有定义了此事件处理函数，右上角菜单才会显示“分享到朋友圈”按钮**

**自定义转发内容**

事件处理函数返回一个 Object，用于自定义分享内容，不支持自定义页面路径，返回内容如下：

| 字段     | 说明                                                         | 默认值                 | 最低版本 |
| :------- | :----------------------------------------------------------- | :--------------------- | :------- |
| title    | 自定义标题，即朋友圈列表页上显示的标题                       | 当前小程序名称         |          |
| query    | 自定义页面路径中携带的参数，如 path?a=1&b=2 的 “?” 后面部分  | 当前页面路径携带的参数 |          |
| imageUrl | 自定义图片路径，可以是本地文件或者网络图片。支持 PNG 及 JPG，显示图片长宽比是 1:1。 | 默认使用小程序 Logo    |          |

**onResize(Object object)**

小程序屏幕旋转时触发。详见 [响应显示区域变化](https://developers.weixin.qq.com/miniprogram/dev/framework/view/resizable.html#在手机上启用屏幕旋转支持)

**onTabItemTap(Object object)**

点击 tab 时触发

**Object 参数说明：**

| 参数     | 类型   | 说明                         | 最低版本                                                     |
| :------- | :----- | :--------------------------- | :----------------------------------------------------------- |
| index    | String | 被点击tabItem的序号，从0开始 | [1.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| pagePath | String | 被点击tabItem的页面路径      | [1.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| text     | String | 被点击tabItem的按钮文字      | [1.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

**示例代码：**

```js
Page({
  onTabItemTap(item) {
    console.log(item.index)
    console.log(item.pagePath)
    console.log(item.text)
  }
})
```

**onSaveExitState()**

每当小程序可能被销毁之前，页面回调函数 `onSaveExitState` 会被调用，可以进行[退出状态](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/operating-mechanism.html#_4-退出状态)的保存。