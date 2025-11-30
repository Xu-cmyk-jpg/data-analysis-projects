import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
# analyze_sales.py
import pandas as pd
import matplotlib.pyplot as plt
# 1. 读取数据
df = pd.read_excel('电商平台销售特征分析与策略优化-数据.xlsx')
print("数据前5行：")
print(df.head())
print(f"\n数据形状：{df.shape}")
print("\n" + "="*60 + "\n")
# 2. 基本统计
print("总销售额：", df['销售额'].sum())
print("总利润：", df['利润'].sum())
print("平均订单金额：", df['销售额'].mean().round(2))
print("订单数量：", len(df))
print("\n" + "="*60 + "\n")
# 3. 各品类利润排名
profit_by_category = df.groupby('商品品类')['利润'].sum().sort_values(ascending=False)
print("各品类利润排名：")
print(profit_by_category)
# 4. 画图
plt.figure(figsize=(10, 6))
profit_by_category.plot(kind='bar', color='skyblue')
plt.title('各商品品类利润对比')
plt.ylabel('利润（元）')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("profit_chart.png")
# 保存图片到文件