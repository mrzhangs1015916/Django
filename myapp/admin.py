from django.contrib import admin
from .models import Banji,Students

# Register your models here.
class StudentsInfo(admin.TabularInline):
    model=Students
    extra=2
@admin.register(Banji)
class BanjiAdmin(admin.ModelAdmin):
    def getGood(self):
        if self.isGood==1:
            return '好'
        else:
            return '不好'
    list_display=['id','name','createtime','num',getGood]
    list_filter=['name']
    list_per_page=10
    search_fields=['name']
    getGood.short_description = '状态'
    # fields=['createtime','num','name','isGood']
    fieldsets=[('first',{'fields':['createtime','num']}),('second',{'fields':['name','isGood']})]
    inlines = [StudentsInfo]

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display=['id','name','age','sex','banNo_id']
    list_filter=['name']
    list_per_page=10
    search_fields=['name']

    # fields=['createtime','num','name','isGood']
    fieldsets=[('first',{'fields':['name','age']}),('second',{'fields':['sex','banNo_id']})]


