from Common_Utility.LLM import GroqLLM

class GenerateUserStory:
    """
    Handles user story generation and refinement using the LLM.
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

    def review_user_story(self, user_story, feedback):
        """
        Reviews and refines the user story based on human feedback.

        Args:
            user_story (str): The original user story.
            feedback (str): Human feedback for refinement.

        Returns:
            str: The refined user story.
        """
        prompt = f"Refine the following user story based on this feedback:\n\nUser Story:\n{user_story}\n\nFeedback:\n{feedback}\n\nRefined User Story:"
        refined_story = self.llm.call_llm(prompt)
        return refined_story.strip() if refined_story else user_story
