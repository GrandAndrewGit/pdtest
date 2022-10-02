from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Note



class ProfileAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_active', 'date_of_birth')
    ordering = ('id',)
    search_fields = ('first_name',)
    exclude = ('username',)
    list_display_links = ('first_name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Profile, ProfileAdmin)



class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'model_id', 'action_time')
    ordering = ('action_time',)
    list_display_links = ('model_name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Note, NoteAdmin)