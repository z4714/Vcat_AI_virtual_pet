# 组件-视图容器



## match-media

> 基础库 2.11.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

## 功能描述

media query 匹配检测节点。可以指定一组 media query 规则，满足时，这个节点才会被展示。

通过这个节点可以实现“页面宽高在某个范围时才展示某个区域”这样的效果。

## 属性说明

| 属性        | 类型   | 默认值 | 必填 | 说明                                    | 最低版本                                                     |
| :---------- | :----- | :----- | :--- | :-------------------------------------- | :----------------------------------------------------------- |
| min-width   | number |        | 否   | 页面最小宽度（ px 为单位）              | [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| max-width   | number |        | 否   | 页面最大宽度（ px 为单位）              | [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| width       | number |        | 否   | 页面宽度（ px 为单位）                  | [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| min-height  | number |        | 否   | 页面最小高度（ px 为单位）              | [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| max-height  | number |        | 否   | 页面最大高度（ px 为单位）              | [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| height      | number |        | 否   | 页面高度（ px 为单位）                  | [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| orientation | string |        | 否   | 屏幕方向（ `landscape` 或 `portrait` ） | [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

```html
<match-media min-width="300" max-width="600">
  <view>当页面宽度在 300 ~ 500 px 之间时展示这里</view>
</match-media>

<match-media min-height="400" orientation="landscape">
  <view>当页面高度不小于 400 px 且屏幕方向为纵向时展示这里</view>
</match-media>
```