from django.contrib import admin
from .models import Account, State, Gender, AccountType, Relationship


admin.site.register(Account)
admin.site.register(State)
admin.site.register(Gender)
admin.site.register(AccountType)
admin.site.register(Relationship)