#!python3
# -*- coding: UTF-8 -*-
#我们要制作一个柱状图，需要先引入Bar
from pyecharts import Bar
 
#创建图表实例，并给图表添加标题和副标题
bar = Bar("使用Python制作柱状图", "HackWork技术工坊交互图表实战")
 
#选择图表的主题样式
bar.use_theme("vintage")
 
#图例的名称
name="服装"
 
#x轴坐标的数据，注意是一个列表List类型，注意这里有6个数据
x_axis=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
 
#y轴坐标的数据，注意是也一个列表List类型，注意这里也有6个数据
y_axis=[5, 20, 36, 10, 75, 90]
 
# 给图表
bar.add(name,x_axis,y_axis)
 
# 生成本地 HTML 文件
bar.render()