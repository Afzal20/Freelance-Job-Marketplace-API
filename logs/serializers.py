from rest_framework import serializers
from .models import (
    Skill, CustomUser, Profile, Portfolio, Achievement, Category, Project, Proposal, Milestone, Review,
    Transaction, Wallet, Message, Notification, AdminModel, Subscription, ReportDispute, SavedProject,
    UserSkillEndorsement, ServicePackage, QuestionAnswer, TestAssessment, Tag, JobPost, JobApplication,
    Contract, Invoice, TimeLog, JobTag, FreelancerTag, FeedbackHistory, PaymentDetail, PaymentTransaction
)

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class AdminModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminModel
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class ReportDisputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportDispute
        fields = '__all__'

class SavedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedProject
        fields = '__all__'

class UserSkillEndorsementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkillEndorsement
        fields = '__all__'

class ServicePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePackage
        fields = '__all__'

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'

class TestAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAssessment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class TimeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLog
        fields = '__all__'

class JobTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTag
        fields = '__all__'

class FreelancerTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerTag
        fields = '__all__'

class FeedbackHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackHistory
        fields = '__all__'

class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = '__all__'

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'
