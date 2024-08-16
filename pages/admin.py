from django.contrib import admin
from .models import ChildProfile
from django.utils.html import format_html

from .models import ChildProfile


class ChildProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'Child_class', 'is_orphan')
    search_fields = ('name',)
    list_filter = ('gender', 'Child_class', 'is_orphan')


admin.site.register(ChildProfile, ChildProfileAdmin)


# Display image thumbnail in the list view
def thumbnail(self, obj):
    if obj.Picture:
        return format_html(f'<img src="{obj.Picture.url}" width="50" height="50" />')
    return ""


thumbnail.short_description = "Picture"

# Customise the form layout in the admin interface
fieldsets = (
    (None, {
        'fields': ('name', 'age', 'gender', 'Child_class', 'is_orphan', 'Picture'),
    })
)
# This will enable inline editing of specific fields in the list view

list_editable = ('age', 'Child_class')

# Setting how many items to show per page

list_per_page = 10
