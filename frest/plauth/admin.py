from django.contrib import admin

# Register your models here.


class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('app_label', 'model')
