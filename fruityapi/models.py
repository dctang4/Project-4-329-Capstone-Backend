from django.db import models

# Create your models here.
class Fruity(models.Model):
  # ICE = (
  #   ('0%', 'No'),
  #   ('25%', 'Little'),
  #   ('50%', 'Half'),
  #   ('75%', 'Less'),
  #   ('100%', 'Regular'),
  # )
  # SUGAR = (
  #   ('0%', 'No'),
  #   ('25%', 'Little'),
  #   ('50%', 'Half'),
  #   ('75%', 'Less'),
  #   ('100%', 'Regular'),
  # )
  # TOPPINGS = (
  #   ('N','None'),
  #   ('B','Boba'),
  #   ('MP','Mango Popper'),
  #   ('LP','Lychee Popper'),
  #   ('PP','Peach Popper'),
  #   ('PFP','Passionfruit Popper'),
  #   ('RJ','Rainbow Jelly'),
  #   ('MJ','Mango Jelly'),
  #   ('LJ','Lychee Jelly'),
  #   ('SJ','Strawberry Jelly'),
  #   ('GJ','GreenApple Jelly'),
  #   ('CJ','Coffee Jelly'),
  # )
  # SIZE = (
  #   ('M', 'Medium'),
  #   ('L', 'Large')
  # )
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=25)
  info = models.CharField(max_length=100)
  # ice = models.CharField(max_length=10, choices=ICE, default='100%')
  # sugar = models.CharField(max_length=15, choices=SUGAR, default='100%')
  # topping = models.CharField(max_length=20, choices=TOPPINGS, default='N')
  # size = models.CharField(max_length=10, choices=SIZE, default='M')
  price = models.CharField(max_length=10)

  def __str__(self):
        return self.name
