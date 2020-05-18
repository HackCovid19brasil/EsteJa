from django.db import models


class Diagnostico(models.Model):
    age = models.IntegerField("Idade", null=True)
    hematocrit = models.DecimalField("Hematócrito", max_digits=50, decimal_places=30, null=True)
    hemoglobin = models.DecimalField("Hemoglobina", max_digits=50, decimal_places=30, null=True)
    platelets = models.DecimalField("Plaquetas", max_digits=50, decimal_places=30, null=True)
    mpv = models.DecimalField("Volume plaquetário médio", max_digits=50, decimal_places=30, null=True)
    rbc = models.DecimalField("Glóbulos vermelhos", max_digits=50, decimal_places=30, null=True)
    lymphocytes = models.DecimalField("Linfócitos", max_digits=50, decimal_places=30, null=True)
    mchc = models.DecimalField("Concentração corpuscular média de hemoglobina", max_digits=50, decimal_places=30, null=True)
    leukocytes = models.DecimalField("Leucócitos", max_digits=50, decimal_places=30, null=True)
    basophils = models.DecimalField("Basófilos", max_digits=50, decimal_places=30, null=True)
    mch = models.DecimalField("Hemoglobina corpuscular média", max_digits=50, decimal_places=30, null=True)
    eosinophils = models.DecimalField("Eosinófilos", max_digits=50, decimal_places=30, null=True)
    mcv = models.DecimalField("Volume corpuscular médio", max_digits=50, decimal_places=30, null=True)
    monocytes = models.DecimalField("Monócitos", max_digits=50, decimal_places=30, null=True)
    rdw = models.DecimalField("Largura de distribuição de glóbulos vermelhos", max_digits=50, decimal_places=30, null=True)
    exam_covid = models.CharField("Diagnóstico", max_length=25, null=True)
