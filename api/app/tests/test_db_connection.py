import pytest
import sys
from pathlib import Path

# Add api directory to Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from app.db.base import Base, get_db
from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine

@pytest.mark.asyncio
async def test_db_connection():
    # 创建测试引擎
    engine = create_async_engine(settings.DATABASE_URL)
    
    try:
        # 测试连接
        async with engine.connect() as conn:
                # 执行简单查询
                from sqlalchemy import text
                result = await conn.execute(text("SELECT 1"))
                assert result.scalar() == 1
                print("Database connection test passed!")
    except Exception as e:
        pytest.fail(f"Database connection failed: {str(e)}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_db_connection())
