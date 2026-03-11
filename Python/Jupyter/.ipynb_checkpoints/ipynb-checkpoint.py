import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from seaborn
iris = sns.load_dataset('iris')

# (i) Histogram
plt.figure(figsize=(10, 6))
sns.histplot(iris['sepal_length'], kde=True)
plt.title('Histogram of Sepal Length')
plt.show()

# (ii) Bar Graph
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='sepal_length', data=iris)
plt.title('Bar Graph of Sepal Length by Species')
plt.show()

# (iii) Pie Chart
plt.figure(figsize=(8, 8))
iris['species'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Pie Chart of Species Distribution')
plt.ylabel('')
plt.show()

# (iv) Box and Whisker Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal_length', data=iris)
plt.title('Box and Whisker Plot of Sepal Length by Species')
plt.show()

# (v) Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.show()