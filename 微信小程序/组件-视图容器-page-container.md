# 组件-视图容器



# page-container



## 功能描述

页面容器。

小程序如果在页面内进行复杂的界面设计（如在页面内弹出半屏的弹窗、在页面内加载一个全屏的子页面等），用户进行返回操作会直接离开当前页面，不符合用户预期，预期应为关闭当前弹出的组件。 为此提供“假页”容器组件，效果类似于 `popup` 弹出层，页面内存在该容器时，当用户进行返回操作，关闭该容器不关闭页面。返回操作包括三种情形，右滑手势、安卓物理返回键和调用 `navigateBack` 接口。

## 属性说明

| 属性                | 类型        | 默认值 | 必填 | 说明                                               | 最低版本                                                     |
| :------------------ | :---------- | :----- | :--- | :------------------------------------------------- | :----------------------------------------------------------- |
| show                | boolean     | false  | 否   | 是否显示容器组件                                   | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| duration            | number      | 300    | 否   | 动画时长，单位毫秒                                 | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| z-index             | number      | 100    | 否   | z-index 层级                                       | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| overlay             | boolean     | true   | 否   | 是否显示遮罩层                                     | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| position            | string      | bottom | 否   | 弹出位置，可选值为 `top` `bottom` `right` `center` | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| round               | boolean     | false  | 否   | 是否显示圆角                                       | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| close-on-slide-down | boolean     | false  | 否   | 是否在下滑一段距离后关闭                           | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| overlay-style       | string      |        | 否   | 自定义遮罩层样式                                   | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| custom-style        | string      |        | 否   | 自定义弹出层样式                                   | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bind:beforeenter    | eventhandle |        | 否   | 进入前触发                                         | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bind:enter          | eventhandle |        | 否   | 进入中触发                                         | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bind:afterenter     | eventhandle |        | 否   | 进入后触发                                         | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bind:beforeleave    | eventhandle |        | 否   | 离开前触发                                         | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bind:leave          | eventhandle |        | 否   | 离开中触发                                         | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bind:afterleave     | eventhandle |        | 否   | 离开后触发                                         | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bind:clickoverlay   | eventhandle |        | 否   | 点击遮罩层时触发                                   | [2.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## Bug & Tip

1. `tip`: 当前页面最多只有 `1` 个容器，若已存在容器的情况下，无法增加新的容器
2. `tip`: `wx.navigateBack` 无法在页面栈顶调用，此时没有上一级页面