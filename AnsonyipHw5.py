import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales.csv')
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='green', width=0.5)
plt.title('Bar Chart of Ice-cream Sales')
plt.xlabel('Month')
plt.ylabel('Sales (in thousand dollars)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
