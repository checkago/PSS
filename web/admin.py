from django.contrib import admin

from web.models import News, Category, Gallery


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('category', 'image')
    list_filter = ['category']


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Gallery, GalleryAdmin)
