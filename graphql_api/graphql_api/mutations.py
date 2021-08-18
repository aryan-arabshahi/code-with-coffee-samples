from graphene import ObjectType, Mutation, String
from graphql_api.datatypes import User


class CreateUser(Mutation):

    Output = User

    class Arguments:
        full_name = String(required=True)
        username = String(required=True)
        email = String(required=True)

    def mutate(self, info, full_name: str, username: str, email: str) -> User:
        return User(
            full_name=full_name,
            username=username,
            email=email
        )


class Mutation(ObjectType):

    create_user = CreateUser.Field()
