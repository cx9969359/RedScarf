class KeyService():
    def get_user_token_key(self, user):
        user_id = user.id
        username = user.username
        return (str(user_id) + username)
