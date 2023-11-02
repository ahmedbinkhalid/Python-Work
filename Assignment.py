import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


# Load the Excel file
df = pd.read_csv('E:\Semster 7\Data Science\DataSet\sales_data.csv')


# Display the first few rows of the data
print(df.head())

# Check the data types of each column
print(df.dtypes)

# Get a summary of the dataset
print(df.describe())

# Check for any missing values
print(df.isnull().sum())

# Check for any duplicates
print(df.duplicated().sum())

# Check for the shape of the dataset
print(df.shape)
# Check for missing values
print(df.isnull().sum())



# Calculate z-scores for 'price' and 'quantity'
z_scores_price = stats.zscore(df['price'])
z_scores_quantity = stats.zscore(df['quantity'])

# Define a threshold for the z-scores
threshold = 5

# Filter the data to exclude outliers
data = df[(abs(z_scores_price) < threshold) & (abs(z_scores_quantity) < threshold)]

# Check the shape of the data after removing outliers
print(data.shape)


# Box plot for 'quantity'
plt.figure(figsize=(6, 6))
sns.boxplot(y=df['quantity'])
plt.title("Box plot for Quantity")
plt.show()

# Box plot for 'price'
plt.figure(figsize=(6, 6))
sns.boxplot(y=df['price'])
plt.title("Box plot for Price")
plt.show()
# Compute basic statistics for the dataset
mean_price = data['price'].mean()
median_price = data['price'].median()
mode_price = data['price'].mode()[0]
std_price = data['price'].std()

mean_quantity = data['quantity'].mean()
median_quantity = data['quantity'].median()
mode_quantity = data['quantity'].mode()[0]
std_quantity = data['quantity'].std()

# Display the computed statistics
print("Price Statistics:")
print(f"Mean: {mean_price}")
print(f"Median: {median_price}")
print(f"Mode: {mode_price}")
print(f"Standard Deviation: {std_price}")
print("\n")
print("Quantity Statistics:")
print(f"Mean: {mean_quantity}")
print(f"Median: {median_quantity}")
print(f"Mode: {mode_quantity}")
print(f"Standard Deviation: {std_quantity}")

# Histogram for 'price'
plt.figure(figsize=(8, 6))
sns.histplot(data['price'], kde=True, color='skyblue')
plt.title('Histogram of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Bar chart for 'category' counts
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='category', palette='viridis')
plt.title('Bar Chart of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()



