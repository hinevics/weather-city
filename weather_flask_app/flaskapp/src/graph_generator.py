import plotly
import plotly.graph_objects as go
# import plotly.express as px
from plotly.subplots import make_subplots


def multiple_axes(x, y1, y2):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    # fig = go.Figure()

    # max_temps
    fig.add_trace(
        go.Scatter(x=datetimes, y=max_temps, name="max_temp"),
        secondary_y=False,)
    # min_temps
    fig.add_trace(
        go.Scatter(x=datetimes, y=min_temps, name="min_temp"),
        secondary_y=False,)
    # snows
    fig.add_trace(
        go.Scatter(x=datetimes, y=snows, name="snow"),
        secondary_y=True,)

    # Add figure title
    fig.update_layout(
        title_text="Changes in snow thickness and changes in max/min temperature")

# Set x-axis title
    fig.update_xaxes(title_text="date")

# Set y-axes titles
    fig.update_yaxes(title_text="<b>Temperature</b>, Celcius", secondary_y=False)
    fig.update_yaxes(title_text="<b>Accumulated snowfall</b>, mm", secondary_y=True)
    # fig.add_trace(go.Scatter(x=datetimes, y=max_temps,
    #                          mode='lines',
    #                          name='max_temps'))
    # fig.add_trace(go.Scatter(x=datetimes, y=min_temps,
    #                          mode='lines',
    #                          name='min_temps'))
    # fig.add_trace(go.Scatter(x=datetimes, y=snows,
    #                          mode='lines',
    #                          name='snows'))
    # fig.add_trace(go.Scatter())
    # fig = px.line(df, x="date", y="lifeExp", color="continent",
    #               line_group="country", hover_name="country",
    #               line_shape="spline", render_mode="svg")

    return fig