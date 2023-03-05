from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models.home import *
from .models.aboutus import *
from .models.studyabroad import *


admin.site.register(Images)

admin.site.register(Videos)

admin.site.register(Icons)

admin.site.register(EducationPhotos)

admin.site.register(Contacts)


@admin.register(Components)
class ComponentsAdmin(TranslatableAdmin):
    list_display = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Advantages)
class AdvatagesAdmin(TranslatableAdmin):
    list_display = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'icon'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Exams)
class ExamsAdmin(TranslatableAdmin):
    list_display = ('tag', 'name', 'description')
    fieldsets = (
        (None, {
            'fields': ('tag', 'name', 'description', 'image_one', 'image_two'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(OurTeam)
class OurTeamAdmin(TranslatableAdmin):
    list_display = ('name', 'position')
    fieldsets = (
        (None, {
            'fields': ('name', 'position', 'image'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Countries)
class CountriesAdmin(TranslatableAdmin):
    list_display = ('country', )
    fieldsets = (
        (None, {
            'fields': ('country', 'flag'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', )
    fieldsets = (
        (None, {
            'fields': ('name', ),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Specialization)
class SpecializationAdmin(TranslatableAdmin):
    list_display = ('name', )
    fieldsets = (
        (None, {
            'fields': ('name', ),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Languages)
class LanguagesAdmin(TranslatableAdmin):
    list_display = ('language', )
    fieldsets = (
        (None, {
            'fields': ('language', ),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(EducationCenters)
class CentersAdmin(TranslatableAdmin):
    list_display = ('name', 'location', 'label')
    fieldsets = (
        (None, {
            'fields': ('name', 'location', 'label', 'title', 'duratuon', 'awards', 'tuition_fee', 'application_fee',
                       'registration_fee', 'tuition', 'entry_qualification', 'semester', 'pre_deadline', 'deadline',
                       'age', 'cost', 'image_1', 'image_2', 'image_3', 'country', 'specialization', 'language',
                       'category', 'commence', 'foundation')
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)
