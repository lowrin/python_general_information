import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('seaborn-whitegrid')


engine = create_engine("postgresql://postgres:<password>@localhost:5432/<dbname>")
df = pd.read_excel("b.xlsx")
print(df.describe())
print(df.info())
bp = df.boxplot(return_type='axes')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.show()
