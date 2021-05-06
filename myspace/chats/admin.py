from django.contrib import admin

# Register your models here.
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # readonly_fields = ('id',)
    fields = ('name', 'archived', )
    actions = ('archive',)

    list_filter = ('archived',)

    def archive(self, request, queryset):
        for room in queryset:
            room.archived = True
            room.save()