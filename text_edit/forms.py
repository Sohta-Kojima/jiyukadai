from django import forms

widget_textarea = forms.Textarea(
    attrs = {
        "class": "form-control",
    }
)
widget_textinput = forms.TextInput(
    attrs = {
        "class": "form-control",
    }
)

class TextForm(forms.Form):
    text = forms.CharField(label="テキストを入力", widget=widget_textarea)
    search = forms.CharField(label="検索", widget=widget_textinput)
    replace = forms.CharField(label="置換", widget=widget_textinput)