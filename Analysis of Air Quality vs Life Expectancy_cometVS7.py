import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Pollution Dataset
pollution_data = pd.read_csv(r"C:\Users\mailv\Desktop\SIT\SEM2\STAIML\Project\global air pollution dataset.csv")
print(pollution_data.head())

# Load Life Expectancy Dataset
life_data = pd.read_csv(r"C:\Users\mailv\Desktop\SIT\SEM2\STAIML\Project\Life Expectancy Data.csv")
print(life_data.head())

# Clean and select relevant columns from both datasets
pollution_data_clean = pollution_data[['Country', 'PM2.5 AQI Value']].copy()  # Use .copy() to avoid SettingWithCopyWarning
life_data_clean = life_data[['Country', 'Life expectancy ']].copy()

# Average values per country
pollution_avg = pollution_data_clean.groupby('Country').mean().reset_index()
life_avg = life_data_clean.groupby('Country').mean().reset_index()

# Merge both datasets based on Country
merged_data = pd.merge(pollution_avg, life_avg, on='Country')

# Filter for 65 major countries
major_countries = [
    'United States', 'China', 'India', 'Russia', 'Japan', 'Germany', 'United Kingdom', 'France', 'Brazil', 'Italy',
    'Canada', 'South Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland',
    'Argentina', 'Sweden', 'Belgium', 'Poland', 'Thailand', 'Norway', 'Austria', 'United Arab Emirates', 'Nigeria', 'South Africa',
    'Denmark', 'Singapore', 'Malaysia', 'Philippines', 'Vietnam', 'Bangladesh', 'Egypt', 'Pakistan', 'Israel', 'Colombia',
    'Ireland', 'New Zealand', 'Greece', 'Portugal', 'Czech Republic', 'Finland', 'Romania', 'Hungary', 'Chile', 'Ukraine',
    'South Korea', 'Iran', 'Kenya', 'Peru', 'Slovakia', 'Morocco', 'Kazakhstan', 'Slovenia', 'Latvia', 'Croatia',
    'Lithuania', 'Estonia', 'Bosnia and Herzegovina', 'Algeria', 'Tunisia', 'Sri Lanka', 'Jordan', 'Oman', 'Kuwait']

# Keep only those 65 countries
merged_data = merged_data[merged_data['Country'].isin(major_countries)]

# Display final merged data
print("\nFinal Merged Data:")
print(merged_data.head())

# Set Seaborn style
sns.set(style="whitegrid")

#Scatter plot: PM2.5 vs Life Expectancy
plt.figure(figsize=(12, 7))
sns.scatterplot(x=merged_data['PM2.5 AQI Value'], y=merged_data['Life expectancy '], s=120, color='dodgerblue')
plt.title('PM2.5 Pollution vs Life Expectancy (65 Major Countries)', fontsize=16)
plt.xlabel('Average PM2.5 AQI Value')
plt.ylabel('Average Life Expectancy (Years)')
plt.grid(True)

#Add regression line
sns.regplot(x=merged_data['PM2.5 AQI Value'], y=merged_data['Life expectancy '], scatter=False, color='red')
plt.tight_layout()
plt.show()

#Bar chart: Country-wise PM2.5 Levels
plt.figure(figsize=(14, 7))
sorted_pollution = merged_data.sort_values('PM2.5 AQI Value', ascending=False)
sns.barplot(x='PM2.5 AQI Value', y='Country', data=sorted_pollution)
plt.title('Country-wise Average PM2.5 AQI (65 Major Countries)', fontsize=16)
plt.xlabel('Average PM2.5 AQI Value')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

#Bar chart: Country-wise Life Expectancy
plt.figure(figsize=(14, 7))
sorted_life = merged_data.sort_values('Life expectancy ', ascending=False)
sns.barplot(x='Life expectancy ', y='Country', data=sorted_life)
plt.title('Country-wise Average Life Expectancy (65 Major Countries)', fontsize=16)
plt.xlabel('Average Life Expectancy (Years)')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

#Correlation calculation
correlation = merged_data['PM2.5 AQI Value'].corr(merged_data['Life expectancy '])
print(f"\n Correlation between PM2.5 and Life Expectancy: {correlation:.4f}")

if correlation < 0:
    print("As PM2.5 increases, life expectancy tends to decrease.")
else:
    print("Higher PM2.5 is associated with higher life expectancy (unexpected).")