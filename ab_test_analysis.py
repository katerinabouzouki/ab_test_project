import pandas as pd
from scipy.stats import chi2_contingency

# Load the CSV dataset
df = pd.read_csv('ab_test_sample_data.csv')

# Calculate conversion rates per group
conversion_rates = df.groupby('Group')['Converted'].mean()
print("Conversion Rates:")
print(conversion_rates)

# Create contingency table for Chi-Square Test
contingency_table = pd.crosstab(df['Group'], df['Converted'])
print("\nContingency Table:")
print(contingency_table)

# Perform Chi-Square Test
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f"\nChi-Square Test Statistic: {chi2}")
print(f"P-value: {p}")

# Conclusion
alpha = 0.05
if p < alpha:
    print("\nResult: Statistically significant difference between groups (reject H0).")
else:
    print("\nResult: No statistically significant difference between groups (fail to reject H0).")