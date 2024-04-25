from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Activity, Company

# Register your models here.


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 1


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        for field_name in ('email', 'phone'):
            if field_name in form.base_fields:
                form.base_fields[field_name].widget.attrs.update({'dir': 'ltr'})
        return form

    inlines = [ActivityInline]
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone', 'email']
    fieldsets = [
        (None, {'fields': ['name', 'logo']}),
        (_('Contact Information'), {'fields': ['phone', 'email']}),
        (_('About Company'), {'fields': ['about']}),
    ]
