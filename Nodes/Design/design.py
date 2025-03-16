from Common_Utility.LLM import GroqLLM

class GenerateDesignSpecification:
    """
    Handles design specification generation using the LLM.
    """
    def __init__(self, llm):
        self.llm = llm

    def generate(self, user_stories):
        """
        Generates design specifications from user stories.

        Args:
            user_stories (list): List of user stories.

        Returns:
            str: Generated design specification.
        """
        prompt = f"Generate a design specification based on the following user stories:\n{user_stories}"
        response = self.llm.call_llm(prompt)
        return response if response else "No design specification generated."
