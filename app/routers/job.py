from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from models.job import Job, JobCreate, JobUpdate
from db import SessionDep

job_router = APIRouter()


@job_router.get("/jobs", tags=["Jobs"], response_model=list[JobCreate])
async def get_jobs(session: SessionDep):
    return session.exec(select(JobCreate)).all()


@job_router.get("/jobs/{job_id}", tags=["Jobs"], response_model=JobCreate)
async def get_job(job_id: int, session: SessionDep):
    job_db = session.get(JobCreate, job_id)
    if not job_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not exists"
        )
    return job_db


@job_router.patch(
    "/jobs/{job_id}",
    tags=["Jobs"],
    response_model=JobCreate,
    status_code=status.HTTP_201_CREATED,
)
async def update_job(job_id: int, job_data: JobUpdate, session: SessionDep):
    job_db = session.get(JobCreate, job_id)
    if not job_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not exists"
        )
    job_data_dict = job_data.model_dump(exclude_unset=True)
    job_db.sqlmodel_update(job_data_dict)
    session.add(job_db)
    session.commit()
    session.refresh(job_db)
    return job_db


@job_router.post("/jobs", tags=["Jobs"], response_model=JobCreate)
async def create_job(job_data: Job, session: SessionDep):
    job = JobCreate.model_validate(job_data.model_dump())
    session.add(job)
    session.commit()
    session.refresh(job)
    return job


@job_router.delete("/jobs/{job_id}", tags=["Jobs"])
async def delete_job(job_id: int, session: SessionDep):
    job_db = session.get(JobCreate, job_id)
    if not job_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not exists"
        )
    session.delete(job_db)
    session.commit()
    return {"detail": "Ok"}
