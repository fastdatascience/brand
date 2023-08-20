__version__ = "0.3.3"

colour_sequence = ['#57cc98','#102a38','#225679','#37a1a3','#0bc36e','#7feb97','#c6f7ca','#0193fc','#bde55d']

import plotly.io as pio
import plotly.graph_objects as go
pio.templates["fastdatascience"] = go.layout.Template(
    layout=go.Layout(
        colorway=colour_sequence[0:1] + colour_sequence[2:] + colour_sequence[1:2]
    )
)
pio.templates.default = 'fastdatascience'

# Brand a Plotly graph with Fast Data Science Light theme
def brand(fig, opacity = 1.0):
    fig.add_layout_image(
        dict(
            source="https://raw.githubusercontent.com/fastdatascience/brand/main/logo.svg",
            xref="paper", yref="paper",
            x=1, y=1,
            sizex=0.25, sizey=0.25,
            xanchor="right", yanchor="bottom",
            opacity = opacity
        )
    )

    fig.update_layout(
        font_family="DM Sans, Roboto, Roboto Bold, PT Sans, PT Sans Bold",
        font=dict(
            family="DM Sans, Roboto, Roboto Bold, PT Sans, PT Sans Bold",
            size=18,
            #color="RebeccaPurple"
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    width=1200,
        height=600,

    )

    fig.update_xaxes(showline=True, linewidth=1, linecolor='#cccccc', gridcolor='#cccccc')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='#cccccc', gridcolor='#cccccc')

    #try:
    #    # line graph
    #    fig.update_traces(line_color='#80ed99')
    #except:
    #    # bar graph
    #    fig.update_traces(marker_color='#0BC36E')
