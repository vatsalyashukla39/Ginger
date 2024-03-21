import streamlit as st
import pandas as pd
import random
import requests

data = {
    "Name": ["John", "Emily", "David", "Sophia", "Michael", "Olivia", "Daniel", "Emma", "Ethan", "Ava"],
    "Age": [25, 28, 22, 26, 30, 27, 29, 24, 31, 23],
    "Bio": [
        "I love hiking and exploring new places!",
        "Coffee lover ☕️. Travel enthusiast ✈️.",
        "Musician 🎸. Movie buff 🎬.",
        "Foodie 🍔. Dog person 🐶.",
        "Tech geek 💻. Gamer 🎮.",
        "Fitness freak 💪. Yoga lover 🧘.",
        "Bookworm 📚. Nature lover 🌿.",
        "Art enthusiast 🎨. Photographer 📷.",
        "Food blogger 🍲. Cooking is my passion! 🍳",
        "Animal lover 🐾. Volunteer at local shelter 🏠."
    ]
}

profiles_df = pd.DataFrame(data)

def get_random_images(count):
    access_key = 'ssXcjdhTO8FnFxbNEaMlySDsFooZ9c-xP2z4DAX2gWQ'
    images = []
    for _ in range(count):
        try:
            response = requests.get("https://api.unsplash.com/photos/random", params={"client_id": access_key})
            if response.status_code == 200:
                images.append(response.json()["urls"]["regular"])
            else:
                st.warning("Failed to fetch image")
                images.append("https://via.placeholder.com/200")
        except Exception as e:
            st.error(f"Error fetching image: {e}")
            images.append("https://via.placeholder.com/200")
    return images

def display_profile(profile):
    st.subheader(profile['Name'])
    st.write(f"Age: {profile['Age']}")
    st.write(f"Bio: {profile['Bio']}")
    images = get_random_images(3)
    for image_url in images:
        st.image(image_url, use_column_width=True)

def main():
    st.title("Ginger - Find your match!")

    st.sidebar.title("Filter Profiles")
    min_age = st.sidebar.slider("Minimum Age", min_value=18, max_value=50, value=20)
    max_age = st.sidebar.slider("Maximum Age", min_value=18, max_value=50, value=35)

    filtered_profiles = profiles_df[(profiles_df['Age'] >= min_age) & (profiles_df['Age'] <= max_age)]

    st.subheader("Profiles")

    if st.button("Next Profile", key='next_button'):
        if len(filtered_profiles) > 0:
            current_profile = random.choice(filtered_profiles.to_dict('records'))
            display_profile(current_profile)
        else:
            st.warning("No profiles match the selected criteria.")

    st.markdown(
"""
        <style>
        .css-1bnyegh {
            position: fixed;
            right: 50px;
            top: 50%;
            transform: translateY(-50%);
        }
        </style>
  """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
