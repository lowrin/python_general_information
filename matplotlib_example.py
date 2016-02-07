import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


engine = create_engine("postgresql://postgres:<password>@localhost:5432/<dbname>")
df = pd.read_excel("b.xlsx")
print(df.describe())
print(df.info())
bp = df.boxplot(return_type='axes')
plt.show()
