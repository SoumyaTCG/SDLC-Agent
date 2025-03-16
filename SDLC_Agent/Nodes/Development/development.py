from Common_Utility.LLM import GroqLLM

class GenerateCode:
    """
    Handles code generation using the LLM.
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
        prompt = f"Generate code based on the following design specification:\n{design_specification}"
        response = self.llm.call_llm(prompt)
        return response if response else "No code generated."
