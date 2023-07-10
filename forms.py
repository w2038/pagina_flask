from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()],)
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired()])
    criar_conta = SubmitField('Criar Conta')
    

class FormLogin(FlaskForm):
    email = StopIteration('Email')
    senha = PasswordField('Senha')
    login = SubmitField('Fazer login')