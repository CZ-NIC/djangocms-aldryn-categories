from django.contrib import admin

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
        (' ', {
            'fields': (
                'treebeard_position',
                'treebeard_ref_node',
            )
        }),
    )


admin.site.register(Category, CategoryAdmin)
