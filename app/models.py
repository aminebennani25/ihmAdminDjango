from django.db import models


class Produit(models.Model):
    """
    Produit : prix, code, etc.
    """

    class Meta:
        verbose_name = "Produit"

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    price_ht = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Prix unitaire HT")
    price_ttc = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Prix unitaire TTC")

    def __unicode__(self):
        return u"{0} [{1}]".format(self.name, self.code)
