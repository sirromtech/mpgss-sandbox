# application/permissions.py

from django.contrib.auth.decorators import user_passes_test

def can_view_selection_media(user) -> bool:
    if not user.is_authenticated:
        return False
    if user.is_superuser or user.is_staff:
        return True
    return user.groups.filter(name="Scholarship Officers").exists()

def can_view_documents(user) -> bool:
    if not user.is_authenticated:
        return False
    if user.is_superuser or user.is_staff:
        return True
    return user.groups.filter(name="Scholarship Officers").exists()
