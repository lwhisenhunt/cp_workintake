from django.contrib import admin

# Register your models here.

from .models import Project, Milestone, Capability

# class CapabilityInline(admin.TabularInline):
#     model = Capability
#     extra = 0

class CapabilityInline(admin.TabularInline):
    model = Capability
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    # pass
    inlines=[CapabilityInline]
    list_display=['name','clarity_project','ace_number','ace_approved','project_priority','requested_budget','approved_budget','status']

class MilestoneAdmin(admin.ModelAdmin):
    # pass
    list_display=['name', 'date', 'project_name']

class CapabilityAdmin(admin.ModelAdmin):
    list_display=['capability' , 'product_type','project_name','discovery_complete','target_date','priority']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Capability, CapabilityAdmin)
