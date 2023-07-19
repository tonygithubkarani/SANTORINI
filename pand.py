import pandas  as pd
df1 = pd.DataFrame({"HPI":[80,70,60,50],"int_rate":[2,1,2,3],"IDG_GDP":[50,45,45,67]},index=[2001,2002,2003,2004])

df2 = pd.DataFrame({"ABS":[80,70,60,50],"AS":[2,1,2,3],"IDG":[50,45,45,67]},index = [2005,2006,2007,2008])

joined = df1.join(df2)
print(joined)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df1=pd.DataFrame({"Day":[1,2,3,4,5,6],"Visitors":[1000,700,6000,1000,400,350],"Bounce_rate":[20,20,30,40,35,34]})
df1 =df1.rename(columns={"Visitors":"Users"})
print(df1)

import pandas as pd
country=pd.read_csv