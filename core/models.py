from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

# Create your models here.

class Projecte(models.Model):
	nom = models.CharField(max_length=200,help_text="Nom del projecte")
	descripcio = models.TextField(blank=True,null=True,default="Un nou projecte...")
	scrum_master = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="scrum_master",
    )
	product_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product_owner",
    )
	grup = models.ForeignKey(Group,
        on_delete=models.CASCADE,
)

class Sprint(models.Model):
	projecte = models.ForeignKey(Projecte,
		on_delete=models.CASCADE)
	data_inici = models.DateField()
	data_final = models.DateField()
	hores = models.IntegerField(default=0,help_text="Hores de desevolupament disponibles de tots els membres de l'equip.")


class Spec(models.Model):
	DIFICULTAT = (
		("D","Desconeguda"),
		("B","Baixa"),
		("M","Mitjana"),
		("A","Alta"),
	)
	descripcio = models.TextField()
	dificultat = models.CharField(
		max_length=1,
		choices=DIFICULTAT,
		default="D")
	hores = models.IntegerField(default=0)

	projecte = models.ForeignKey(Projecte,
		on_delete=models.CASCADE,)
	sprint = models.ForeignKey(Sprint,
		on_delete=models.CASCADE,)
	developer = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,)
