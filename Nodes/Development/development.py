from Common_Utility.LLM import GroqLLM

class GenerateCode:
    """
    Handles code generation and refinement using the LLM.
    """
    def __init__(self, llm):
        self.llm = llm

    def generate(self, design_specification):
        """
        Generates code from the design specification.

        Args:
            design_specification (str): Design specification.

        Returns:
            str: Generated code.
        """
        prompt = f"Generate high-quality, modular, and well-documented code based on the following design specification:\n\n{design_specification}\n\nCode:"
        response = self.llm.call_llm(prompt)
        return response.strip() if response else "No code generated."

    def review_code(self, code, feedback):
        """
        Reviews and refines the generated code based on human feedback.
        Ensures improvements in readability, efficiency, modularity, and adherence to best practices.

        Args:
            code (str): The generated code.
            feedback (str): Human feedback for improvement.

        Returns:
            str: The refined code.
        """
        prompt = (
            "Analyze and refine the following code based on the provided feedback.\n"
            "Ensure the improvements align with best coding practices, maintain efficiency, "
            "and enhance readability and modularity.\n\n"
            f"Code:\n{code}\n\n"
            f"Feedback:\n{feedback}\n\n"
            "Provide the improved code without additional explanations:\n"
        )
        refined_code = self.llm.call_llm(prompt)
        return refined_code.strip() if refined_code else code
