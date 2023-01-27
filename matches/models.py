from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class MixedDoubles(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("NA", "Prefer not to say")]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default="NA")
    student_number = models.IntegerField(
        null=False, blank=False, validators=[MaxValueValidator(99999999)]
    )
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(null=False, blank=False, max_length=12)
    SKILL_CHOICES = [("A", "Level A"), ("B", "Level B"), ("C", "Level C")]
    skill_level = models.CharField(max_length=1, choices=SKILL_CHOICES, default="C")

    partner_first_name = models.CharField(null=False, blank=False, max_length=100)
    partner_last_name = models.CharField(null=False, blank=False, max_length=100)
    partner_gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default="NA"
    )
    partner_student_number = models.PositiveSmallIntegerField(
        null=False, blank=False, validators=[MaxValueValidator(99999999)]
    )
    partner_email_address = models.EmailField(max_length=100)
    partner_phone_number = models.CharField(null=False, blank=False, max_length=12)
    partner_skill_level = models.CharField(
        max_length=1, choices=SKILL_CHOICES, default="C"
    )
    paid_status = models.BooleanField(default=False, null=False, blank=False)


class Doubles(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("NA", "Prefer not to say")]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default="NA")
    student_number = models.IntegerField(
        null=False, blank=False, validators=[MaxValueValidator(99999999)]
    )
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(null=False, blank=False, max_length=12)
    SKILL_CHOICES = [("A", "Level A"), ("B", "Level B"), ("C", "Level C")]
    skill_level = models.CharField(max_length=1, choices=SKILL_CHOICES, default="C")

    partner_first_name = models.CharField(null=False, blank=False, max_length=100)
    partner_last_name = models.CharField(null=False, blank=False, max_length=100)
    partner_gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default="NA"
    )
    partner_student_number = models.IntegerField(
        null=False, blank=False, validators=[MaxValueValidator(99999999)]
    )
    partner_email_address = models.EmailField(max_length=100)
    partner_phone_number = models.CharField(null=False, blank=False, max_length=12)
    partner_skill_level = models.CharField(
        max_length=1, choices=SKILL_CHOICES, default="C"
    )
    paid_status = models.BooleanField(default=False, null=False, blank=False)


class DoublesWithNoPartner(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("NA", "Prefer not to say")]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default="NA")
    student_number = models.IntegerField(
        null=False, blank=False, validators=[MaxValueValidator(99999999)]
    )
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(null=False, blank=False, max_length=12)
    SKILL_CHOICES = [("A", "Level A"), ("B", "Level B"), ("C", "Level C")]
    skill_level = models.CharField(max_length=1, choices=SKILL_CHOICES, default="C")
    paid_status = models.BooleanField(default=False, null=False, blank=False)


class Singles(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("NA", "Prefer not to say")]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="NA")
    student_number = models.IntegerField(
        null=False, blank=False, validators=[MaxValueValidator(99999999)]
    )
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(null=False, blank=False, max_length=12)
    SKILL_CHOICES = [("A", "Level A"), ("B", "Level B"), ("C", "Level C")]
    skill_level = models.CharField(max_length=1, choices=SKILL_CHOICES, default="C")
    paid_status = models.BooleanField(default=False, null=False, blank=False)
