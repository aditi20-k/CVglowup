from pydantic import BaseModel, Field
from typing import List


class Education(BaseModel):
    institution: str
    degree: str
    period: str = Field(default="")


class Experience(BaseModel):
    role: str
    company: str
    duration: str = Field(default="")
    responsibilities: List[str] = Field(default_factory=list)


class Project(BaseModel):
    title: str
    description: str
    technologies: List[str] = Field(default_factory=list)


class CVData(BaseModel):
    name: str
    summary: str
    education: List[Education]
    experience: List[Experience]
    skills: List[str]
    projects: List[Project]
    certifications: List[str]
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]