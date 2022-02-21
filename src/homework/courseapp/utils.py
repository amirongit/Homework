def generate_user_type_test(type):
    def user_type_is(user):
        if user.is_authenticated and user.user_type == type:
            return True
        return False
    return user_type_is
