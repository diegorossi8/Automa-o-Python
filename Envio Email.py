import pandas as pd
contatos_df = pd.read_excel("CAMINHO ARQUIVO EXCEL COM CONTATOS E NOMES")
display(contatos_df)

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


# Criando objeto
server = smtplib.SMTP('smtp.gmail.com: 587')
# Login com servidor
server.ehlo()
server.starttls()
server.login('seuemail@gmail.com', 'suasenha')
        
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    email = contatos_df.loc[i, "Email"]
    texto = (f"Olá, {pessoa}!\n{mensagem}")

    # Criando mensagem
    message = texto
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = email
    email_msg['Subject'] = "IMPORTANTE !!!"
    email_msg.attach(MIMEText(message, 'plain'))
        # Enviando mensagem
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print(f'Mensagem {i} enviada!')
