from django.contrib import admin

from ong.models import Ong, Despesas

admin.site.register(Ong)
admin.site.register(Despesas)
# Register your models here.

from ong.models import Ong

admin.site.register(Ong)
