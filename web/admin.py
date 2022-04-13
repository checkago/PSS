from django.contrib import admin
from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect

from web.models import News, Category, Gallery


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_filter = ['parent_category']


admin.site.register(Category, CategoryAdmin)


class ChangeCategoryForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label=u'Основная категория')


def move_to_category(modeladmin, request, queryset):
    form = None

    if 'apply' in request.POST:
        form = ChangeCategoryForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']

            count = 0
            for item in queryset:
                item.category = category
                item.save()
                count += 1

            modeladmin.message_user(request, "Категория %s применена к %d галерее." % (category, count))
            return HttpResponseRedirect(request.get_full_path())

    if not form:
        form = ChangeCategoryForm(initial={'_selected_action': queryset.values_list('id', flat=True)})

    return render(request, 'change_category.html',
                  {'items': queryset, 'form': form, 'title': u'Изменение категории'})


move_to_category.short_description = u"Изменить категорию"


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('category', 'image')
    list_filter = ['category']

    actions = [move_to_category, ]

    def change_category(self, request, queryset):
        queryset.update(category=request.Gallery.category)

    change_category.short_description = "Изменить категорию"


admin.site.register(News, NewsAdmin)
admin.site.register(Gallery, GalleryAdmin)
