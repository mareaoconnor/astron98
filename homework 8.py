#!/usr/bin/env python
# coding: utf-8

# In[47]:


#part a
import pandas as pd

df_data = pd.read_csv("GlobalLandTemperaturesByStateee.csv")

df_filtered = df_data[['dt', 'AverageTemperature', 'State']]

print(df_filtered)


# In[48]:


df_filtered['dt'] = pd.to_datetime(df_filtered['dt'])
df_filtered = df_filtered[df_filtered['dt'].dt.year > 2000]
print(df_filtered)


# In[49]:


df_filtered = df_filtered[df_filtered['State'].isin(['Wyoming', 'Nebraska', 'South Dakota'])]


print(df_filtered)


# In[50]:


df_averagetemp = df_filtered.groupby('dt')['AverageTemperature'].mean().reset_index()

df_averagetemp = df_averagetemp.rename(columns={'temperature': 'average_temperature'})

print(df_averagetemp)


# In[51]:


import matplotlib.pyplot as plt

plt.plot(df_averagetemp['dt'], df_averagetemp['AverageTemperature'])
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Temperature Over Time for Wyoming, Nebraska, and South Dakota')
pl.show()


# In[52]:


df_averagetemp['dt'] = pd.to_datetime(df_averagetemp['dt'])
df_averagetemp['Year'] = df_averagetemp['dt'].dt.year
df_averagetemp['Month'] = df_averagetemp['dt'].dt.month
df_averagetemp['Day'] = df_averagetemp['dt'].dt.day
print(df_averagetemp)


# In[54]:


import numpy as np
amplitude = (df_averagetemp['AverageTemperature'].max() - df_averagetemp['AverageTemperature'].min())/2
frequency = 2 / np.pi
phaseshift = 0
verticalshift = df_averagetemp['AverageTemperature'].mean()

initial_guess = [amplitude, frequency, phaseshift, verticalshift]
print(initial_guess)


# In[55]:


from scipy.optimize import curve_fit

def sinusoidal_model(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

df_averagetemp['date_numeric'] = (df_averagetemp['dt'] - df_averagetemp['dt'].min()).dt.days

params, covariance = curve_fit(sinusoidal_model, df_averagetemp['date_numeric'], df_averagetemp['AverageTemperature'], p0 = initial_guess)

print("Fitted parameters:", params)
print("Covariance matrix:", covariance)


# In[63]:


x_values = np.linspace(df_averagetemp['date_numeric'].min(), df_averagetemp['date_numeric'].max())

plt.plot(df_averagetemp['date_numeric'], df_averagetemp['AverageTemperature'], color='red', label='Original Data')
plt.plot(x_values, sinusoidal_model(x_values, * params), label = 'Fitted Curve', color = 'blue')

plt.xlabel('Date (days since start)')
plt.ylabel('Average Temperature (°C)')
plt.title('Fitted Curve vs Original Data')
plt.legend()

plt.show()


# In[68]:


errors = np.sqrt(np.diag(covariance))

for i, error in enumerate(errors):
    print(f"Parameter {i+1}'s error: {error}")
    


# In[70]:


for i, (param,error) in enumerate(zip(params, errors)):
    print(f"Parameter {i+1}: {param:.2f} +/- {error:.2f}")
    
print(f"Final equation: y = {params[0]:.2f} * sin({params[1]:.2f} * x + {params[2]:.2f}) + {params[3]:.2f}")


# In[93]:


from astropy.table import Table

data_table = Table.read('global_SF6_MMM.csv', format='ascii')
df = data_table.to_pandas()
df = df[['SF6ottoyr', 'SF6ottoGLm', 'SF6ottoGLsd']]


# In[94]:


plt.errorbar(df['SF6ottoyr'], df['SF6ottoGLm'], yerr=df['SF6ottoGLsd'], fmt='o', markersize=3)
plt.xlabel('Date')
plt.ylabel('Global Mean Concentration')
plt.title('Global Mean Concentration Over Time with Error Bars')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[95]:


def linear_model(x, m, b):
    return m * x + b


# In[100]:


print(df.columns)


# In[102]:


df.rename(columns={'SF6ottoyr': 'Year'}, inplace=True)
df.rename(columns={'SF6ottoGLm': 'global_mean_concentration'}, inplace=True)
df.rename(columns={'SF6ottoGLsd': 'global_mean_concentration_sd'}, inplace=True)


# In[103]:


print(df.columns)


# In[105]:


df_clean = df.dropna(subset=['Year', 'global_mean_concentration'])
df_clean = df_clean.replace([np.inf, -np.inf], np.nan).dropna()

# Fit a linear model to the clean data
parameters, covariance = curve_fit(linear_model, df_clean['Year'], df_clean['global_mean_concentration'])


# In[106]:


residuals = df['global_mean_concentration'] - linear_model(df['Year'], *parameters)
chi_squared = np.sum((residuals / df['global_mean_concentration_sd'])**2)
dof = len(df) - 2  # Degrees of freedom
reduced_chi_squared = chi_squared / dof


# In[107]:


print("Linear Model Parameters:")
print("Slope (m):", parameters[0])
print("Intercept (b):", parameters[1])
print("Parameter Errors:", np.sqrt(np.diag(covariance)))
print("Reduced Chi-squared Value:", reduced_chi_squared)


# In[ ]:




