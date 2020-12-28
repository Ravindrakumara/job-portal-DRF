from django.contrib import admin

# Import model
from.models import Jobs,Work_record,Candidates,questionnaire
# Register your models here.
admin.site.site_header = "Job Portal"
admin.site.site_title = "Job Portal"    # this represent to title of page tittle
admin.site.index_title = "Welcome to admin"

class Job(admin.ModelAdmin):
    list_display = ['job','qualifications','experience','reporting_to','added_date'] #   Display to table
    list_editable = ['qualifications','experience','reporting_to'] #    On the raw able for edit
    search_fields = ['job', 'reporting_to'] #   search for the Job & reporting_to
    list_per_page = 1 #     set to num fo data rows allow. pagenation

class Candidate_name(admin.ModelAdmin):
    list_display = ['name','added_date'] #,'work_record','apply_for'

class Work_records(admin.ModelAdmin):
    list_display = ['positon','workplace','start','end','added_date']

class Questionnaire(admin.ModelAdmin):
    list_display = ['question','answer','mark','added_date']
    list_editable = ['mark']

admin.site.register(Jobs,Job)   # here have to put model name & class name
admin.site.register(Candidates,Candidate_name)
admin.site.register(Work_record,Work_records)
admin.site.register(questionnaire,Questionnaire)