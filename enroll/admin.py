from django.contrib import admin
from .models import Students

# Register your models here.
class studentAdmin(admin.ModelAdmin):
      list_display = ('id','stid','stname','stemail','stpass')

admin.site.register(Students, studentAdmin)
