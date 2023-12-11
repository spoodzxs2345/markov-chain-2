import numpy as np
import streamlit as st

def activity_forecast(starting_state, ending_state, days):
    # Define the possible states
    states = ["Adobo", "Shanghai", "Mechado"]

    # Choose the starting state based on user input
    activityToday = starting_state

    # Initialize the list of activities
    activityList = [activityToday]

    # Initialize the probability
    prob = 1

    # Define the transition matrix
    transitionMatrix = np.array([
        [0.2, 0.6, 0.2],
        [0.1, 0.6, 0.3],
        [0.2, 0.7, 0.1]
    ])

    # Define the transition names for each state
    transitionName = [
        ["AA", "AS", "AM"],
        ["SA", "SS", "SM"],
        ["MA", "MS", "MM"]
    ]

    i = 0
    while i != days:
        if activityToday == states[0]:
            # Get the index of the starting state
            index = states.index(activityToday)

            # Randomly choose the next state based on the transition probabilities
            change = np.random.choice(transitionName[index], replace=True, p=transitionMatrix[index])

            # Update the activityToday and activityList variables
            if change == transitionName[index][0]:
                prob = prob * 0.2
                activityList.append(activityToday)
            elif change == transitionName[index][1]:
                prob = prob * 0.6
                activityToday = states[1]
                activityList.append(states[1])
            else:
                prob = prob * 0.2
                activityToday = states[2]
                activityList.append(states[2])

        elif activityToday == states[1]:
            # Get the index of the starting state
            index = states.index(activityToday)

            # Randomly choose the next state based on the transition probabilities
            change = np.random.choice(transitionName[index], replace=True, p=transitionMatrix[index])

            # Update the activityToday and activityList variables
            if change == transitionName[index][1]:
                prob = prob * 0.6
                activityList.append(activityToday)
            elif change == transitionName[index][0]:
                prob = prob * 0.1
                activityToday = states[0]
                activityList.append(states[0])
            else:
                prob = prob * 0.3
                activityToday = states[2]
                activityList.append(states[2])

        else:
            # Get the index of the starting state
            index = states.index(activityToday)

            # Randomly choose the next state based on the transition probabilities
            change = np.random.choice(transitionName[index], replace=True, p=transitionMatrix[index])

            # Update the activityToday and activityList variables
            if change == transitionName[index][2]:
                prob = prob * 0.1
                activityList.append(activityToday)
            elif change == transitionName[index][0]:
                prob = prob * 0.2
                activityToday = states[0]
                activityList.append(states[0])
            else:
                prob = prob * 0.7
                activityToday = states[1]
                activityList.append(states[1])

        i += 1

    # Check if the final state matches the user-specified ending state
    if activityList[-1] == ending_state:
        return activityList
    else:
        return None

# create a function that gets the starting state and returns the ending state
def get_ending_state(starting_state, days):
    # Define the possible states
    states = ["Adobo", "Shanghai", "Mechado"]

    # Choose the starting state based on user input
    activityToday = starting_state

    # Initialize the list of activities
    activityList = [activityToday]

    # Initialize the probability
    prob = 1

    # Define the transition matrix
    transitionMatrix = np.array([
        [0.2, 0.6, 0.2],
        [0.1, 0.6, 0.3],
        [0.2, 0.7, 0.1]
    ])

    # Define the transition names for each state
    transitionName = [
        ["AA", "AS", "AM"],
        ["SA", "SS", "SM"],
        ["MA", "MS", "MM"]
    ]

    i = 0
    while i != days:
        if activityToday == states[0]:
            # Get the index of the starting state
            index = states.index(activityToday)

            # Randomly choose the next state based on the transition probabilities
            change = np.random.choice(transitionName[index], replace=True, p=transitionMatrix[index])

            # Update the activityToday and activityList variables
            if change == transitionName[index][0]:
                prob = prob * 0.2
                activityList.append(activityToday)
            elif change == transitionName[index][1]:
                prob = prob * 0.6
                activityToday = states[1]
                activityList.append(states[1])
            else:
                prob = prob * 0.2
                activityToday = states[2]
                activityList.append(states[2])

        elif activityToday == states[1]:
            # Get the index of the starting state
            index = states.index(activityToday)

            # Randomly choose the next state based on the transition probabilities
            change = np.random.choice(transitionName[index], replace=True, p=transitionMatrix[index])

            # Update the activityToday and activityList variables
            if change == transitionName[index][1]:
                prob = prob * 0.6
                activityList.append(activityToday)
            elif change == transitionName[index][0]:
                prob = prob * 0.1
                activityToday = states[0]
                activityList.append(states[0])
        
        i += 1

    return activityList

st.image('graph.png')

st.title("Markov Chain Program for Joven's Mother's Cooking")

st.write("Joven's Mother usually cooks one of his favorite dishes every time he is feeling down. She either goes for a Mechado, Adobo or Lumpiang Shanghai. From his memory, if she cooks Adobo for that day. The next day it is 60% likely she will go for a Lumpiang Shanghai, 20% she will cook Mechado the next day and 20% chance she will recook Adobo. When she cooks Lumpiang Shanghai for that day, there is a 60% chances she'll go for a Lumpiang Shanghai again the next day, 30% chance for adobo and only 10% chances she'll Mechado the next day. Finally, when she cooks a Mechado on that day, there is a mere 10% chance she continues to have Mechado the next day as well, 70% she is likely to go for a Lumpiang Shanghai and 20% chance that she goes for an Adobo the next day.")

# Get user input for starting and ending states
starting_state = st.selectbox("What's the dish for today?", ("Adobo", "Shanghai", "Mechado"))
ending_state = st.selectbox("What dish do you want to cook?", ("Adobo", "Shanghai", "Mechado"))

# Get user input for the number of days
days = st.slider("Enter the number of days: ", 1, 10, 3)

iterations = 10000

if st.button("Predict"):
    # Count the number of simulations that end in the desired state
    count = 0

    for _ in range(iterations):
        activity_list = activity_forecast(starting_state, ending_state, days)
        if activity_list is not None:
            count += 1

    # Calculate the probability
    probability = (count / iterations) * 100

    st.write("The probability of cooking {} and cooking {} after {} days is {:.2f}%.".format(starting_state, ending_state, days, probability))

    # Calculate the ending state
    count = 0

    for _ in range(iterations):
        ending_state = get_ending_state(starting_state, days)
        if ending_state is not None:
            count += 1

    st.write("Most probably, Joven's mother will cook {} after {} days.".format(ending_state[-1], days))