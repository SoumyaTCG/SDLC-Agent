from Common_Utility.LLM import GroqLLM

class GenerateTestCases:
    """
    Handles test case generation using the LLM.
    """
    def __init__(self, llm):
        self.llm = llm

    def generate_test_cases(self, security_reviewed_code):
        """
        Generates test cases from security-reviewed code.

        Args:
            security_reviewed_code (str): The code that has passed security review.

        Returns:
            str: Generated test cases.
        """
        prompt = f"""
        Generate unit, integration, and security test cases for the following security-reviewed code:
        {security_reviewed_code}
        """
        response = self.llm.call_llm(prompt)
        return response if response else "No test cases generated."

    def fix_test_cases(self, test_cases, feedback):
        """
        Fixes test cases based on human feedback.

        Args:
            test_cases (str): The initially generated test cases.
            feedback (str): Human-provided feedback on test cases.

        Returns:
            str: Improved test cases.
        """
        prompt = f"""
        Here are some test cases:
        {test_cases}
        
        Based on the following feedback, improve the test cases:
        {feedback}
        """
        response = self.llm.call_llm(prompt)
        return response if response else "No improvements made to test cases."
