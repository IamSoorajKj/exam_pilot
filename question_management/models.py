from django.db import models
from django.utils.text import slugify

from assesment_management.models import Assesment

# Create your models here.

class Question(models.Model):
      
      title=models.CharField(max_length=200)

      description=models.CharField(max_length=200)

      slug = models.SlugField(
            max_length=220,
            unique=True,
            blank=True
      )

      created_at = models.DateTimeField(auto_now_add=True)

      updated_at = models.DateTimeField(auto_now=True)

      assesment=models.ForeignKey(Assesment,on_delete=models.CASCADE,related_name="questions")

      order = models.PositiveIntegerField(null= True)

      sample_input=models.TextField(null=True)

      sample_output=models.TextField(null=True)

      def save(self, *args, **kwargs):
      
            question_instance =   Question.objects.filter(assesment=self.assesment).last()

            if question_instance:

                  self.order = question_instance.order + 1
            else:
                  self.order = 1

            if not self.slug:
                  self.slug = slugify(self.title)

            super().save(*args, **kwargs)

      def __str__(self):
            return f"{self.assesment.title} - {self.title}"

      class Meta:
            ordering = ["order"]
            unique_together = ["assesment", "order"] 
