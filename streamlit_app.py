import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
data = pd.read_csv('bmi.csv')

# Create a Streamlit app title
st.title('BMI Class Analysis')

# Add some information about the data
st.write("The dataset contains information about Age, Height, Weight, BMI, and BMI Class.")


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)





st.write("**You can view data about specific BmiClass**")
# Add an interactive feature to filter data by BMI Class
selected_bmi_class = st.multiselect("Select BMI Class", data['BmiClass'].unique())
filtered_data = data[data['BmiClass'].isin(selected_bmi_class)]
st.write("Filtered Data:")
st.write(filtered_data)



# Add an interactive feature to display summary statistics
st.subheader("Summary Statistics About Age and Bmi")
selected_feature = st.selectbox("Select Feature for Summary", ["Age", "Bmi"])
if selected_feature == "Age":
    st.write("Summary Statistics for Age:")
    st.write(data['Age'].describe())
else:
    st.write("Summary Statistics for BMI:")
    st.write(data['Bmi'].describe())



st.subheader("Visualizations")
st.write("**Box plot of Bmi vs BmiClass**")
st.write("You can hover over the boxes to see Age and BMI information.")
# Create the box plot figure with custom colors
fig2 = px.box(
    data,
    x="BmiClass",
    y="Bmi",
    title="BMI Distribution by BMI Class",
    color_discrete_sequence=["#003366"],
    hover_data=["Age"],  # Add Age as hover information
)
# Customize the layout for zooming and panning
fig2.update_xaxes(showline=True, linewidth=1, linecolor='black', fixedrange=True)
fig2.update_yaxes(showline=True, linewidth=1, linecolor='black', fixedrange=True)


# Set the background color to be transparent
fig2.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',  # Transparent background
    'paper_bgcolor': 'rgba(0, 0, 0, 0)'  # Transparent plot area
})

# Add hover template to display Age and Bmi values
fig2.update_traces(hovertemplate='Age: %{customdata[0]}<br>BMI: %{y}')
# Enable the legend
fig2.update_layout(showlegend=True)

# Show the updated figure
st.plotly_chart(fig2)





# Assuming 'data' is your DataFrame containing the necessary information

# Visualizations
st.write("## Visualizations")

# Interactive Feature: Select Age for Filtering
selected_age = st.slider("Select Age to view BmiClass distribution about", min_value=int(data['Age'].min()), max_value=int(data['Age'].max()))

# Filter data based on selected age
filtered_data_pie = data[data['Age'] == selected_age]

# Create a pie chart for BMI class distribution based on the selected age
st.write(f"### BMI Class Distribution for Age {selected_age}")
# Define a color scale ranging from a bright color to a dark color
color_scale = px.colors.sequential.Blues[::-1]
fig_pie_age = px.pie(
    filtered_data_pie['BmiClass'].value_counts().reset_index(),
    names='index',
    values='BmiClass',
    title=f'BMI Class Distribution for Age {selected_age}',
    color_discrete_sequence=color_scale,
)
fig_pie_age.update_traces(textinfo='percent+label', textfont_size=14)

# Add labels to chart segments
fig_pie_age.update_traces(textinfo='percent+label', textfont_size=14)
# Enable the legend
fig_pie_age.update_layout(showlegend=True)

st.plotly_chart(fig_pie_age)






import streamlit as st
import plotly.express as px
import pandas as pd

# Assuming 'data' is your DataFrame containing the necessary information

# Visualizations


# Scatter plot for Age vs. BMI
#st.write("### Scatter Plot of Age vs. BMI")
#fig_age_bmi = px.scatter(data, x="Age", y="Bmi", title="Age vs. BMI Scatter Plot", color="BmiClass")

# Add interactive features
st.subheader("Age vs Bmi")

import streamlit as st

# Assuming 'data' is your DataFrame containing the necessary information

# Get unique BMI classes
all_bmi_classes = data['BmiClass'].unique()

# Set the default value to "Obese Class 1" if it exists in the data
default_bmi_classes = ["Obese Class 1"] if "Obese Class 1" in all_bmi_classes else []

# Create the multiselect widget with the default value
selected_bmi_classes = st.multiselect("Select BMI Classes(You can add more than one class)", all_bmi_classes, default=default_bmi_classes)

filtered_data_scatter = data[data['BmiClass'].isin(selected_bmi_classes)]
fig_age_bmi_filtered = px.scatter(filtered_data_scatter, x="Age", y="Bmi", title=f"Age vs. BMI Scatter Plot ({', '.join(selected_bmi_classes)} Classes)", color="BmiClass")

# Display the scatter plot
#st.plotly_chart(fig_age_bmi)
st.plotly_chart(fig_age_bmi_filtered)
