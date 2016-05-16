from django import forms

# form to keep track of how many questions and how difficult the user wants the questions to be
class QuestionSettingsForm(forms.Form):
    number_of_questions = forms.CharField(label='number of questions', max_length = 100)
    difficulty = forms.CharField(label='difficulty', max_length = 100)

class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(QuestionForm, self).__init__(*args, **kwargs)
        for i, question in enumerate(extra):
                        self.fields['custom_%s' % i] = forms.CharField(label=question)
#    question = forms.CharField(label='question')
    def extra_answers(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('custom_'):
                yield (self.fields[name].label, value)
