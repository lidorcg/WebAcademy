from django.contrib import admin
from .models import Idea, Group, Concept


# Register your models here.

class GroupInline(admin.TabularInline):
    model = Group


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    inlines = [GroupInline, ]


class ConceptsInline(admin.StackedInline):
    model = Concept
    extra = 0


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [ConceptsInline, ]


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    pass
