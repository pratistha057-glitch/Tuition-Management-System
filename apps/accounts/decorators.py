def is_admin(user):
    return (
        user.is_authenticated
        and hasattr(user, 'userprofile')
        and user.userprofile.role == 'ADMIN'
    )


def is_teacher(user):
    return (
        user.is_authenticated
        and hasattr(user, 'userprofile')
        and user.userprofile.role == 'TEACHER'
    )


def is_student(user):
    return (
        user.is_authenticated
        and hasattr(user, 'userprofile')
        and user.userprofile.role == 'STUDENT'
    )


def is_admin_or_teacher(user):
    return (
        user.is_authenticated
        and hasattr(user, 'userprofile')
        and user.userprofile.role in ['ADMIN', 'TEACHER']
    )