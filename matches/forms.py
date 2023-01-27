from django import forms

class Singles(forms.Form):
    first_name = forms.CharField(label="Enter your first name",max_length=35)
    last_name = forms.CharField(label="Enter your last name",max_length=35)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NA', 'Prefer not to say')
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    student_number = forms.IntegerField(label="Enter your student number")
    email_address = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=12)
    SKILL_CHOICES = [
        ('A', 'Level A'),
        ('B', 'Level B'),
        ('C', 'Level C')
    ]
    skill_level = forms.ChoiceField(choices=SKILL_CHOICES)
    
class DoublesWithNoPartner(forms.Form):
    first_name = forms.CharField(label="Enter your first name",max_length=35)
    last_name = forms.CharField(label="Enter your last name",max_length=35)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NA', 'Prefer not to say')
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    student_number = forms.IntegerField(label="Enter your student number")
    email_address = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=12)
    SKILL_CHOICES = [
        ('A', 'Level A'),
        ('B', 'Level B'),
        ('C', 'Level C')
    ]
    skill_level = forms.ChoiceField(choices=SKILL_CHOICES)
    
class Doubles(forms.Form):
    first_name = forms.CharField(label="Enter your first name",max_length=35)
    last_name = forms.CharField(label="Enter your last name",max_length=35)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NA', 'Prefer not to say')
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    student_number = forms.IntegerField(label="Enter your student number")
    email_address = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=12)
    SKILL_CHOICES = [
        ('A', 'Level A'),
        ('B', 'Level B'),
        ('C', 'Level C')
    ]
    skill_level = forms.ChoiceField(choices=SKILL_CHOICES)
    partner_first_name = forms.CharField(label="Enter your first name",max_length=35)
    partner_last_name = forms.CharField(label="Enter your last name",max_length=35)
    partner_gender = forms.ChoiceField(choices=GENDER_CHOICES)
    partner_student_number = forms.IntegerField(label="Enter your student number")
    partner_email_address = forms.EmailField(max_length=100)
    partner_phone_number = forms.CharField(max_length=12)
    partner_skill_level = forms.ChoiceField(choices=SKILL_CHOICES)
class MixedDoubles(forms.Form):
        first_name = forms.CharField(label="Enter your first name",max_length=35)
        last_name = forms.CharField(label="Enter your last name",max_length=35)
        GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('NA', 'Prefer not to say')
        ]
        gender = forms.ChoiceField(choices=GENDER_CHOICES)
        student_number = forms.IntegerField(label="Enter your student number")
        email_address = forms.EmailField(max_length=100)
        phone_number = forms.CharField(max_length=12)
        SKILL_CHOICES = [
            ('A', 'Level A'),
            ('B', 'Level B'),
            ('C', 'Level C')
        ]
        skill_level = forms.ChoiceField(choices=SKILL_CHOICES)
        partner_first_name = forms.CharField(label="Enter your first name",max_length=35)
        partner_last_name = forms.CharField(label="Enter your last name",max_length=35)
        partner_gender = forms.ChoiceField(choices=GENDER_CHOICES)
        partner_student_number = forms.IntegerField(label="Enter your student number")
        partner_email_address = forms.EmailField(max_length=100)
        partner_phone_number = forms.CharField(max_length=12)
        partner_skill_level = forms.ChoiceField(choices=SKILL_CHOICES)