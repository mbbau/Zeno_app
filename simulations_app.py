import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ---- Starting Configuration and titles ----
st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Zeno Simulations")
st.markdown(
    "Welcome to the Zeno Simulations web app. This platform provides insights into user behavior "
    "on our learning platform through advanced Monte Carlo simulations. Explore the results and "
    "discover valuable information to shape strategic decisions and enhance the user experience."
)

# Set Seaborn style
sns.set(style="whitegrid")

# ---- Zeno Logo ----

st.sidebar.image('Zeno_logo.svg')
st.sidebar.header('Filtering Panel')

# Display the summary in English
summary_text = """

In the absence of empirical data, the project was initiated to gain insights into user behavior on the learning platform through Monte Carlo simulations. The initial phase involved the development of comprehensive functions to simulate users' weekly interactions, encompassing activities such as video consumption, quizzes, and social sharing. Each interaction contributed to an accumulation of experience points, subsequently associated with benefits and rewards. The outcomes of these simulations will inform the development of tailored benefits and rewards structures.

Furthermore, the simulations facilitated the estimation of user lifecycle dynamics, shedding light on the expected duration of user engagement. The calculation of the lifetime value for distinct user tiers was another key outcome, offering valuable insights for strategic decision-making. The next steps involve leveraging these simulation results to design and implement user-centric benefits, ultimately enhancing the learning platform's appeal and user retention.
"""
st.subheader("Project Overview: Simulating User Behavior in a Learning Platform")
st.markdown(summary_text)
st.markdown("In the next figure, you will be able to see the parameters that were simulated for every user.")
st.image('simulation_details.png')

st.markdown('The process we adopted to conduct this analysis involved first generating a user dataset using the Monte Carlo simulations mentioned earlier. These simulations were performed in the "Zeno_simulations.ipynb" script. The results of these simulations were then stored in a database (Zeno_simulations.db) with the aim of making this information available for further analyses.')

# summarized simulations' data
st.subheader("Simulation Results Overview.")
st.markdown(
    "Explore the overview of simulation results, which provide insights into the user life cycle "
    "under different scenarios and varying parameters. Each row in the table represents a summary "
    "of a user's life cycle considering different simulation settings. In the next table you will be able a sample of the final table."
)
df = pd.read_csv('Summary_table.csv', encoding='utf-8- sig')
# sample table
st.dataframe(df.head(10))

st.write(f'Based on the simulations, our analysis reveals that users are anticipated to experience a lifecycle ranging between {df.total_weeks.min()} and {df.total_weeks.max()} weeks '
         '. The corresponding distribution is illustrated in the following histogram.')

# histogram of weeks
fig_hist_weeks, hist_weeks =  plt.subplots(figsize=(8, 5))
hist_weeks = sns.histplot(df, x='total_weeks', bins=15, hue='tier', multiple='stack', palette='viridis', alpha=0.7)
plt.title('Distribution of Lifetime Cycle in weeks per user.')
plt.xlabel('Weeks')
plt.ylabel('Number of users')
st.pyplot(fig_hist_weeks)

st.markdown('Next you will be able to see how the life time cycle changes whenever the mean amount of hours spend per week changes')

fig_box_lifetime, box_lifetime =  plt.subplots(figsize=(8, 5))
box_lifetime = sns.boxplot(
    data = df,
    x = 'hour_simulated_avg', 
    y = 'total_weeks', 
    hue='tier'
    )
plt.title('Distribution of Lifetime Cycle in weeks per average hour simulated and tier')
plt.xlabel('Simulated Avg Hours')
plt.ylabel('Weeks')
st.pyplot(fig_box_lifetime)

st.markdown('As observed, as the weekly hours of usage increase for users, their lifecycle significantly decreases, from an average of 130 weeks to 60 for tier 2 and 3, and from 70 to 30 for tier 1 users. This distinct behavior between tier 1 and the rest was achieved by reducing the number of available courses for this user type, representing the limit of two monthly courses they have. Nevertheless, we estimate that the actual behavior will result from a general average of behaviors, as seen in the following chart, illustrating the distribution of lifecycle in weeks per tier.')

fig_violin_lifetime, violin_lifetime =  plt.subplots(figsize=(8, 5))
violin_lifetime = sns.violinplot(
    data = df,
    x = 'total_weeks', 
    y = 'tier',
    split=True,
    inner="point"
    )
plt.title('Distribution of Lifetime Cycle in weeks per tier')
plt.xlabel('Lifetime in weeks')
plt.ylabel('Tiers')
st.pyplot(fig_violin_lifetime)

st.subheader("Weekly Study Hours Distribution by User Tier")

# Add a description for the histogram
st.markdown(
    "Explore the distribution of weekly study hours among different user tiers. "
    "This histogram provides insights into how users from various tiers allocate their time for learning."
)

# histogram
plt.figure(figsize=(10, 6))
sns.histplot(
    df, 
    x='weekly_hour_avg', 
    bins=20, 
    kde=True, 
    hue='hour_simulated_avg', 
    multiple='stack', 
    palette='viridis', 
    alpha=0.7)
plt.title('Users weekly hours distribution for different averages')
plt.xlabel('Hours')
plt.ylabel('Frecuency')
# Pass the Matplotlib figure to st.pyplot()
st.pyplot(plt)



