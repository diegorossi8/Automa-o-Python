import pandas as pd
contatos_df = pd.read_excel("CAMINHO ARQUIVO EXCEL COM CONTATOS E NOMES")
display(contatos_df)

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


# Criando objeto

        
for i, mensagem in enumerate(contatos_df['Mensagem']):
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        # Login com servidor
        server.ehlo()
        server.starttls()
        server.login('EMAIL@gmail.com', 'SENHA')
        pessoa = contatos_df.loc[i, "Pessoa"]
        email = contatos_df.loc[i, "Email"]
        texto = (f"Olá, {pessoa}!\nTudo bem? \n A CONQUER liberou gratuitamente o curso de Produtividade e Gestão do Tempo.\nAprenda estratégias e ferramentas de produtividade para gerir melhor o seu tempo, priorizar seus sonhos e alcançar os objetivos desejados. \nCurso Gratuito Produtividade e Gestão do Tempo | Escola Conquer\nhttps://upvir.al/ref/61f425eff1d88M")

        # Criando mensagem
        message = texto
        email_msg = MIMEMultipart()
        email_msg['From'] = "EMAIL@gmail.com"
        email_msg['To'] = email
        email_msg['Subject'] = "IMPORTANTE !!! CURSO GRATUITO"
        email_msg.attach(MIMEText(message, 'plain'))
        # Enviando mensagem
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print(f'Mensagem {i} enviada!')
        server.close()
    except:
        print(f'Mensagem {i} NÃO!')
        pass
