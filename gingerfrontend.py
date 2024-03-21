import streamlit as st
import pandas as pd
import random

# Sample data for profiles
data = {
    "Name": ["John", "Emily", "David", "Sophia", "Michael"],
    "Age": [25, 28, 22, 26, 30],
    "Bio": [
        "I love hiking and exploring new places!",
        "Coffee lover ☕️. Travel enthusiast ✈️.",
        "Musician 🎸. Movie buff 🎬.",
        "Foodie 🍔. Dog person 🐶.",
        "Tech geek 💻. Gamer 🎮."
    ]
}

profiles_df = pd.DataFrame(data)

# Function to display a profile
def display_profile(profile):
    st.subheader(profile['Name'])
    st.write(f"Age: {profile['Age']}")
    st.write(f"Bio: {profile['Bio']}")

# Main function for the app
def main():
    st.title("Ginger")

    # Sidebar
    st.sidebar.title("Filter Profiles")
    min_age = st.sidebar.slider("Minimum Age", min_value=18, max_value=50, value=20)
    max_age = st.sidebar.slider("Maximum Age", min_value=18, max_value=50, value=35)

    filtered_profiles = profiles_df[(profiles_df['Age'] >= min_age) & (profiles_df['Age'] <= max_age)]

    # Display profiles
    st.subheader("Swipe Right if you like, Left if you don't")
    profile_index = st.empty()
    profile_display = st.empty()

    if st.button("Next Profile"):
        if len(filtered_profiles) > 0:
            current_profile = random.choice(filtered_profiles.to_dict('records'))
            display_profile(current_profile)
            profile_index.text(f"Profile {profiles_df.index[profiles_df['Name'] == current_profile['Name']].tolist()[0] + 1} of {len(filtered_profiles)}")
            profile_display.image("https://via.placeholder.com/200", use_column_width=True) # Placeholder image
        else:
            st.warning("No profiles match the selected criteria.")

# Run the app
if __name__ == "__main__":
    main()
