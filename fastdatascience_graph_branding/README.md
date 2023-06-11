# Usage

```
import fastdatascience

import plotly.express as px
fig = px.line(x=df["date"], y=df["y"],
                title="<b>Demand for data scientists is increasing over time</b><br><sup>Data science postings per 1 million postings on Indeed. Data source: indeed.com</sup>")

fastdatascience.brand(fig)

fig.show(renderer="png")
```
