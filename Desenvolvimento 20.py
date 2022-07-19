
import pandas as pd

df = pd.read_csv('notas_alunos.csv')

media = (df["nota_1"]+df["nota_2"])/2

df["media"] = media

df.loc[df["media"]>=7,"situacao"]  ="APROVADO"
df.loc[df["faltas"]>5 ,"situacao"] ="REPROVADO"
df.loc[df["media"]<7 ,"situacao"]  ="REPROVADO"
df.to_csv('C:/Users/Filip/Documents/Programas python/notas_alunos.csv',index=False)
