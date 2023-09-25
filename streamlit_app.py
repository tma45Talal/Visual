import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Load the dataset
data = pd.read_csv("bmi.csv")

# Create a Streamlit app title
st.title('BMI Class Analysis')

# Add some information about the data
st.write("The dataset contains information about Age, Height, Weight, BMI, and BMI Class.")

st.write("Note that bmi=weight/height^2")
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
    names='df.index',
    values='BmiClass',
    title=f'BMI Class Distribution for Age {selected_age}',
    color_discrete_sequence=color_scale,
)
fig_pie_age.update_traces(textinfo='percent+label', textfont_size=14)

# Add labels to chart segments
fig_pie_age.update_traces(textinfo='percent+label', textfont_size=14)
# Enable the legend
fig_pie_age.update_layout(showlegend=True)

# Display the explanation for the pie chart
st.write("The following pie chart shows the distribution of BMI classes for the selected age. Each segment represents a BMI class, and the percentage label indicates the proportion of individuals in each class.")

# Display the pie chart
st.plotly_chart(fig_pie_age)


# Add a scatter plot of BMI vs. Weight
st.subheader("BMI vs Weight")

# Get unique BMI classes
all_bmi_classes = data['BmiClass'].unique()

# Create the multiselect widget for BMI classes with all classes selected by default
selected_bmi_classes = st.multiselect("Select BMI Classes (You can add more than one class)", all_bmi_classes, default=all_bmi_classes)

# Filter the data based on selected BMI classes
filtered_data_scatter_bmi_weight = data[data['BmiClass'].isin(selected_bmi_classes)]

# Create the scatter plot for BMI vs. Weight
fig_bmi_weight = px.scatter(
    filtered_data_scatter_bmi_weight,
    x="Weight",
    y="Bmi",
    title=f"BMI vs. Weight Scatter Plot ({', '.join(selected_bmi_classes)} Classes)",
    color="BmiClass",
)


# Display the scatter plot
st.plotly_chart(fig_bmi_weight)

# Display the explanation for the scatter plot
st.write("The above scatter plot shows the relationship between BMI and Weight. Each point represents an individual, color-coded by BMI class. It helps visualize how weight and BMI are distributed across different BMI classes. There is a positive relationship between bmi and weight since when calculating a bmi value, weight is in the numerator")

# Create a bar plot to show the average BMI for each age group
st.subheader("Average BMI by Age (Bar Plot)")
age_bmi_avg = data.groupby("Age")["Bmi"].mean().reset_index()
fig_bar = px.bar(age_bmi_avg, x="Age", y="Bmi", title="Average BMI by Age (Bar Plot)")


# Display the bar plot
st.plotly_chart(fig_bar)


# Display the explanation for the bar plot
st.write("This bar plot displays the average BMI for each age group. It provides insights into how BMI varies across different age groups, helping to identify potential trends or patterns. For example, the average bmi for age 34 is about 25.")
