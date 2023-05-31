# 组件-视图容器

# grid-view

> 相关 api: [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)、[Skyline 迁移起步](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/migration.html)

## 功能描述

Skyline 下网格布局容器。基础库版本 2.30.4 起提供 WebView 兼容实现。

## 属性说明

> Skyline 仅列出与 WebView 属性的差异，未列出的属性与 WebView 一致。

WebView Skyline



|      | 属性                                                         | 类型   | 默认值  | 必填 | 说明               |
| :--- | :----------------------------------------------------------- | :----- | :------ | :--- | :----------------- |
|      | type                                                         | string | aligned | 是   | 布局方式           |
|      | aligned每行高度由同一行中最大高度子节点决定                                     masonry瀑布流，根据子元素高度自动布局 |        |         |      |                    |
|      | cross-axis-count                                             | number | 2       | 否   | 交叉轴元素数量     |
|      | max-cross-axis-extent                                        | number | 0       | 否   | 交叉轴元素最大范围 |
|      | main-axis-gap                                                | number | 0       | 否   | 主轴方向间隔       |
|      | cross-axis-gap                                               | number | 0       | 否   | 交叉轴方向间隔     |

**组件差异**
\1. 仅支持作为 `scroll-view` 自定义模式下的直接子节点 2. 按需渲染节点，比 WebView 兼容实现具备更好的性能。

