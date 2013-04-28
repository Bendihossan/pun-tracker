from django.contrib import admin
from puns .models import Pun

class PunAdmin(admin.ModelAdmin):
    fieldsets = [
      ('Pun',       {'fields': ['name', 'description', 'vote']}),
      ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]

admin.site.register(Pun, PunAdmin)
