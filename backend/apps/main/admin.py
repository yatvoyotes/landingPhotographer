from django.contrib import admin

from backend.apps.main.models import Zapis, Back


class ZapisModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "date", "type_photoset"]

    class Meta:
        model = Zapis


class BackModelAdmin(admin.ModelAdmin):
    list_display = ["name_back", "email_back", "phone_back"]

    class Meta:
        model = Back


admin.site.register(Zapis, ZapisModelAdmin)
admin.site.register(Back, BackModelAdmin)
