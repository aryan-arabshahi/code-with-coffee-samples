from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from graphene import Schema
from graphql_api.mutations import Mutation
from graphql_api.queries import Query


class GraphQLApp:

    def __init__(self):

        self._flask_app = Flask(__name__)

        CORS(self._flask_app)

        schema = Schema(query=Query, mutation=Mutation)

        self._flask_app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view(
                'graphql',
                schema=schema,
                graphiql=True
            )
        )

    def run(self) -> None:
        self._flask_app.run(host='0.0.0.0', port=5000)
