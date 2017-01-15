from django import forms

PROGRESSION_STATUS = (
	(0, 'Completed'),
	(1, 'Almost there'),
	(2, 'Under progression'),
	(3, 'Initialized'),
	)

class ActivityForm(forms.Form):
	activity_category = forms.CharField(label='Category', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Programming, new language, Music,...', 'required':'true'}))
	details = forms.CharField(label='Details', widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':"Today I learnt how to use meta class in python programming....", 'required':'true'}))
	status = forms.ChoiceField(choices=PROGRESSION_STATUS, widget=forms.Select(attrs={'class':'form-control'}))
	# creation_date = forms.CharField(label='Date', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the SchedulerName','required':'false'}))