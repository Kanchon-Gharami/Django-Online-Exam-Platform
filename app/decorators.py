from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def studentRequired(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='app:index'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.isStudent,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# QuestionSetter varified check
def questionSetterCheck(user):
    try:
        return user.is_authenticated and user.isQuestionSetter
        # and user.questionsetter_releted_user.isVarified
    except AttributeError:
        return False

def questionSetterRequired(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='app:index'):
    actual_decorator = user_passes_test(
        questionSetterCheck,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator



def adminRequired(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='app:index'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.isAdmin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def superuserRrequired(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='app:index'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
