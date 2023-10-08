import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})

options_builder = GridOptionsBuilder.from_dataframe(df)
options_builder.configure_column('col1', editable=True)
options_builder.configure_selection("single")
grid_options = options_builder.build()

grid_return = AgGrid(df, grid_options)
selected_rows = grid_return["selected_rows"]

st.write(selected_rows)
