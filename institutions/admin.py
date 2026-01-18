# institutions/admin.py
from django.contrib import admin
from .models import Institution, Course
from django.utils.html import format_html
from decimal import Decimal, InvalidOperation

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'location', 'courses_count', 'phone', 'email')
    search_fields = ('name', 'code', 'location')
    list_filter = ('location',)
    ordering = ('name',)

    def courses_count(self, obj):
        return obj.courses.count()
    courses_count.short_description = "Courses"

    def get_readonly_fields(self, request, obj=None):
        return ('code',) if obj else ()


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "institution", "years_of_study", "formatted_fee")
    list_filter = ("institution",)
    search_fields = ("code", "name", "institution__name")
    ordering = ("institution", "code")

    def formatted_fee(self, obj):
        raw = obj.total_tuition_fee

        try:
        # Convert anything (Decimal/float/str/SafeString) -> Decimal
            fee = Decimal(str(raw).replace(",", "").strip())
        except (InvalidOperation, TypeError, ValueError, AttributeError):
            fee = Decimal("0")

        fee_text = f"{fee:,.2f}"
        return format_html("PGK {}", fee_text)

    formatted_fee.short_description = "Tuition Fee"
    formatted_fee.admin_order_field = "total_tuition_fee"
