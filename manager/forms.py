from django import forms
from .models import Popup, Front, MainBoard, Email, Clubs, Maintenance, Terms, AddClass, EmailAll, ClassSetting

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ('text',)

class ClassSettingForm(forms.ModelForm):
    class Meta:
        model = ClassSetting
        fields = ('club_start', 'club_end', 'stu_start', 'stu_end')

class ClassForm(forms.ModelForm):
    class Meta:
        model=AddClass
        fields=('name', 'confirm')

class TermsForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ('file1', 'file2', 'file3')

class PopupForm(forms.ModelForm):
    class Meta:
        model = Popup
        fields = ('file1', 'content1')


class FrontForm(forms.ModelForm):
    class Meta:
        model = Front
        fields = ('file1', 'file2', 'file3', 'title1', 'title2', 'title3', 'content1', 'content2', 'content3')


class ClubsForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = ('file1_1', 'file1_2', 'file1_3', 'file2_1', 'file2_2', 'file2_3', 'file3_1', 'file3_2', 'file3_3', 'file4_1', 'file5_1', 'calendar_check')


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields=('email1',)

class EmailAllForm(forms.ModelForm):
    class Meta:
        model = EmailAll
        fields=('email1', 'email2')

#
# class BoardForm(forms.ModelForm):
#     class Meta:
#         model = Board
#         fields = ('group', 'title0', 'permission')


class MainBoardForm(forms.ModelForm):
    class Meta:
        model = MainBoard
        fields = ('board1', 'board2')