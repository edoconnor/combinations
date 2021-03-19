import pandas as pd
from itertools import combinations 
import time 

df = pd.read_csv("data.csv") 
df = df[['player', 'salary']]

player = df['player']
combos = list(combinations(player,5))

df5 = pd.DataFrame(combos, columns =['A', 'B', 'C', 'D', 'E']) 

df5['AA'] = df5.A.replace(df.set_index('player').salary.to_dict())
df5['BB'] = df5.B.replace(df.set_index('player').salary.to_dict())
df5['CC'] = df5.C.replace(df.set_index('player').salary.to_dict())
df5['DD'] = df5.D.replace(df.set_index('player').salary.to_dict())
df5['EE'] = df5.E.replace(df.set_index('player').salary.to_dict())
df5['F'] = (df5['AA'] + df5['BB'] + df5['CC'] + df5['DD'] + df5['EE'])

df6 = df5[['A', 'B', 'C', 'D', 'E', 'F']]

print(df6)
df = df6
df.to_csv('picks.csv')

#------------------------
begin = time.time()  
for i in range(5): 
    print(".....") 
time.sleep(1) 
end = time.time() 
print(f"Total runtime: {end - begin}") 
#------------------------