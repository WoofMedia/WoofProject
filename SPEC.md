Overview
--
本文档指定了Woof Project中，所使用到的数据储存标准以及 API 交互标准

在本项目中，使用到了这些数据格式类型：
1. Binary
2. Json
3. Key value

Metadata File
--
元数据以 Binary 文件形式存在，被储存在与其所描述的多媒体文件同一目录下

其文件名为多媒体文件的 base name + ".wom"，如
```
flower.2004.x264.mp4
flower.2004.x264.wom
```

wom 文件所包含的 binary field，按实际储存顺序如下：
```
title
description
cover_img_data
poster_img_data
category
rank
score
session
episode
```
