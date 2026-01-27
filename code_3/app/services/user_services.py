from app.repositories.user_repo import create_user_repo, get_all_users_repo


async def create_user_service(db, user):
    # later we will hash password here
    return await create_user_repo(db, user)


async def get_users_service(db):
    return await get_all_users_repo(db)
