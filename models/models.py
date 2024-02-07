from django.db import models

class Subject_Model(models.Model):
    name = models.CharField(max_length=160)
    objects = models.Manager()
    def __str__(self):
        return self.name

class Course_Models(models.Model):
    name = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject_Model, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=9, decimal_places=2)
    about = models.CharField(max_length=1000)
    teacher = models.ForeignKey('Teacher_Model', on_delete=models.CASCADE)
    category = models.CharField(max_length=120)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Teacher_Model(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    description = models.TextField()
    subject_type = models.ForeignKey(Subject_Model, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='teacher_photo/')
    objects = models.Manager()

    @property
    def full_name(self):
        return f"{self.first_name}  {self.last_name}"
    def __str__(self):
        return self.full_name


class Certificate_Model(models.Model):
    class level_model(models.TextChoices):
        A1 = 'A1'
        A2 = 'A2'
        B1 = 'B1'
        B2 = 'B2'
        C1 = 'C1'
        C2 = 'C2'

    certificate = models.ForeignKey(Teacher_Model, related_name='certificate', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='certificate_photos')
    level = models.CharField(max_length=2, choices=level_model, default=level_model.B2)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)