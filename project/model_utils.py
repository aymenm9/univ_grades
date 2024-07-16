def get_id(user_obj):
    '''
    return user_id and user_type
    user_type: Admin, Teacher, Student class or none
    '''
    if user_obj is None:
        return None
    user = f'{user_obj.id},{user_obj.__class__.__name__}'
    return user
