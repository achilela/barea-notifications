# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd

# Load sample data (you can replace this with your own Excel file)
sample_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Color': ['red', 'blue', 'blue', 'black', 'green']
})

def main():
    st.title("Excel Data Filter App")

    # Upload Excel file
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xls", "xlsx"])

    if uploaded_file:
        # Read data from the uploaded file
        data = pd.read_excel(uploaded_file)

        # Sidebar filters
        st.sidebar.title("Filters")
        selected_names = st.sidebar.multiselect("Select Name", data['Name'].unique())
        selected_colors = st.sidebar.multiselect("Select Color", data['Color'].unique())

        # Apply filters
        filtered_data = data[
            (data['Name'].isin(selected_names)) &
            (data['Color'].isin(selected_colors))
        ]

        # Display filtered results
        st.subheader("Filtered Data")
        st.dataframe(filtered_data)

        # Calculate and display totals
        st.subheader("Totals")
        st.write(f"Total rows: {len(filtered_data)}")
        st.write(f"Total unique names: {len(filtered_data['Name'].unique())}")
        st.write(f"Total unique colors: {len(filtered_data['Color'].unique())}")

if __name__ == "__main__":
    main()
