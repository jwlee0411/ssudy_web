from django import forms
from .models import Reserve_new


class ReserveNewForm(forms.ModelForm):
    user_id = forms.CharField(max_length=32, required=False)
    user_name = forms.CharField(max_length=100, required=False)
    user_tel = forms.CharField(max_length=100, required=False)
    user_email = forms.CharField(max_length=100, required=False)
    reserve_date = forms.DateTimeField(required=False)
    reserve_time = forms.CharField(max_length=32, required=False)
    room = forms.CharField(max_length=100, required=False)
    reserve_desc_1 = forms.CharField(max_length=500, required=False)
    reserve_desc_2 = forms.CharField(max_length=500, required=False)
    reserve_desc_3 = forms.CharField(max_length=500, required=False)
    reserve_num = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Reserve_new
        fields = ('user_id', 'user_name', 'user_tel', 'user_email', 'reserve_date', 'reserve_time', 'room', 'confirm', 'reserve_num',
                  'reserve_desc_1', 'reserve_desc_2', 'reserve_desc_3')
