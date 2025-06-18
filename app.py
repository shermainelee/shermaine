import streamlit as st
import pandas as pd

# Load guest data
guests = pd.read_csv('guests.csv')
slug_to_guest = {row['slug']: row for _, row in guests.iterrows()}

# URL param handling
query_params = st.query_params
slug = query_params.get("guest", [None])[0]

if slug and slug in slug_to_guest:
    guest = slug_to_guest[slug]
    st.title(f"🎉 RSVP for {guest['name']}")
    st.markdown(f"**{guest['message']} {guest['emoji']}**")

    st.subheader("Can you make it?")
    attending = st.radio("RSVP:", ["Yes", "No", "Maybe"])

    if st.button("Submit"):
        st.success("RSVP received! See you soon 🎈")

        # Optionally save to CSV
        with open("rsvp_responses.csv", "a") as f:
            f.write(f"{guest['name']},{attending}\n")

else:
    st.title("Oops!")
    st.write("We couldn't find your invite. Double-check your link!")
