from django.contrib import admin

from .models import Birthday, Tag

admin.site.empty_value_display = 'Не задано'


class TagAdmin(admin.ModelAdmin):

    list_display = (
        'tag',
    )


class BirthdayAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'birthday',
        'image'
    )

    list_editable = (
        'birthday',
        'image',
    )

    search_fields = ('first_name',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Birthday, BirthdayAdmin)
