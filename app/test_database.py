from sqlalchemy import text
from app.core.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("\nDATABASE CONNECTION SUCCESSFUL\n")
        print(result.fetchone()[0])

except Exception as e:
    print("\nDATABASE CONNECTION FAILED\n")
    print(e)