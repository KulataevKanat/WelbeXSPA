from django.urls import path
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

from api.authentication import SafeJWTAuthentication
from api.permissions.permission import ROLE_ADMIN, ROLE_USER, UserPermissionsObj, AllowAnyGroups
from api.views import UserViews, GroupViews, ObjectViews

allow_any = AllowAny
admin = ROLE_ADMIN
user = ROLE_USER
any_groups = AllowAnyGroups
own_object = UserPermissionsObj

urlpatterns = [
    # USERS
    path("user/access_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.AccessToken)).as_view()),
    path("user/refresh_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.RefreshToken)).as_view()),
    path("user/create_user/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.CreateUserView)).as_view()),
    path("user/create_super_user/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.CreateSuperUserView)).as_view()),
    path("user/delete_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.DeleteUserByIdView)).as_view()),
    path("user/delete_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.DeleteAllUsersView)).as_view()),
    path("user/update_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.UpdateUserView)).as_view()),
    path("user/find_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.GetUserView)).as_view()),
    path("user/find_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(UserViews.FindUserByIdView)).as_view()),

    # GROUPS
    path("group/create_group/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(GroupViews.CreateGroupView)).as_view()),
    path("group/delete_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(GroupViews.DeleteGroupByIdView)).as_view()),
    path("group/update_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(GroupViews.UpdateGroupByIdView)).as_view()),
    path("group/find_all_groups/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(GroupViews.GetGroupView)).as_view()),
    path("group/find_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(GroupViews.FindGroupByIdView)).as_view()),

    # OBJECT
    path("object/create_object/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(ObjectViews.CreateObjectView)).as_view()),
    path("object/delete_object_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(ObjectViews.DeleteObjectByIdView)).as_view()),
    path("object/update_object_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(ObjectViews.UpdateObjectByIdView)).as_view()),
    path("object/find_all_objects/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(ObjectViews.GetObjectView)).as_view()),
    path("object/find_object_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([allow_any])(ObjectViews.FindObjectByIdView)).as_view()),
]
