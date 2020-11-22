from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category','get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('content', 'title',)
    list_filter = ('is_published', 'category',)
    list_editable = ('is_published',)
    fields = ('title','content', 'created_at', 'updated_at', 'is_published', 'category','view','photo','get_photo')
    readonly_fields = ('updated_at', 'created_at','view','get_photo')
    save_on_top = True

    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Управление'
admin.site.site_header = 'Управление'
