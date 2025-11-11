import streamlit as st
import graphviz as gv

st.header("Praktikum 2 Visualisasi Data")
st.subheader("Graph Chart")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

st.graphviz_chart("""
digraph {
    "Training Data" -> "ML Algorithm"
    "ML Algorithm" -> "Model"
    "Model" -> "Result Forecasting"
    "New Data" -> "Model"
}
""")

# Create a graphlib graph object
graph = gv.Digraph()
graph.edge("Training Data", "ML Algorithm")
graph.edge("ML Algorithm", "Model")
graph.edge("Model", "Result Forecasting")
graph.edge("New Data", "Model")
st.graphviz_chart(graph)