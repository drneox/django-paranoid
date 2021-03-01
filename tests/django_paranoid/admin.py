
""" Sthis adds 'created_at', 'updated_at' and 'delete_at'  fields like a rail apps in django,
    also added soft delete method.
Copyright (c) 2018, Carlos Ganoza Plasencia
url: http://carlosganoza.com
"""

from django.contrib import admin


class ParanoidAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','deleted_at','updated_at')

