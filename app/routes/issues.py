from fastapi import APIRouter, HTTPException, status
import uuid
from app.routes.schemas import IssueCreate,IssueOut, IssueUpdate
from app.routes.storage import load_data, save_data
router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/issues", response_model=list[IssueOut])
async def get_issues():
    """Retrieve all issues from load_data fucntion"""
    issues = load_data()
    return issues

@router.post("/create", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
async def create_issue(payload:IssueCreate):
    """Create an issue"""
    issues = load_data()
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority,
        "status": "open"
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
    """Retrieve a specific issue"""
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue Not Found")

@router.put("/update/{issue_id}", response_model=IssueOut)
async def update_issue(payload:IssueUpdate, issue_id:str):
    """Updates an issue"""
    issues = load_data()
    for index, issue in enumerate(issues):
        if(issue["id"] == issue_id):
            updated_issue = issue.copy()
            if(payload.title is not None):
                updated_issue["title"] = payload.title
            if(payload.description is not None):
                updated_issue["description"] = payload.description

            if(payload.priority is not None):
                updated_issue["priority"] = payload.priority

            if(payload.status is not None):
                updated_issue["status"] = payload.status
            issues[index] = updated_issue
            save_data(issues)
            return updated_issue

    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue Not Found")

@router.delete("/{issue_id}")
def delete_issue(issue_id: str):
    """Delete an issue"""
    issues = load_data()
    for index, issue in enumerate(issues):
        if(issue["id"] == issue_id):
            issues.pop(index)
            save_data(issues)
            return {"Message": "Issue Deleted Successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue Not Found")
