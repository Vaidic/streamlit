import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.header("st.write")

# Example 1
st.write("Hello *world* :sunglasses:")

# Example 2
st.write(1234)

# Example 3
df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})
st.write(df)

# Example 4
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=["a", "b", "c"]
)
c = alt.Chart(df2).mark_circle().encode(
    x="a", y="b", size="c", color="c"
)
st.write(c)