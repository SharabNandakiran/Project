import pandas as pd
import plotly_express as px
import streamlit as st 

st.set_page_config(page_title="Production Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")
df = pd.read_excel("June_report.xlsx")

st.sidebar.header("Please Filter Here for Production Details:")

OPERATOR = st.sidebar.multiselect(
    "Select the operator",
    options=df["OPERATOR"].unique()
    #default=df["OPERATOR"].unique()
)

#MACHINE = st.sidebar.multiselect(
#    "Select the Machine",
#    options=df["MACHINE"].unique()
    #default=df["OPERATOR"].unique()
#)

df_selection = df.query("OPERATOR == @OPERATOR")

st.title("Operator Performance")
st.markdown("##")

plan_qty = int(df_selection["PLAN QTY"].sum())
actual_qty = int(df_selection["ACTUAL QTY"].sum())
efficiency = round(df_selection["EFFICIENCY"].mean(),2)
consumption = round(df_selection["CONSUMPTION"].sum(),2)

first_column, second_column, third_column, fourth_column = st.columns(4)
with first_column:
    st.subheader("Total Plan Qty")
    st.subheader(f"{plan_qty}")

with second_column:
    st.subheader("Total Actual Qty")
    st.subheader(f"{actual_qty}")
    
with third_column:
    st.subheader("Efficiency")
    st.subheader(f"{efficiency} %")

with fourth_column:
    st.subheader("Consumption")
    st.subheader(f"{consumption} kgs")




st.dataframe(df_selection)





#streamlit run Production_Dashboard.py


