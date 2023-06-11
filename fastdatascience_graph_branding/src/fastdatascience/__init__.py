__version__ = "0.3.0"

# Brand a Plotly graph with Fast Data Science Light theme
def brand(fig):
    fig.add_layout_image(
        dict(
            source="https://raw.githubusercontent.com/fastdatascience/brand/main/logo.svg",
            xref="paper", yref="paper",
            x=1, y=1,
            sizex=0.25, sizey=0.25,
            xanchor="right", yanchor="bottom"
        )
    )

    fig.update_layout(
        font_family="Roboto, Roboto Bold, PT Sans, PT Sans Bold",
        xaxis_title="Date",
        yaxis_title="Postings per million",
        font=dict(
            family="Roboto, Roboto Bold, PT Sans, PT Sans Bold",
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

    fig.update_traces(line_color='#80ed99')
