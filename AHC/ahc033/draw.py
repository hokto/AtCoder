import plotly.express as px
import pandas as pd

df_tmp = pd.read_csv("./AHC/ahc033/temp.csv")
df_pr = pd.read_csv("./AHC/ahc033/pr.csv")
df_eval = pd.read_csv("./AHC/ahc033/eval.csv")
fig_tmp = px.line(x=df_tmp["cnt"],y=df_tmp["tmp"],title="cnt vs tmp")
fig_tmp.show()
fig_pr = px.line(x=df_pr["cnt"],y=df_pr["pr"],title="cnt vs pr")
fig_pr.show()
fig_eval = px.line(x=df_eval["cnt"],y=df_eval["eval"],title="cnt vs eval")
fig_eval.show()