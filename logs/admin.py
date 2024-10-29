from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import (
    CustomUser, Skill, Profile, Portfolio, Achievement, Category, Project, Proposal, Milestone,
    Review, Transaction, Wallet, Message, Notification, AdminModel, Subscription, ReportDispute,
    SavedProject, UserSkillEndorsement, ServicePackage, QuestionAnswer, TestAssessment, Tag, 
    JobPost, JobApplication, Contract, Invoice, TimeLog,
    JobTag, FreelancerTag, FeedbackHistory, PaymentDetail, PaymentTransaction
)

admin.site.site_header = 'Freelancing Platform Admin Panel'
admin.site.index_title = 'Freelancing Platform Admin Panel'


# Custom user admin registration
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')},
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Registering other models
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    search_fields = ('user__name', 'experience')
    list_filter = ('rating',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'link')
    search_fields = ('title', 'description')
    list_filter = ('user',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'issuer', 'date_awarded')
    search_fields = ('title', 'issuer')
    list_filter = ('date_awarded',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget', 'duration', 'client', 'status')
    search_fields = ('title', 'description')
    list_filter = ('category', 'status', 'client')

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('project', 'freelancer', 'proposed_rate', 'status', 'submitted_at')
    search_fields = ('project__title', 'freelancer__name')
    list_filter = ('status', 'submitted_at')

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'due_date', 'amount', 'status')
    search_fields = ('project__title', 'title')
    list_filter = ('due_date', 'status')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'reviewee', 'project', 'rating', 'created_at')
    search_fields = ('reviewer__name', 'reviewee__name', 'project__title')
    list_filter = ('rating', 'created_at')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('project', 'amount', 'freelancer', 'client', 'transaction_type', 'status', 'transaction_date')
    search_fields = ('project__title', 'freelancer__name', 'client__name')
    list_filter = ('transaction_type', 'status', 'transaction_date')

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'project', 'timestamp', 'read_status')
    search_fields = ('sender__name', 'receiver__name', 'content')
    list_filter = ('read_status', 'timestamp')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'is_read', 'timestamp')
    search_fields = ('user__name', 'message')
    list_filter = ('is_read', 'type', 'timestamp')

@admin.register(AdminModel)
class AdminModelAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'start_date', 'end_date')
    search_fields = ('user__name', 'type')
    list_filter = ('type', 'start_date', 'end_date')

@admin.register(ReportDispute)
class ReportDisputeAdmin(admin.ModelAdmin):
    list_display = ('user', 'reported_user', 'reason', 'status', 'created_at')
    search_fields = ('user__name', 'reported_user__name', 'reason')
    list_filter = ('status', 'created_at')

@admin.register(SavedProject)
class SavedProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'saved_date')
    search_fields = ('user__name', 'project__title')
    list_filter = ('saved_date',)

@admin.register(UserSkillEndorsement)
class UserSkillEndorsementAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill', 'endorsed_by', 'endorsement_date')
    search_fields = ('user__name', 'skill__name', 'endorsed_by__name')
    list_filter = ('endorsement_date',)

@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ('freelancer', 'title', 'price', 'delivery_time', 'status')
    search_fields = ('freelancer__name', 'title', 'description')
    list_filter = ('status', 'price')

@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'question', 'timestamp')
    search_fields = ('user__name', 'project__title', 'question')
    list_filter = ('timestamp',)

@admin.register(TestAssessment)
class TestAssessmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'score', 'date_taken')
    search_fields = ('title', 'user__name')
    list_filter = ('date_taken',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register Job Models
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'title', 'budget', 'duration', 'is_open', 'posted_date')
    search_fields = ('title', 'client__email')
    list_filter = ('is_open', 'posted_date', 'required_skills')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'freelancer', 'proposed_rate', 'status', 'applied_date')
    search_fields = ('job__title', 'freelancer__email')
    list_filter = ('status', 'applied_date')

# Register Contract and Related Models
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'client', 'freelancer', 'start_date', 'end_date', 'status')
    search_fields = ('project__title', 'client__email', 'freelancer__email')
    list_filter = ('status', 'start_date', 'end_date')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'amount_due', 'issued_date', 'due_date', 'is_paid')
    search_fields = ('contract__project__title', 'contract__client__email', 'contract__freelancer__email')
    list_filter = ('is_paid', 'issued_date', 'due_date')

@admin.register(TimeLog)
class TimeLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'start_time', 'end_time')
    search_fields = ('contract__project__title', 'contract__freelancer__email')
    list_filter = ('start_time', 'end_time')

# Register Tag Models
@admin.register(JobTag)
class JobTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'tag')
    search_fields = ('job__title', 'tag')

@admin.register(FreelancerTag)
class FreelancerTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'freelancer', 'tag')
    search_fields = ('freelancer__email', 'tag')

# Register Feedback and Payment Models
@admin.register(FeedbackHistory)
class FeedbackHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'date', 'rating', 'feedback')
    search_fields = ('contract__project__title', 'contract__client__email', 'contract__freelancer__email')
    list_filter = ('date', 'rating')

@admin.register(PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_provider', 'account_id', 'created_at')
    search_fields = ('user__email', 'payment_provider')
    list_filter = ('payment_provider', 'created_at')

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'payment_detail', 'amount', 'transaction_date', 'status')
    search_fields = ('invoice__contract__project__title', 'payment_detail__user__email')
    list_filter = ('status', 'transaction_date')
