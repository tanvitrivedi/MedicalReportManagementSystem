from django import forms
from .models import report
from .models import read

class ReportForm(forms.ModelForm):
    class Meta:
        model = report
        fields = ('username', 'report_type', 'image','cur_date')



class ReadForm(forms.ModelForm):
    class Meta:
        model = read
        fields = ('username','read_img')
