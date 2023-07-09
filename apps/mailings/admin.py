from django.contrib import admin
from apps.mailings.models import Mail, Mailings, MailingLog


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'body',)
    list_filter = ('subject',)
    search_fields = ('subject', 'body',)


@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'frequency', 'status', 'clients', 'text',)
    list_filter = ('time', 'frequency', 'status', 'text')
    search_fields = ('clients', 'text',)

    def get_readonly_fields(self, request, obj=None):
        """Make fields read only fields"""
        if request.user.is_superuser:
            return self.readonly_fields
        else:
            return ['time', 'end_time', 'frequency', 'clients', 'text', 'owner']

@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'attempt_date', 'attempt_status', 'response',)
    list_filter = ('attempt_date', 'attempt_status', 'response',)
