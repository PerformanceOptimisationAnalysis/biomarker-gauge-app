
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Biomarker Linear Gauge Generator")

st.markdown("### Paste your biomarker data below (CSV format)")
csv_data = st.text_area("Example: Marker,Result,Min,Max,Optimal Min,Optimal Max", "", height=200)

if csv_data:
    from io import StringIO
    df = pd.read_csv(StringIO(csv_data))
    st.write(df)

    st.markdown("---")
    st.markdown("### Linear Gauges")

    for index, row in df.iterrows():
        fig = go.Figure()

        fig.add_trace(go.Indicator(
            mode = "gauge+number",
            value = row['Result'],
            title = {'text': row['Marker']},
            gauge = {
                'shape': "bullet",
                'axis': {'range': [row['Min'], row['Max']]},
                'threshold': {
                    'line': {'color': "red", 'width': 2},
                    'thickness': 0.75,
                    'value': row['Result']
                },
                'steps': [
                    {'range': [row['Min'], row['Optimal Min']], 'color': "lightgray"},
                    {'range': [row['Optimal Min'], row['Optimal Max']], 'color': "green"},
                    {'range': [row['Optimal Max'], row['Max']], 'color': "lightgray"}
                ]
            }
        ))

        fig.update_layout(height=150)
        st.plotly_chart(fig)
