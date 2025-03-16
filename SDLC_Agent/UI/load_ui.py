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

        # API Key Input
        groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")
        if not groq_api_key:
            st.sidebar.warning("Groq API Key is required.")

        # Model Selection
        selected_groq_model = st.sidebar.selectbox(
            "Select Groq Model:",
            ["mixtral-8x7b", "llama3-8b", "llama3-70b"]
        )

        # SDLC Phase Selection
        selected_usecase = st.sidebar.selectbox(
            "Select SDLC Phase:",
            ["Requirement Gathering", "Design", "Development", "Testing", "Deployment", "Maintenance"]
        )

        if not selected_usecase:
            st.sidebar.warning("Please select an SDLC phase.")

        # If all inputs are filled, return as a dictionary
        if groq_api_key and selected_groq_model and selected_usecase:
            return {
                "GROQ_API_KEY": groq_api_key,
                "selected_groq_model": selected_groq_model,
                "selected_usecase": selected_usecase
            }
        else:
            return None
