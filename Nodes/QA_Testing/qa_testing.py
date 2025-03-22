import pytest
import tempfile
import os
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

    def execute_test_cases(self, test_code, generated_code):
        """
        Executes the test cases on the generated code.

        Args:
            test_code (str): The test script (pytest/unittest).
            generated_code (str): The code to be tested.

        Returns:
            dict: Test results with pass/fail status.
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save the generated code and test code as Python files
            code_file = os.path.join(temp_dir, "generated_code.py")
            test_file = os.path.join(temp_dir, "test_script.py")

            with open(code_file, "w") as f:
                f.write(generated_code)

            with open(test_file, "w") as f:
                f.write(test_code)

            # Run pytest on the test file
            result = os.system(f"pytest {test_file} --tb=short > {temp_dir}/output.log")

            # Read the test output
            with open(f"{temp_dir}/output.log", "r") as f:
                test_output = f.read()

        return {"status": "Success" if result == 0 else "Failed", "output": test_output}
