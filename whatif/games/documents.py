from django import forms
from mongoengine import (Document, EmbeddedDocument, EmbeddedDocumentField, 
                         ListField, StringField, IntField, ReferenceField)

# Token is a simple property of a game 
class Token(Document):
    # Text describing the token
    text  = StringField(required=True)
    
    # JSON util method
    def as_dict(self):
        return { "id": str(self.id), "text": str(self.text) }
    
    # Form for adding a token
    class TokenForm(forms.Form):
        text = forms.CharField(max_length=140, min_length=1)
    
# TokenModifier is a definition for a yes or no response to a question
class TokenModifier(EmbeddedDocument):
    # reference to the token this modifier affects
    token = ReferenceField(Token)
    # yes answer modifier
    yes_modifier = IntField()
    # no answer modifier
    no_modifier = IntField()
    
    # Probably not the best thing to do, but all modifiers can be set to a value between -10 and 10
    def create_options(self, selectedValue):
        result = []
        for value in range(10, -10, -1):
            selected = 'selected="selected"' if value == selectedValue else ''
            result.append('<option value="%d" %s>%d</option>' % (value, selected, value))
        return ''.join(result)
    
    # Util method for outputting <option> values for the yes modifier
    def get_yes_options(self):
        return self.create_options(self.yes_modifier)
    
    # Util method for outputting <option> values for the no modifier
    def get_no_options(self):
        return self.create_options(self.no_modifier)
    
    # JSON util method
    def as_dict(self):
        return { "token": self.token.as_dict(), "yes_modifier": self.yes_modifier, "no_modifier":self.no_modifier }
    
# Question is a definition for a question in a game
class Question(Document):
    # question text
    text = StringField(required=True)
    # token modifiers determine the effect on a token based on a yes or no answer
    token_modifiers = ListField(EmbeddedDocumentField(TokenModifier), default=list)
    
    # JSON util method
    def as_dict(self):
        token_modifiers = []
        for modifier in self.token_modifiers:
            token_modifiers.append(modifier.as_dict())
        return { "id": str(self.id), "text": str(self.text), "token_modifiers": token_modifiers }
    
# Game is a definition for a game/quiz
class Game(Document):
    # game title
    title = StringField(required=True)
    # game tokens
    tokens = ListField(ReferenceField(Token), default=list)
    # game questions
    questions = ListField(ReferenceField(Question), default=list)
    
    # JSON util method
    def as_dict(self):
        tokens = []
        for token in self.tokens:
            tokens.append(token.as_dict())
        questions = []
        for question in self.questions:
            questions.append(question.as_dict())
        return { "id": str(self.id), "title": str(self.title), "tokens": tokens, "questions": questions }
    
    # Game form
    class GameForm(forms.Form):
        title = forms.CharField(max_length=140, min_length=1, widget=forms.TextInput)
    
# Response represents a user's response to a question
class Response(EmbeddedDocument):
    # the question the response refers to
    question = ReferenceField(Question)
    # response value 1 indicates a 'Yes' answer, 0 indicates a 'No' answer
    response = IntField(min_value=0, max_value=1)
    
# GameInstance is created everytime a user starts a game.
class GameInstance(Document):
    # game reference
    game = ReferenceField(Game)
    # user responses
    responses = ListField(EmbeddedDocumentField(Response), default=list)
    
    # util method denotes if user completed the game
    def is_complete(self):
        return len(self.game.questions) == len(self.responses)
