
from Common_Utility.LLM import GroqLLM

class RunQATests:
    """
    Handles execution of QA test cases.
    """
    def __init__(self, llm):
        self.llm = llm

    def validate_test_cases(self, fixed_test_cases, generated_code):
        """
        Uses LLM to analyze test cases before execution.

        Args:
            fixed_test_cases (list): List of reviewed test cases.
            generated_code (str): The final generated code.

        Returns:
            str: Feedback from the LLM about the test cases.
        """
        prompt = f"""
        Analyze the following test cases for the given code:
        
        Code:
        {generated_code}

        Test Cases:
        {fixed_test_cases}

        Do the test cases cover all edge cases? Suggest improvements.
        """
        response = self.llm.call_llm(prompt)
        return response if response else "No feedback provided."

    