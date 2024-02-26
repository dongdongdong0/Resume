import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Read the data into a pandas dataframe and display the head and tail
df = pd.read_csv('/Users/wuyuzheng/Documents/UC/DATA601/Building Data.csv')
#print(df.head(4))
#print(df.tail(4))
#print(df.dtypes[2:])
# convert the types pf value
df = df.replace(' ', np.nan)

for col in df.columns[2:]:
    df[col]=df[col].str.replace(',', '')
    df[col]=df[col].astype(float)

#df['year']=df['Date'].apply(lambda x: x.split('-')[0])
#df['month']=df['Date'].apply(lambda x: x.split('-')[1])
#df['day']=df['Date'].apply(lambda x: x.split('-')[2])
df['Date']=pd.to_datetime(df['Date'])
df['year']=df['Date'].dt.year
df['month']=df['Date'].dt.month
df['day']=df['Date'].dt.day

#del df['Date']

df = df.set_index(['year', 'month', 'day', 'Building'])
print(df.head(10))

new_df1 = df.loc[2019]
#electricity_usage = new_df1.groupby(by='Building')['Electricity (kWh)'].sum()
#building = electricity_usage.index.to_numpy()
#usage = electricity_usage.to_numpy()
#plt.figure()
#plt.bar(building, usage)
#plt.xlabel('Building')
#plt.ylabel('electricity usage')
#plt.title('Electricity usage of per building in 2019')
#plt.show()
compute_list = [col for col in new_df1.columns.to_list() if 'kWh' in col]
#energe_usage = new_df1.groupby(by='Building')[compute_list].sum()
#energe_usage_per = energe_usage.sum(axis=1)
#building = energe_usage_per.index.to_numpy()
#usage = energe_usage_per.to_numpy()
#plt.figure()
#plt.bar(building, usage)
#plt.xlabel('Building')
#plt.ylabel('Energy usage')
#plt.title('Energy usage of per building in 2019')
#plt.show()

#daily_usage = new_df1.groupby(by='month')[compute_list].mean()
#daily_usage_per = daily_usage.sum(axis=1)

#usage1=daily_usage_per.to_numpy()

#plt.boxplot(usage1)
#plt.title('Boxplot of daily energy usage per month')
#plt.ylabel('values')
#plt.show()

#df['Date'] = pd.to_datetime(df)
#print(df.head(10))



     
    
  
    
#df[col].astype(float)

start_date1 = '2020-01-11'
end_date1 = '2020-03-10'
start_date2 = '2020-03-11'
end_date2 = '2020-05-11'
df1 = df.loc[(df['Date'] >= start_date1)& (df['Date']<=end_date1)]
df2 = df.loc[(df['Date'] >= start_date2)& (df['Date']<=end_date2)]



water_usage_before = df1.groupby(by='Building')['Domestic Cold Water (m3)'].mean()
#water_usage_before_per = water_usage_before.sum(axis=1)
water_usage_after = df2.groupby(by='Building')['Domestic Cold Water (m3)'].mean()
#water_usage_after_per = water_usage_after.sum(axis=1)

building = water_usage_after.index.to_numpy()
usage_before = water_usage_before.to_numpy()
usage_after = water_usage_after.to_numpy()
plt.figure()
plt.plot(building,usage_before, label='Before pandemic')
plt.plot(building,usage_after, label='After pandemic')
plt.title('Average daily water usage of different buildings before and after pandemic' )
plt.xlabel('building')
plt.ylabel('Average daily water usage')
plt.legend()


plt.show()
    
            






