import plotly.express as px

def plot_numeric(df, col):
    fig = px.histogram(df, x=col, title=f"Distribution of {col}")
    return fig

def plot_box(df, col):
    fig = px.box(df, y=col, title=f"Boxplot of {col}")
    return fig

def plot_categorical(df, col, top_n=10):
    data = df[col].value_counts().head(top_n)
    fig = px.bar(
        x= data.index,
        y= data.values,
        title=f"Top {top_n} Category in {col}"
    )
    return fig

def plot_correlation(df):
    corr = df.select_dtypes(include=['number']).corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    fig.update_layout(
        title='Correlation Heatmap',
        width=900,
        height=700
    )
    return fig
