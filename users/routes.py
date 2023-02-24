from flask_restful import Api
from users.views import LoginApi, SignUpApi


def create_authentication_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    api.add_resource(SignUpApi, "/api/v1/auth/register/")
    api.add_resource(LoginApi, "/api/v1/auth/login/")
    # api.add_resource(ForgotPassword, "/api/auth/forgot-password/")
    # api.add_resource(ResetPassword, "/api/auth/reset-password/<token>")