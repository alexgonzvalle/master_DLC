import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('obesity_cps.csv')
_df = df[['Streaming', 'Obesity']]
correlation_matrix = _df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
