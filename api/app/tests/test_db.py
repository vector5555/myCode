import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from db.base import get_db
from models.user import User

@pytest.mark.asyncio
async def test_db_connection():
    """测试数据库连接"""
    async with get_db() as session:
        assert isinstance(session, AsyncSession)
        # 测试简单查询
        result = await session.execute("SELECT 1")
        assert result.scalar() == 1

@pytest.mark.asyncio
async def test_user_crud():
    """测试用户模型的CRUD操作"""
    async with get_db() as session:
        # 创建用户
        new_user = User(username="testuser", password_hash="testhash")
        session.add(new_user)
        await session.commit()
        
        # 读取用户
        user = await session.get(User, new_user.id)
        assert user.username == "testuser"
        
        # 更新用户
        user.username = "updateduser"
        await session.commit()
        updated_user = await session.get(User, new_user.id)
        assert updated_user.username == "updateduser"
        
        # 删除用户
        await session.delete(updated_user)
        await session.commit()
        deleted_user = await session.get(User, new_user.id)
        assert deleted_user is None
