from django.contrib import admin

from .models import News,Category



class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at','is_published','photo','category')
    list_display_links = ('id','title')
    search_fields = ('content','title',)
    list_filter = ('is_published','category',)
    list_editable = ('is_published',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields = ('title',)

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)