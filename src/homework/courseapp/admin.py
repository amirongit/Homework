from django.contrib import admin

from .models import (Course, Homework, HomeworkStudentRel, Lecture,
                     Presentation, PresentationStudentRel)


@admin.register(Course)
class CourseAdminRep(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ('name', )
    readonly_fields = ('name', 'teacher', 'description')
    fieldsets = (
        (None, {
            'fields': readonly_fields
        }),
    )

    def has_add_permission(self, _):
        return False


class StudentItemInline(admin.TabularInline):
    model = PresentationStudentRel
    extra = 0


@admin.register(Presentation)
class PresentationAdminRep(admin.ModelAdmin):
    list_display = ('course', 'start_date', 'end_date')
    search_fields = ('course__name', )
    readonly_fields = ('course', 'start_date', 'end_date')
    inlines = (StudentItemInline, )

    def has_add_permission(self, _):
        return False


class AnswerItemInline(admin.TabularInline):
    model = HomeworkStudentRel
    extra = 0


@admin.register(Homework)
class HomeworkAdminRep(admin.ModelAdmin):
    list_display = ('title', 'presentation')
    search_fields = ('title', 'presentation__course__name')
    readonly_fields = ('presentation', 'title', 'description')
    inlines = (AnswerItemInline, )

    def has_add_permission(self, _):
        return False


@admin.register(Lecture)
class LectureAdminRep(admin.ModelAdmin):
    list_display = ('title', 'presentation')
    search_fields = ('title', 'presentation__course__name')
    readonly_fields = ('presentation', 'title', 'text')

    def has_add_permission(self, _):
        return False
