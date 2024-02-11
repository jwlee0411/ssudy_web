import django.contrib.auth.forms as auth_forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import ClubInfo

from django import forms

from common.models import EmailVerify


class ClubInfoEditForm(forms.ModelForm):
    class Meta:
        model = ClubInfo
        fields = ('club_name', 'club_category', 'image', 'description', 'sns1_name', 'sns2_name', 'sns1_link', 'sns2_link',
                  'intro_01', 'intro_02', 'leader', 'room', 'year', 'image_01', 'image_02', 'image_03', 'image_04')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'email2', 'first_name', 'phone_number', 'dept', 'num')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['dept'].required = False
        self.fields['num'].required = False
        self.fields['email2'].required = False


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
        'email', 'email2', 'phone_number', 'first_name')


class CustomUserCreationForm2(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
        'email', 'first_name')

class EmailVerifyForm(forms.ModelForm):
    class Meta:
        model = EmailVerify
        # fields = ('title', 'contents', 'board')

        fields = ('verify',)




class CustomPasswordResetForm(PasswordResetForm):
    model = get_user_model()
    username = auth_forms.UsernameField(label="사용자ID")  # CharField 대신 사용

    # validation 절차:
    # 1. username에 대응하는 User 인스턴스의 존재성 확인
    # 2. username에 대응하는 email과 입력받은 email이 동일한지 확인

    def clean_username(self):
        data = self.cleaned_data['username']
        if not User.objects.filter(username=data).exists():
            raise ValidationError("해당 사용자ID가 존재하지 않습니다.")

        return data

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if username and email:
            if User.objects.get(username=username).email != email:
                raise ValidationError("사용자의 이메일 주소가 일치하지 않습니다")

    def get_users(self, email=''):
        active_users = User.objects.filter(**{
            'username__iexact': self.cleaned_data["username"],
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password()
        )
