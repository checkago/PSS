from django.contrib import admin
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from ckeditor.widgets import CKEditorWidget

from web.models import News, Category, Gallery, Feedback, Vacancy


class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

    class Meta:
        verbose_name = 'Текст'
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = NewsAdminForm
    list_display = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_category')
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


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'email', 'phone', 'text')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'lastname', 'email', 'phone', 'resume', 'letter')


admin.site.register(News, NewsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Vacancy, VacancyAdmin)