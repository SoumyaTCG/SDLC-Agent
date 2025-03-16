import streamlit as st

class LoadStreamlitUI:
    """
    Handles loading the user input via Streamlit UI.
    """

    def load_streamlit_ui(self):
        """
        Loads the UI components and captures user input.

        Returns:
            dict: User input including API key, model, and selected SDLC phase.
        """
        st.sidebar.title("SDLC Agent Configuration")

        # Initialize session state to retain inputs
        if "GROQ_API_KEY" not in st.session_state:
            st.session_state["GROQ_API_KEY"] = ""
        if "selected_groq_model" not in st.session_state:
            st.session_state["selected_groq_model"] = "mixtral-8x7b"
        if "selected_usecase" not in st.session_state:
            st.session_state["selected_usecase"] = "Requirement Gathering"

        # API Key Input
        st.session_state["GROQ_API_KEY"] = st.sidebar.text_input(
            "Enter Groq API Key:", 
            value=st.session_state["GROQ_API_KEY"], 
            type="password"
        )
        if not st.session_state["GROQ_API_KEY"]:
            st.sidebar.warning("Groq API Key is required.")

        # Model Selection
        st.session_state["selected_groq_model"] = st.sidebar.selectbox(
            "Select Groq Model:",
            ["mixtral-8x7b", "llama3-8b", "llama3-70b"],
            index=["mixtral-8x7b", "llama3-8b", "llama3-70b"].index(st.session_state["selected_groq_model"])
        )

        # SDLC Phase Selection
        st.session_state["selected_usecase"] = st.sidebar.selectbox(
            "Select SDLC Phase:",
            ["Requirement Gathering", "Design", "Development", "Testing", "Deployment", "Maintenance"],
            index=[
                "Requirement Gathering", "Design", "Development", 
                "Testing", "Deployment", "Maintenance"
            ].index(st.session_state["selected_usecase"])
        )

        # Prepare user input dictionary (return even if some fields are missing)
        user_input = {
            "GROQ_API_KEY": st.session_state["GROQ_API_KEY"],
            "selected_groq_model": st.session_state["selected_groq_model"],
            "selected_usecase": st.session_state["selected_usecase"]
        }

        return user_input
