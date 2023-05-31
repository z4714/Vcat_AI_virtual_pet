# 组件-视图容器



# movable-view

## 功能描述

可移动的视图容器，在页面中可以拖拽滑动。[movable-view](https://developers.weixin.qq.com/miniprogram/dev/component/movable-view.html)必须在 [movable-area](https://developers.weixin.qq.com/miniprogram/dev/component/movable-area.html) 组件中，并且必须是直接子节点，否则不能移动。

## 属性说明

| 属性          | 类型          | 默认值 | 必填 | 说明                                                         | 最低版本                                                     |
| :------------ | :------------ | :----- | :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| direction     | string        | none   | 否   | movable-view的移动方向，属性值有all、vertical、horizontal、none | [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| inertia       | boolean       | false  | 否   | movable-view是否带有惯性                                     | [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| out-of-bounds | boolean       | false  | 否   | 超过可移动区域后，movable-view是否还可以移动                 | [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| x             | number/string |        | 否   | 定义x轴方向的偏移，如果x的值不在可移动范围内，会自动移动到可移动范围；改变x的值会触发动画；单位支持px（默认）、rpx； | [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| y             | number/string |        | 否   | 定义y轴方向的偏移，如果y的值不在可移动范围内，会自动移动到可移动范围；改变y的值会触发动画；单位支持px（默认）、rpx； | [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| damping       | number        | 20     | 否   | 阻尼系数，用于控制x或y改变时的动画和过界回弹的动画，值越大移动越快 | [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| friction      | number        | 2      | 否   | 摩擦系数，用于控制惯性滑动的动画，值越大摩擦力越大，滑动越快停止；必须大于0，否则会被设置成默认值 | [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| disabled      | boolean       | false  | 否   | 是否禁用                                                     | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| scale         | boolean       | false  | 否   | 是否支持双指缩放，默认缩放手势生效区域是在movable-view内     | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| scale-min     | number        | 0.1    | 否   | 定义缩放倍数最小值                                           | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| scale-max     | number        | 10     | 否   | 定义缩放倍数最大值                                           | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| scale-value   | number        | 1      | 否   | 定义缩放倍数，取值范围为 0.1 - 10                            | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| animation     | boolean       | true   | 否   | 是否使用动画                                                 | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindchange    | eventhandle   |        | 否   | 拖动过程中触发的事件，event.detail = {x, y, source}          | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindscale     | eventhandle   |        | 否   | 缩放过程中触发的事件，event.detail = {x, y, scale}，x和y字段在[2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)之后支持 | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| htouchmove    | eventhandle   |        | 否   | 初次手指触摸后移动为横向的移动时触发，如果catch此事件，则意味着touchmove事件也被catch | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| vtouchmove    | eventhandle   |        | 否   | 初次手指触摸后移动为纵向的移动时触发，如果catch此事件，则意味着touchmove事件也被catch | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## `bindchange` 返回的 `source` 表示产生移动的原因

| 值                  | 说明                 |
| :------------------ | :------------------- |
| touch               | 拖动                 |
| touch-out-of-bounds | 超出移动范围         |
| out-of-bounds       | 超出移动范围后的回弹 |
| friction            | 惯性                 |
| 空字符串            | setData              |

## Bug & Tip

1. `tip`: movable-view 必须设置width和height属性，不设置默认为10px
2. `tip`: movable-view 默认为绝对定位，top和left属性为0px
3. `tip`: 若当前组件所在的页面或全局开启了 `enablePassiveEvent` 配置项，该内置组件可能会出现非预期表现（详情参考 [enablePassiveEvent 文档](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app)）