from django import forms
from .models import Item


class CreateUpdateItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
