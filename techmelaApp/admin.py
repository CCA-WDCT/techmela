from django.contrib import admin
from .models import Project, ProjectScore, CustomUser, ProjectLike
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_judge')
    fieldsets = (
        (None,
         {'fields': ('email', 'username', 'password', 'is_judge')}),)


admin.site.register(CustomUser, CustomUserAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'likes')


admin.site.register(Project, ProjectAdmin)


class ProjectScoreAdmin(admin.ModelAdmin):
    list_display = ('project', 'score', 'judgedBy', 'created')


admin.site.register(ProjectScore, ProjectScoreAdmin)

class ProjectLikeAdmin(admin.ModelAdmin):
    list_display = ('project', 'likedBy')


admin.site.register(ProjectLike, ProjectLikeAdmin)
