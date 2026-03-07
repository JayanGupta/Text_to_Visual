import plotly.express as px
import plotly.graph_objects as go

class ChartLibrary:
    """General-purpose Visualization Library"""
    
    COLORS = {
        'primary': '#6c63ff',
        'secondary': '#48cfad',
        'background': '#0e0e0e',
        'text': '#FFFFFF',
        'grid': '#2a2a3e'
    }

    PALETTE = px.colors.sequential.Plasma

    @staticmethod
    def apply_theme(fig):
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color=ChartLibrary.COLORS['text'], family="Inter, sans-serif"),
            margin=dict(l=40, r=40, t=60, b=40),
            hovermode='closest',
            title_font_size=20,
            showlegend=True
        )
        fig.update_xaxes(gridcolor=ChartLibrary.COLORS['grid'], showline=True, linewidth=1, linecolor=ChartLibrary.COLORS['grid'])
        fig.update_yaxes(gridcolor=ChartLibrary.COLORS['grid'], showline=True, linewidth=1, linecolor=ChartLibrary.COLORS['grid'])
        return fig

    @staticmethod
    def bar_chart(df, x, y, title, orientation='v'):
        fig = px.bar(df, x=x, y=y, title=title, orientation=orientation,
                     color_discrete_sequence=[ChartLibrary.COLORS['primary']])
        return ChartLibrary.apply_theme(fig)

    @staticmethod
    def line_chart(df, x, y, title):
        fig = px.line(df, x=x, y=y, title=title,
                      color_discrete_sequence=[ChartLibrary.COLORS['secondary']])
        return ChartLibrary.apply_theme(fig)

    @staticmethod
    def scatter_plot(df, x, y, title, color=None, size=None):
        fig = px.scatter(df, x=x, y=y, title=title, color=color, size=size,
                         color_discrete_sequence=ChartLibrary.PALETTE)
        return ChartLibrary.apply_theme(fig)

    @staticmethod
    def pie_chart(df, names, values, title):
        fig = px.pie(df, names=names, values=values, title=title,
                     color_discrete_sequence=ChartLibrary.PALETTE)
        return ChartLibrary.apply_theme(fig)

    @staticmethod
    def histogram(df, x, title):
        fig = px.histogram(df, x=x, title=title,
                           color_discrete_sequence=[ChartLibrary.COLORS['primary']])
        return ChartLibrary.apply_theme(fig)
