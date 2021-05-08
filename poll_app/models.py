from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50, null = True)
    option_three = models.CharField(max_length=50, null = True)
    option_one_count = models.IntegerField(default = 0)
    option_two_count = models.IntegerField(default = 0)
    option_three_count = models.IntegerField(default = 0)
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
    def increement(self,option):
        if option == self.option_one:
            self.option_one_count += 1
            self.save()
        elif option == self.option_two:
            self.option_two_count += 1
            self.save()
        elif option == self.option_three:
            self.option_three_count += 1
            self.save()