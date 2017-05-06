from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)


# Update the registeration to include this customised interfac
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Page)

# Update the registeration to include this customised interface


