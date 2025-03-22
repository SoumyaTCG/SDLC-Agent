from Common_Utility.LLM import GroqLLM

class GenerateDesignSpecification:
    """
    Handles design specification generation and refinement using the LLM.
    """
    def __init__(self, llm):
        self.llm = llm

    def generate_design(self, user_stories):
        """
        Generates design specifications from user stories.

        Args:
            user_stories (list): List of user stories.

        Returns:
            str: Generated design specification.
        """
        prompt = f"Generate a design specification based on the following user stories:\n{user_stories}\n\nDesign Specification:"
        response = self.llm.call_llm(prompt)
        return response if response else "No design specification generated."

    def review_design_specification(self, design_specification, feedback):
        """
        Reviews and refines the design specification based on human feedback.

        Args:
            design_specification (str): The original design specification.
            feedback (str): Human feedback for refinement.

        Returns:
            str: The refined design specification.
        """
        prompt = f"Refine the following design specification based on this feedback:\n\nDesign Specification:\n{design_specification}\n\nFeedback:\n{feedback}\n\nRefined Design Specification:"
        refined_spec = self.llm.call_llm(prompt)
        return refined_spec.strip() if refined_spec else design_specification
