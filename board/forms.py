from django import forms
from .models import Post, Board, Search


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'contents', 'board')

        fields = ('title', 'contents', 'board', 'file1', 'file2', 'file3', 'file4', 'file5', 'name', 'file_reset')


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('search',)


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('board_title', 'sub_id', 'is_superuser', 'board_seq')
