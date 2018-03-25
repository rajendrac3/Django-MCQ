from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from crispy_forms.layout import Submit, Layout, Div, Fieldset

from Home.models import Question, Answer, Course, Quiz

# class TakeQuizForm(forms.ModelForm):
#     answer = forms.ModelChoiceField(
#         queryset=Answer.objects.none(),
#         widget=forms.RadioSelect(),
#         required=True,
#         empty_label=None)

#     # class Meta:
#     #     model = Answer
#     #     fields = ('answer', )

#     # def __init__(self, *args, **kwargs):
#     #     question = kwargs.pop('question')
#     #     super().__init__(*args, **kwargs)
#     #     # self.fields['answer'].queryset = question.answers.order_by('text')

#     class Meta:
#         model = Answer
#         fields = ('answer', )

#     def __init__(self, *args, **kwargs):
#         question = kwargs.pop('question')
#         # print("question.first()",question.first())
#         # s = list(question.filter())
#         # print("question.filter()",s)
#         c = question.filter()
#         super().__init__(*args, **kwargs)
#         v = list(question.filter())
#         categories=[]
#         categories.extend(question.all())
#         # print("c = ", c)
#         # print("c = ", question)
#         # for aninmal in v:
#         for i, c in enumerate(question):
            
            
#             # print("Question - ", aninmal)
#         # print("All questions", question.filter())
#         # print("this is answers", c.answers)
#             # print("Answers - ", aninmal.answers.order_by('text'))
#             # print("i, c", i, c)
#             # print("answers", c.answers.all())

#             for ans in [c]:
#                 # print("final", ans.answers.order_by('text'))
#                 list_of_querysets = ans.answers.order_by('text')
#                 # print("list_of_querysets", [list_of_querysets])
#                 # print("This is queryset ", self.fields['answer'].queryset)
#                 # print("This is queryset after assignment", self.fields['answer'].queryset)
#                 # self.fields['answer'].queryset = ans.answers.order_by('text')
#                 # self.fields['answer'].queryset = ans.answers.all()
#                 # self.fields['answer'].queryset = ans.answers.all()

#                 for qs in [list_of_querysets]:
#                     print("qs", qs)
#                     self.fields['answer'].queryset = qs
                
#         # self.helper = FormHelper(self)
#         # self.helper.layout.append(
#         #     FormActions(
#         #         HTML("""<a role="button" class="btn btn-default"
#         #                 href="{% url "some_cancel_url" %}">Cancel</a>"""),
#         #         Submit('save', 'Submit'),
#         # ))

    
class TakeQuizForm(forms.ModelForm):

    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = Answer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        spk = kwargs.pop('spk')
        super().__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelChoiceField(
            queryset=Answer.objects.filter(id=spk),
            widget=forms.RadioSelect(),
            empty_label=None,
            required=True
        )

    