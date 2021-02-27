from datetime import timedelta
from typing import Any, List, Optional

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import schemas
from app.services import (
    authenticate_user,
    create_access_token,
    create_user,
    get_current_active_user,
    get_db,
    get_posts_by_userid,
    get_user_by_email,
    get_user_by_id,
    get_user_by_username,
    get_users,
    update_user,
)
from app.services.security import ACCESS_TOKEN_EXPIRE_MINUTES

router: Any = APIRouter(
    tags=["users"],
    responses={404: {"Description": "Not found"}},
)


@router.post(
    "/users",
    response_model=schemas.User,
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
)
def create_new_user(
    user: schemas.UserCreate, db: Session = Depends(get_db)
) -> Any:
    db_username = get_user_by_username(db, username=user.username)
    db_email = get_user_by_email(db, email=user.email)
    if db_username:
        raise HTTPException(
            status_code=400, detail="Username already registered"
        )
    elif db_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get(
    "/users",
    response_model=Page[schemas.Users],
    dependencies=[Depends(pagination_params)],
)
def list_users(db: Session = Depends(get_db)) -> List:
    """
    List all users
    """
    users = get_users(db=db)
    return paginate(users)


@router.get("/users/user", response_model=schemas.User)
def read_user(
    username: Optional[str] = None,
    user_id: Optional[int] = None,
    db: Session = Depends(get_db),
) -> Any:
    """
    Get data about user
    """
    if username:
        db_user = get_user_by_username(db=db, username=username)
    elif user_id:
        db_user = get_user_by_id(db=db, user_id=user_id)
    else:
        raise HTTPException(status_code=404, detail="User not found")

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/token", response_model=schemas.Token)
def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    """
    Generate a token to access endpoints
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get(
    "/users/me/posts",
    response_model=Page[schemas.Posts],
    dependencies=[Depends(pagination_params)],
)
def read_own_posts(
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> List:
    """
    Get own posts
    """
    user_id = current_user.id
    user_posts = get_posts_by_userid(db, user_id)
    return paginate(user_posts)


@router.put(
    "/users/{username}",
    response_model=schemas.User,
    response_model_exclude_none=True,
)
def update_user_data(
    username: str,
    user: schemas.user.UserUpdate,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> Any:
    """
    The password field is optional
    """
    if username != current_user.username:
        raise HTTPException(status_code=403, detail="Don't have permission")

    result = update_user(db, user, username)

    return result
