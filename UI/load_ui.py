import streamlit as st

class LoadStreamlitUI:
    """
    Handles loading the user input via Streamlit UI.
    """

    def load_streamlit_ui(self):
        """
        Loads the UI components and captures user input.

        Returns:
            dict: User input including API key and selected model.
        """
        st.sidebar.title("SDLC Agent Configuration")

        # Initialize session state to retain inputs
        st.session_state.setdefault("GROQ_API_KEY", "")
        st.session_state.setdefault("selected_groq_model", "gemma2-9b-it")

        # API Key Input
        st.session_state["GROQ_API_KEY"] = st.sidebar.text_input(
            "Enter Groq API Key:", 
            value=st.session_state["GROQ_API_KEY"], 
            type="password"
        )
        if not st.session_state["GROQ_API_KEY"]:
            st.sidebar.warning("Groq API Key is required.")
            st.sidebar.markdown("Select a model from the dropdown below:")
        # Model Selection
        st.session_state["selected_groq_model"] = st.sidebar.selectbox(
            "Select Groq Model:",
            ["gemma2-9b-it","llama-3.3-70b-versatile"],
            index=["gemma2-9b-it","llama-3.3-70b-versatile"].index(st.session_state["selected_groq_model"])
        )

        # Prepare user input dictionary
        user_input = {
            "GROQ_API_KEY": st.session_state["GROQ_API_KEY"],
            "selected_groq_model": st.session_state["selected_groq_model"]
        }

        return user_input