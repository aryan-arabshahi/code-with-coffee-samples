from graphene import ObjectType, String, Field, Enum, Boolean


class NotificationStatus(Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'


class Settings(ObjectType):
    notifications = Field(NotificationStatus, default_value=NotificationStatus.DISABLED)
    verified = Boolean(default_value=False)


class User(ObjectType):
    full_name = String()
    username = String()
    email = String()
    settings = Field(Settings, default_value=Settings())
