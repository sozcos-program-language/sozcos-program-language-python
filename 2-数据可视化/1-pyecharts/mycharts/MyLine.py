from pyecharts.charts import Line

# 得到折线图对象
line = Line()
# 绘制x轴
line.add_xaxis(
    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
)
# 绘制y轴
line.add_yaxis("最高气温", [1, 2, 3, 4, 5])

# 生成图表
line.render("myline.html")
