from pydantic import BaseModel, Field
from typing import List

class SDLCState(BaseModel):
    """
    Represents the state for the entire SDLC process using Pydantic BaseModel.
    """
    requirement: str = Field(default="", description="Requirements for the project.")
    feedback: str = Field(default="", description="User feedback for refining user stories.")
    user_stories: str = Field(default_factory=list, description="Generate user stories.")
    design_specification: str = Field(default="", description="Generated design specification.")
    code: str = Field(default="", description="Generated code.")
    test_cases: str = Field(default="", description="Generated Test Cases.")
    deployment_status: str = Field(default="", description="Deployment status.")

