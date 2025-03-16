import streamlit as st
from Nodes import agent

st.title("SDLC AI Agent - Requirement Gathering")

# User input for requirements
agent.state.requirement = st.text_area("Describe the requirements in detail:", "")

if st.button("Generate User Stories"):
    if agent.state.requirement.strip():
        agent.run("generate")
        st.session_state['user_stories'] = agent.state.user_stories
    else:
        st.error("Please provide detailed requirements.")

# Display generated user stories
if 'user_stories' in st.session_state:
    st.header("Generated User Stories")
    for i, story in enumerate(st.session_state['user_stories']):
        st.write(f"{i + 1}. {story}")

# Feedback and refinement
agent.state.feedback = st.text_area("Provide feedback or suggest changes:", "")

if st.button("Refine User Stories"):
    if agent.state.feedback.strip():
        agent.run("refine")
        st.session_state['user_stories'] = agent.state.user_stories
        st.success("User stories refined based on feedback.")
    else:
        st.error("Please provide feedback.")
