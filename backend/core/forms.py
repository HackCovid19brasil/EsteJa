from django import forms
from .models import Diagnostico


class DiagnosticoForm(forms.ModelForm):
  required_css_class = 'required'

  class Meta:
    model = Diagnostico
    fields = (
      "age",
      "hematocrit",
      "hemoglobin",
      "platelets",
      "mpv",
      "rbc",
      "lymphocytes",
      "mchc",
      "leukocytes",
      "basophils",
      "mch",
      "eosinophils",
      "mcv",
      "monocytes",
      "rdw"
    )
