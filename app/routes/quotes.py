from fastapi import APIRouter, HTTPException, status, Depends
from typing import Optional, List
from ..config import db_connection
from bson import json_util
import json
from .. import schemas
from ..auth.auth import validate_api_key

router = APIRouter(
    prefix='/quotes'
)

@router.get('/random', response_model=List[schemas.Quote] )
async def random_quote(limit: Optional[int]=1, api_key: str = Depends(validate_api_key)):
    try:
        db_conn =db_connection()
        quotes = db_conn.db_quotes.quotes
        quote = quotes.aggregate([{ '$sample': { 'size': limit} }, { '$project': { '_id': 0 } }])
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)
    finally:
        db_conn.close()
    return json.loads(json_util.dumps(quote))