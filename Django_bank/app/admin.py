from django.contrib import admin
from .models import Acc_creation, Acc_type, RelationShip,Gender, State

admin.site.register(Acc_creation)
admin.site.register(Gender)
admin.site.register(State)
admin.site.register(Acc_type)
admin.site.register(RelationShip)

