# CelebrityGPT

## O que é o projeto?
Esse projeto é apenas para estudar o básico sobre a API da OpenAI usando Python.

A aplicação consiste em uma interface de texto para conversar com o ChatGPT como se ele fosse uma celebridade famosa. O usuário pode escolher com quem deseja conversar no início do diálogo e depois pode questionar o que quiser para a versão GPT da celebridade. Todo o contexto do que foi discutido é mantido durante a conversa.

## Como preparar o ambiente
Faça um git clone do projeto.
```shell
git clone git@github.com:Gabriel-Sasaki/CelebrityGPT.git
```
Crie e ative um ambiente virtual.
```shell
python -m venv env
source ./env/bin/activate
```
Instale as dependências.
```shell
pip install -r requirements.txt
```
Execute a aplicação.
```shell
python ./openai-project/main.py
```
É necessário possuir uma Organization Key e uma API Key da OpenAI. Veja mais abaixo.

## Organization e API Key
Para executar o projeto é necessário possuir uma Organization Key e uma API Key da própria OpenAI. Você pode saber mais acessando a página oficial de autenticação da API em: https://platform.openai.com/docs/api-reference/authentication

## Bibliotecas obrigatórias
aiohttp==3.8.5 <br>
aiosignal==1.3.1 <br>
async-timeout==4.0.2 <br>
attrs==23.1.0 <br>
certifi==2023.7.22 <br>
charset-normalizer==3.2.0 <br>
frozenlist==1.4.0 <br>
idna==3.4 <br>
multidict==6.0.4 <br>
openai==0.27.8 <br>
requests==2.31.0 <br>
tqdm==4.65.0 <br>
urllib3==2.0.4 <br>
yarl==1.9.2
