from graphene import ObjectType, Field, List
from graphql_api.datatypes import User, Settings, NotificationStatus


class Query(ObjectType):

    users = Field(List(User))

    def resolve_users(self, info):
        return [
            User(
                full_name='Naruto Uzumaki',
                username='naruto',
                email='naruto@codewithcoffee.dev',
                settings=Settings(notifications=NotificationStatus.ENABLED, verified=True)
            ),
            User(
                full_name='Kakashi Hatake',
                username='kakashi',
                email='kakashi@codewithcoffee.dev',
            ),
        ]
