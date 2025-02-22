from django.contrib.auth.decorators import user_passes_test

def provider_required(view_func):
    def test(user):
        return user.roles == "provider"
    return user_passes_test(test)(view_func)

def patient_required(view_func):
    def test(user):
        return user.roles == "patient"
    return user_passes_test(test)(view_func)
            