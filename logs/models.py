import json
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# CustomUser-related Models
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    username = None

    USERNAME_FIELD = 'email'  # login with email
    REQUIRED_FIELDS = []  # No required fields for superuser creation

    objects = CustomUserManager()  # Use the custom manager

    
class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    experience = models.TextField()
    education = models.TextField()
    certifications = models.TextField(blank=True)
    social_links = models.URLField(blank=True)
    portfolio = models.OneToOneField('Portfolio', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.FloatField(default=0.0)

class Portfolio(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='portfolios/', blank=True, null=True)
    link = models.URLField(blank=True)

class Achievement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    date_awarded = models.DateField()
    description = models.TextField(blank=True)

# Project and Related Models
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    price  = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(CustomUser, related_name='client_projects', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    requirements = models.TextField(blank=True)
    status = models.CharField(max_length=100)
    skills_required = models.ManyToManyField(Skill, related_name='projects', blank=True)

class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(CustomUser, related_name='proposals', on_delete=models.CASCADE)
    cover_letter = models.TextField()
    proposed_rate = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)

class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, related_name='given_reviews', on_delete=models.CASCADE)
    reviewee = models.ForeignKey(CustomUser, related_name='received_reviews', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Transaction Models
class Transaction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    freelancer = models.ForeignKey(CustomUser, related_name='freelancer_transactions', on_delete=models.CASCADE)
    client = models.ForeignKey(CustomUser, related_name='client_transactions', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()

class Wallet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_history = models.ManyToManyField(Transaction, blank=True)

# Communication Models
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    type = models.CharField(max_length=100)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class AdminModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permissions = models.TextField() 
    activity_log = models.TextField(blank=True)

    def set_permissions(self, permissions_dict):
        self.permissions = json.dumps(permissions_dict)

    def get_permissions(self):
        return json.loads(self.permissions) if self.permissions else {}


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class ReportDispute(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(CustomUser, related_name='disputes_reported_against', on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# Miscellaneous Models
class SavedProject(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    saved_date = models.DateTimeField(auto_now_add=True)

class UserSkillEndorsement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    endorsed_by = models.ForeignKey(CustomUser, related_name='endorsements_given', on_delete=models.CASCADE)
    endorsement_date = models.DateTimeField(auto_now_add=True)

class ServicePackage(models.Model):
    freelancer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.DurationField()
    revisions = models.IntegerField()
    status = models.CharField(max_length=100)

class QuestionAnswer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class TestAssessment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    score = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_taken = models.DateField()

class Tag(models.Model):
    name = models.CharField(max_length=100)


# New Models for Job Postings and Applications
class JobPost(models.Model):
    client = models.ForeignKey(CustomUser, related_name='job_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    required_skills = models.ManyToManyField('Skill', related_name='job_posts')
    posted_date = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

class JobApplication(models.Model):
    job = models.ForeignKey(JobPost, related_name='applications', on_delete=models.CASCADE)
    freelancer = models.ForeignKey(CustomUser, related_name='job_applications', on_delete=models.CASCADE)
    cover_letter = models.TextField()
    proposed_rate = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    applied_date = models.DateTimeField(auto_now_add=True)

# Models for Contracts, Invoicing, and Time Tracking
class Contract(models.Model):
    project = models.ForeignKey('Project', related_name='contracts', on_delete=models.CASCADE)
    client = models.ForeignKey(CustomUser, related_name='contracts_as_client', on_delete=models.CASCADE)
    freelancer = models.ForeignKey(CustomUser, related_name='contracts_as_freelancer', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    terms = models.TextField()
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('paused', 'Paused'), ('completed', 'Completed')])

class Invoice(models.Model):
    contract = models.ForeignKey(Contract, related_name='invoices', on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)

class TimeLog(models.Model):
    contract = models.ForeignKey(Contract, related_name='time_logs', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity_log = models.TextField()

# Models for Tagging and Feedback
class JobTag(models.Model):
    job = models.ForeignKey(JobPost, related_name='tags', on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

class FreelancerTag(models.Model):
    freelancer = models.ForeignKey(CustomUser, related_name='tags', on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

class FeedbackHistory(models.Model):
    contract = models.ForeignKey(Contract, related_name='feedback_history', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    feedback = models.TextField()

# Payment Models for External Integration
class PaymentDetail(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_provider = models.CharField(max_length=100, choices=[('stripe', 'Stripe'), ('paypal', 'PayPal')])
    account_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class PaymentTransaction(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_detail = models.ForeignKey(PaymentDetail, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('successful', 'Successful'), ('failed', 'Failed')])