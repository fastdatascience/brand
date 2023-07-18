# Python library to produce Fast Data Science branded graphs in Plotly

## Installation

```
pip install .
```

## Usage

### Light theme

```
import fastdatascience

import plotly.express as px
fig = px.line(x=[1,2,3], y=[3,1,2],
                title="<b>Receiver operating characteristic</b>")

fastdatascience.brand(fig)

fig.show(renderer="png")
```

![fds.png](fds.png)
