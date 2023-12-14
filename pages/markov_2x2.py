import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Markov Chain Calculator")

# Define the states
states = []

for state in range(2):
    state = st.text_input("Enter state: ", key=state)
    states.append(state)

df = pd.DataFrame(columns=['Iterations'] + states)

# Define the initial state
ism = np.zeros((2), dtype=float)

# for loop to get probabilities for ism
for i in range(2):
    # Prompt the user for a float value
    value = st.number_input(f"Enter probability for S0 ({i + 1}): ")
    # Store the value in the corresponding position of the matrix
    ism[i] = value

df.loc[0] = [0] + list(ism)

# Define the transition matrix
tpm = np.zeros((2, 2), dtype=float)

# for loop to get probabilities for tpm
for i in range(2):
  for j in range(2):
    # Prompt the user for a float value
    value = st.number_input(f"Enter probability for TPM ({i + 1},{j + 1}): ")
    # Store the value in the corresponding position of the matrix
    tpm[i, j] = value

iterations = st.slider("Number of iterations", 1, 100, 1)

for i in range(iterations):
    ism = np.dot(ism, tpm)
    df.loc[i + 1] = [i + 1] + list(ism.copy())

if st.button('Calculate'):
    # correspond each state to the values in the ism and store in a dictionary. convert the ism values to percentages and round to 2 decimal places
    results = dict(zip(states, np.round(ism * 100, 2)))

    output = " "
    # Loop through each state and probability
    for state, probability in zip(states, ism):
        # Format the probability with two decimal places
        output += f"* **{state}:** {probability:.2%}\n"
    
    fig, ax = plt.subplots()
    ax.plot(df['Iterations'], df[states], label=states)
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Probability')
    ax.set_title('Markov Chain')
    ax.legend()
    st.pyplot(fig)

    # Display the formatted output in Streamlit
    st.markdown(output)

    df = pd.DataFrame(columns=['Iterations'] + states)