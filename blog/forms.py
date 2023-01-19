from django import forms

class FormKomentar(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Namamu"
        })
    )

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class" : "form-control",
            "placeholder" : "Tinggalkan komen!!"
        }
    ))