from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailAuthBackend(object):
    """ Авторизация по почте """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

class PhoneAuthBackend(object):
    """ Авторизация по телефону """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(phone=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None