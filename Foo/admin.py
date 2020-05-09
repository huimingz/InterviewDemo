from django.contrib import admin

from Foo import models

# Register your models here.


admin.site.register(models.Course)
admin.site.register(models.Unit)
admin.site.register(models.Chapter)
admin.site.register(models.Category)
admin.site.register(models.GiftCategory)
