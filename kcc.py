

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_excel("Kisan Call Centre.xlsx")


# In[4]:


print(df.info())


# In[18]:


df = df.drop_duplicates()


# In[19]:


df.shape


# In[20]:


df = df.dropna()


# In[7]:


df


# In[8]:


df['homestatecode'] = df['homestatecode'].astype(int)
df['salestatecode'] = df['salestatecode'].astype(int)
df['month'] = df['month'].astype(int)
df['year'] = df['year'].astype(int)
df['txn_count'] = df['txn_count'].astype(int)


# In[9]:


df


# In[10]:


region_mapping = {
    'JAMMU AND KASHMIR': 'North', 'UTTARAKHAND': 'North', 'HARYANA': 'North',
    'DELHI': 'North', 'UTTAR PRADESH': 'North', 'BIHAR': 'East'
}
df['region'] = df['salestatename'].map(region_mapping)


# In[11]:


df['month'] = pd.to_datetime(df['month'], format='%m').dt.strftime('%B')


# In[12]:


df['txn_count'].fillna(df['txn_count'].mean(), inplace=True)


# In[13]:


df.to_csv("updated_data.csv", index=False)

print("Dataset updated! File saved as 'updated_data.csv'.")


# In[14]:


df


# In[15]:


print(df.info())


# In[16]:


plt.figure(figsize=(10, 5))
plt.bar(df['salestatename'], df['txn_count'], color='skyblue')
plt.xticks(rotation=90)
plt.xlabel("Sale State")
plt.ylabel("Transaction Count")
plt.title("Transaction Count per Sale State")
plt.show()


# In[17]:


plt.figure(figsize=(10, 5))
plt.plot(df['month'], df['txn_count'], marker='o', linestyle='-', color='b')
plt.xlabel("Month")
plt.ylabel("Transaction Count")
plt.title("Transaction Trend Over Time")
plt.show()


# In[18]:


plt.figure(figsize=(10, 5))
plt.scatter(df['homestatename'], df['txn_count'], color='r', alpha=0.5)
plt.xticks(rotation=90)
plt.xlabel("Home State")
plt.ylabel("Transaction Count")
plt.title("Home State vs Transaction Count")
plt.show()


# In[19]:


plt.figure(figsize=(8, 5))
plt.hist(df['txn_count'], bins=20, color='g', alpha=0.7)
plt.xlabel("Transaction Count")
plt.ylabel("Frequency")
plt.title("Distribution of Transactions")
plt.show()


# In[20]:


plt.figure(figsize=(8, 8))
plt.pie(df.groupby('salestatename')['txn_count'].sum(),labels=df['salestatename'].unique(), autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title("Transaction Share by Sale State")
plt.show()


# In[21]:


plt.figure(figsize=(10, 5))
sns.boxplot(x='salestatename', y='txn_count', data=df)
plt.xticks(rotation=90)
plt.xlabel("Sale State")
plt.ylabel("Transaction Count")
plt.title("Transaction Count Distribution per Sale State")
plt.show()


# In[22]:


sns.pairplot(df, vars=['homestatecode', 'salestatecode', 'txn_count'])
plt.show()


# In[23]:


plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt='.2f')
plt.title("Feature Correlation Heatmap")
plt.show()


# In[24]:


plt.figure(figsize=(10, 5))
sns.violinplot(x='homestatename', y='txn_count', data=df)
plt.xticks(rotation=90)
plt.xlabel("Home State")
plt.ylabel("Transaction Count")
plt.title("Transaction Distribution per Home State")
plt.show()


# In[25]:


plt.figure(figsize=(10, 5))
sns.boxplot(x='salestatename', y='txn_count', data=df)
plt.xticks(rotation=90)
plt.xlabel("Sale State")
plt.ylabel("Transaction Count")
plt.title("Transaction Count Distribution per Sale State")
plt.show()


# In[26]:


plt.xticks(rotation=90)
plt.xlabel("State Name")
plt.ylabel("Transaction Count")
plt.title("Transaction Count Bubble Chart by State")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

