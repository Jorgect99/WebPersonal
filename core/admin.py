from django.contrib import admin
from .models import About,Skill

# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('level',)

    
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Skill, SkillAdmin)
admin.site.register(About, AboutAdmin)