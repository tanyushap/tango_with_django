

# Register your models here.

from django.contrib import admin
from models import Category, Page
from rango.models import UserProfile

#class PageAdmin(admin.ModelAdmin) :
   # list_display = ('title', 'category', 'url')

#admin.site.register(Category)
#admin.site.register(Page,PageAdmin)


# Add in this class to customize the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)

admin.site.register(UserProfile)

