from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from .models import Base, User
from .schema import UserSchema
from .exceptions import NotFound

class UsersService:
    name = "users"

    db = DatabaseSession(Base)

    @rpc
    def create_user(self, user_data):
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            password=user_data["password"],
            project=user_data["project"],
            sa_token=user_data["sa_token"]
        )

        self.db.add(user)
        self.db.commit()

        return UserSchema().dump(user)
    
    @rpc
    def get_user(self, id):
        user = self.db.query(User).get(id)

        if not user:
            raise NotFound("User with id {0} not found".format(id))

        return UserSchema().dump(user)
    
    @rpc
    def update_user(self, id, user_data):
        user = self.db.query(User).get(id)

        for key, value in user_data.items():
            if key == "password":
                user.password = user.generate_hash(value)
            else:
                setattr(user, key, value)

        self.db.commit()

        return UserSchema().dump(user)
    
    @rpc
    def delete_user(self, id):
        user = self.db.query(User).get(id)
        self.db.delete(user)
        self.db.commit()
