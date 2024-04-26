from django.contrib import admin

from .models import Slide, Slider

# Register your models here.


class SlideInline(admin.TabularInline):
    model = Slide
    extra = 0


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [SlideInline]
