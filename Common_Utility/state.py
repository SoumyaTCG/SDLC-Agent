from pydantic import BaseModel, Field
from typing import Dict, Tuple, List

class SDLCState(BaseModel):
    """
    Represents the state for the entire SDLC process using Pydantic BaseModel.
    This class captures the state of various phases in the SDLC process.
    """
    requirement: str = Field(default="", description="Requirements for the project.")
    feedback: str = Field(default="", description="User feedback for refining user stories.")
    user_stories: str = Field(default_factory=list, description="Generate user stories.")
    design_specification: str = Field(default="", description="Generated design specification.")
    code: str = Field(default="", description="Generated code.")
    test_cases: str = Field(default="", description="Generated Test Cases.")
    deployment_status: str = Field(default="", description="Deployment status.")
    feedback: str= Field(default="", description="Feedback for each Node.")
    evaluation: str = Field(default="", description="Evaluation of the generated code.")
