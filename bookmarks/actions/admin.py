from django.contrib import admin

from .models import Actions


class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'vebr', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('vebr',)


admin.site.register(Actions, ActionAdmin)
