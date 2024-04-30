from django.db import models
from django_resized import ResizedImageField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class OurHeroes(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = ResizedImageField(size=[700, 544], upload_to='our_heroes/', null=True, blank=True,
                              force_format='WEBP', quality=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Our Heroes"


class AdmissionForm(models.Model):
    addmission_no = models.AutoField(primary_key=True)
    applicant_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    education = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    event = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    reference = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=True)
    applicant_photo = models.ImageField(upload_to='applicant_photo/', blank=True)
    applicant_sign = models.ImageField(upload_to='applicant_sign/', blank=True)
    guardian_sign = models.ImageField(upload_to='guardian_sign/', blank=True)
    applicant_doc_1 = models.FileField(upload_to='applicant_file_1/', blank=True)
    applicant_doc_2 = models.FileField(upload_to='applicant_file_2/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Admission Forms"

    def __str__(self):
        return self.applicant_name