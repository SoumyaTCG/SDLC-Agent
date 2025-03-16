import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    """
    Utility class to handle calls to the Groq LLM using Langchain.

    Args:
        user_controls_input (dict): Dictionary containing the API key and model selection.

    Methods:
        get_llm_model: Initializes and returns the LLM model.
        call_llm: Sends a prompt to the LLM and returns the response.
    """
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        self.llm = self.get_llm_model()

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get('GROQ_API_KEY', os.getenv("GROQ_API_KEY"))
            selected_groq_model = self.user_controls_input.get('selected_groq_model')

            if not groq_api_key:
                st.error("Please enter the Groq API KEY")
                return None

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            return llm

        except Exception as e:
            raise ValueError(f"Error occurred with exception: {e}")

    def call_llm(self, prompt):
        """
        Calls the Groq LLM with the given prompt and returns the response.

        Args:
            prompt (str): The input prompt to send to the LLM.

        Returns:
            str: The output from the LLM.
        """
        try:
            response = self.llm.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            st.error(f"Failed to get response from LLM: {e}")
            return ""
