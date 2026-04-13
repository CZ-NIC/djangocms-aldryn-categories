from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from parler.admin import TranslatableAdmin

from treebeard.admin import TreeAdmin

from .forms import CategoryAdminForm
from .models import Category


class CategoryAdmin(TranslatableAdmin, TreeAdmin):
    form = CategoryAdminForm

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
            )
        }),
        (_('Advanced options'), {
            'fields': (
                'treebeard_position',
                'treebeard_ref_node',
                'attributes',
            )
        }),
    )
    list_display = ['name', 'attributes_string']

    @admin.display(description=_("Attributes"))
    def attributes_string(self, obj):
        return obj.attributes_str()


admin.site.register(Category, CategoryAdmin)
