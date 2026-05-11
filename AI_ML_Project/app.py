import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

from backend.eda import dataset_summary
from backend.visualization import plot_box, plot_categorical, plot_numeric, plot_correlation

st.title("Auto Insight")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file :
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    summary = dataset_summary(df)
    
    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", summary["rows"])
    col2.metric("Columns", summary["columns"])
    col3.metric("Duplicates", summary["duplicates"])

    st.subheader("Missing Values")
    st.write(summary['missing_values'])

    st.subheader('Data Types')
    dtype_df = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.astype(str),
        'Missing Values': df.isnull().sum().values
    })

    st.dataframe(dtype_df, use_container_width=True)

    st.subheader("Column Categorization")

    col_numeric = df.select_dtypes(include=['number'])
    col_categorical = df.select_dtypes(include=['object', 'category'])

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Numeric Columns**")
        st.write(list(col_numeric.columns))
        st.caption(f"Total: {len(col_numeric.columns)} columns")

    with col2:
        st.write("**Categorical Columns**")
        st.write(list(col_categorical.columns))
        st.caption(f"Total: {len(col_categorical.columns)} columns")

    st.subheader("Numeric Visualization")
    numeric_cols = df.select_dtypes(include=['number']).columns
    selected_num = st.selectbox("Choose Numeric Column", numeric_cols)

    if selected_num :
        col1, col2 = st.columns(2)
        with col1 :
            st.plotly_chart(plot_numeric(df, selected_num), use_container_width=True)
        with col2 :
            st.plotly_chart(plot_box(df, selected_num), use_container_width=True)

    st.subheader("Categorical Visualization")
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    selected_cat = st.selectbox("Choose Categorical Column", cat_cols)

    if selected_cat :
        st.plotly_chart(
            plot_categorical(df, selected_cat),
            use_container_width=True
        )

    st.subheader("Correlation Analysis")
    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.shape[1] > 1 :
        st.plotly_chart(
            plot_correlation(df),
            use_container_width=True
        )
    else : 
        st.info("Not enough numeric columns for correlation analysis")