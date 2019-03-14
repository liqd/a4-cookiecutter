from django.contrib import admin

from apps.organisations import models


class OrganisationAdmin(admin.ModelAdmin):
    filter_horizontal = ('initiators',)


admin.site.register(models.Organisation, OrganisationAdmin)
