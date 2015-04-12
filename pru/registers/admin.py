from django.contrib import admin
from .models import Register


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['title', 'public', 'community']
    list_filder = ['id_data', 'contractor', 'privacy', 'text', 'comparable', 'scan',
        'spending', 'created', ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super(RegisterAdmin, self).save_model(request, obj, form, change)
