from django.contrib import admin
from .models import *

class participantsAdmin(admin.ModelAdmin):
	list_display = ('fullname', 'username', 'rollno', 'emailid', 'team', 'login_flag')

class omrsheetAdmin(admin.ModelAdmin):
    list_display = ('username', 'final_submit', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8')

class scorecardAdmin(admin.ModelAdmin):
    list_display = ('username', 'score')

admin.site.register(participants, participantsAdmin)
admin.site.register(omrsheet, omrsheetAdmin)
admin.site.register(scorecard, scorecardAdmin)