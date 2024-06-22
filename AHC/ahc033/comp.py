import plotly.graph_objects as pgo
import pandas as pd
df_prev = pd.read_csv("./AHC/ahc033/res_20240526_ver2.csv")
df_now = pd.read_csv("./AHC/ahc033/res.csv")
fig = pgo.Figure()
fig.add_trace(pgo.Bar(x=df_prev["num"],y=df_prev["score"],name="prev"))
fig.add_trace(pgo.Bar(x=df_now["num"],y=df_now["score"],name="now"))
fig.update_layout(barmode="group")
fig.show()