from django import forms
from mongoengine import (Document, EmbeddedDocument, EmbeddedDocumentField, 
                         ListField, StringField, IntField, ReferenceField)

class Token(Document):
    text  = StringField(required=True)
    
    def as_dict(self):
        return { "id": str(self.id), "text": str(self.text) }
    
    class TokenForm(forms.Form):
        text = forms.CharField(max_length=140, min_length=1)
    
class TokenModifier(EmbeddedDocument):
    token = ReferenceField(Token)
    yes_modifier = IntField()
    no_modifier = IntField()
    
    def create_options(self, selectedValue):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        result = []
        for value in values:
            selected = 'selected="selected"' if value == selectedValue else ''
            result.append('<option value="%d" %s>%d</option>' % (value, selected, value))
        return ''.join(result)
    
    def get_yes_options(self):
        return self.create_options(self.yes_modifier)
    
    def get_no_options(self):
        return self.create_options(self.no_modifier)
    
    def as_dict(self):
        return { "token": self.token.as_dict(), "yes_modifier": self.yes_modifier, "no_modifier":self.no_modifier }
    
class Question(Document):
    text = StringField(required=True)
    token_modifiers = ListField(EmbeddedDocumentField(TokenModifier), default=list)
    
    def as_dict(self):
        token_modifiers = []
        for modifier in self.token_modifiers:
            token_modifiers.append(modifier.as_dict())
        return { "id": str(self.id), "text": str(self.text), "token_modifiers": token_modifiers }
    
class Game(Document):
    title = StringField(required=True)
    tokens = ListField(ReferenceField(Token), default=list)
    questions = ListField(ReferenceField(Question), default=list)
    
    def as_dict(self):
        tokens = []
        for token in self.tokens:
            tokens.append(token.as_dict())
        questions = []
        for question in self.questions:
            questions.append(question.as_dict())
        return { "id": str(self.id), "title": str(self.title), "tokens": tokens, "questions": questions }
    
    class GameForm(forms.Form):
        title = forms.CharField(max_length=140, min_length=1, widget=forms.TextInput)
    
class Response(EmbeddedDocument):
    question = ReferenceField(Question)
    response = IntField(min_value=0, max_value=1) # 1 indicates a 'Yes' answer, -1 indicates a 'No' answer
    
class GameInstance(Document):
    game = ReferenceField(Game)
    responses = ListField(EmbeddedDocumentField(Response), default=list)
    
    def is_complete(self):
        return len(self.game.questions) == len(self.responses)