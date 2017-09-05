from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)


from .models import News


class NewsModelAdmin(ModelAdmin):
    model = News
    menu_label = 'News'
    menu_icon = 'date'
    menu_order = 450
    add_to_settings_menu = False
    list_display = ('title', 'first_published_at',)
    ordering = ('-first_published_at',)


modeladmin_register(NewsModelAdmin)