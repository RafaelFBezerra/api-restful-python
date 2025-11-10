from datetime import datetime, timedelta, timezone
from typing import Annotated

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from utils.constants import TOKEN_AUTH, ENCODER_DECODER_ALGORITHM, TOKEN_EXPIRES_MINUTES, USERS_DB


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/token") 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, TOKEN_AUTH, algorithm=ENCODER_DECODER_ALGORITHM)
    return encoded_jwt

def get_user(username: str):
    if username in USERS_DB:
        user_dict = USERS_DB[username]
        return user_dict
    return None

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, TOKEN_AUTH, algorithms=[ENCODER_DECODER_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = {"username": username, "role": payload.get("role")}
    except JWTError:
        raise credentials_exception
    
    user = get_user(token_data["username"])
    if user is None:
        raise credentials_exception
    return user

def requires_role(role: str):
    def role_checker(user: dict = Depends(get_current_user)):
        if user.get("role") != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acesso Proibido. Requer a role: {role}",
            )
        return user
    return role_checker

async def token_endpoint(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = get_user(form_data.username)
    print(user['hashed_password'])
    if not user or not verify_password(form_data.password, pwd_context.hash(user["hashed_password"])):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nome de usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=TOKEN_EXPIRES_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"], "role": user["role"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
