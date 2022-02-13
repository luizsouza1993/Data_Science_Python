import pandas
import statsmodels.formula.api as smf

# Load a file containing dog's boot and harness sizes
data = pandas.read_csv(r'C:\Users\Samsung Max\OneDrive\Área de Trabalho\Microsoft\Cientista de Dados\doggy-boot-harness.csv')

# Print the first few rows
print(data.head())

# Fit a simple model that finds a linear relationship
# between booth size and harness size, which we can use later
# to predict a dog's boot size, given their harness size
model = smf.ols(formula = "boot_size ~ harness_size", data = data).fit()

print("Model trained!")




