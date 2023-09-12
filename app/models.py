from django.db import models

SITUATION = (
    ('Approved', ('Approved')),
    ('Pending', ('Pending')),
    ('Refused', ('Refused')),
)
GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Candidate(models.Model):
    company_note = models.TextField(null=True, blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    job = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER)
    age = models.IntegerField()
    exprience = models.BooleanField(null=True, default='No')
    company = models.CharField(max_length=20, null=True)
    file = models.FileField(upload_to='cv', null=True)
    image = models.ImageField(upload_to='candidate_images', null=True)
    situation = models.CharField(
        max_length=50, choices=SITUATION, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'

    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()
        self.job = self.job.upper()


class Email(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name


class Chat(models.Model):
    candidate_email = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    chat = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
