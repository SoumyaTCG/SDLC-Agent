from Common_Utility.LLM import GroqLLM

class GenerateUserStory:
    """
    Handles user story generation using the LLM.
    """
    def __init__(self, llm):
        self.llm = llm

    def generate(self, requirement):
        """
        Generates user stories from the provided requirement.

        Args:
            requirement (str): User-provided requirement.

        Returns:
            list: List of generated user stories.
        """
        prompt = f"Generate user stories based on the following requirement:\n{requirement}\n\nUser Stories:"
        response = self.llm.call_llm(prompt)
        user_stories = response.split("\n") if response else []
        return user_stories
