from rest_framework import permissions
from authentication.permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
