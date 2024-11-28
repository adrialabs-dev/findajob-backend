from sqlmodel import SQLModel, Field

class Job(SQLModel):
    datePosted: str = Field(default=None)
    url: str | None = Field(default=None)
    source: str | None = Field(default=None)
    jobTitle: str | None = Field(default=None)
    jobDescription: str | None = Field(default=None)
    skills: str | None = Field(default=None)
    contractType: str | None = Field(default=None)
    workSchedule: str | None = Field(default=None)
    seniority: str | None = Field(default=None)
    subscriptionType: str | None = Field(default=None)
    companyName: str | None = Field(default=None)
    jobLocation: str | None = Field(default=None)
    salaryRange: str | None = Field(default=None)
    contactEmail: str | None = Field(default=None)
    postedBy: str | None = Field(default=None)

class JobCreate(Job, table=True):
    id: int | None = Field(default=None, primary_key=True)

class JobUpdate(Job):
    pass