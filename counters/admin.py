from django.contrib import admin
from .models import Counters


# Register your models here.
class CountersAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'edited']
    list_display_links = ('title',)
    search_fields = ('title',)
    # list_editable = ('title',)
    list_filter = ('published', )


admin.site.register(Counters, CountersAdmin)
