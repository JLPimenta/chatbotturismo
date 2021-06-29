import requests
import json
import os


class JaoJalapao:

    def __init__(self):
        BOT_TOKEN = 'INSIRA O SEU TOKEN AQUI' # NÃO SUBIR PARA O GITHUB 
        self.url_base = f'https://api.telegram.org/bot{BOT_TOKEN}/'

    def nova_mensagem(self, update_id):
                link_requisicao = f'{self.url_base}getUpdates?timeout=100' # Bot aguardará por 100 segundos uma nova requisição
                if update_id:
                    link_requisicao = f'{link_requisicao}&offset={update_id + 1}' # Com isso, o bot responderá somente a última mensagem enviada.
                resultado = requests.get(link_requisicao)
                return json.loads(resultado.content)

    def iniciar(self):
        update_id = None
        while True:
          atualizacao = self.nova_mensagem(update_id)
          dados = atualizacao['result']
          if dados:
            for dado in dados:
              update_id = dado['update_id']
              mensagem = str(dado["message"]["text"])
              chat_id = dado["message"]["from"]["id"]
              primeiro_contato = int(dado['message']['message_id']) == 1
              resposta = self.criar_mensagem_resposta(mensagem, primeiro_contato)
              self.resposta_chat(resposta, chat_id)

    def criar_mensagem_resposta(self, mensagem, primeiro_contato):

        if primeiro_contato == True or mensagem in ('menu', 'Menu', '/start'):
          return f'Olá! Bem vindo(a) ao chat do TurismoTocantins! 😁 Por favor, tecle:\n{os.linesep}1 -☀️🏝 Para conhecer mais sobre as belezas do Jalapão;\n{os.linesep}2 - ✈️ Conhecer os pacotes de viagem disponíveis;\n{os.linesep}3 - 👩‍💼 Falar diretamente com um atendente humano. \n\n{os.linesep}Digite "sobre" para mais informações sobre a empresa e o BOT :)' # Resposta desenvolvida para o início da conversa

        if mensagem == '1':
          return f'☀️🏖 Entre dunas douradas, paisagens grandiosas, fervedouros e cachoeiras o Jalapão cada dia mais conquista os viajantes amantes do ecoturismo. Em meio ao cerrado do Tocantins, o Jalapão está sendo descoberto pelos turistas que buscam alguns dias de descanso longe dos grandes centros urbanos.\n O destino é ideal para relaxar e curtir intensamente o contato com a natureza. A região é uma das mais bem preservadas do país e o acesso, ainda limitado, faz do Jalapão uma região bem pouco explorada. É hora de sair do roteiro comum e seguir para um refrescante banho nas águas do Jalapão, afinal, sol é o que não falta por lá.{os.linesep}Digite "menu" para voltar.'

        
        if mensagem == '2':
          return f'✈️ Há alguns pacotes disponíveis no momento. Digite:\n{os.linesep} A - para conhecer nosso Pacote 4 dias e 3 noites Nº01;\n{os.linesep}B - para o Pacote 4 dias e 3 noites Nº02;\n{os.linesep}C - para o Pacote 6 dias e 5 noites.'
          

        elif mensagem == 'A' or mensagem == 'a':
          return f'Roteiro de 4 dias e 3 noites Nº01:'"\n" "\n" '1° dia' "\n""\n" '(Saída as 7:30h de Palmas)' "\n" '✔ Lagoa do Japonês' "\n" '(Almoço às 12:30)' "\n" '✔ Por do sol Pedra Furada' "\n" '(Pernoite em Ponte Alta)' "\n""\n" '2° dia' "\n""\n" '(Saída as 7:30h de Ponte Alta do Tocantins)' "\n" '✔ Cânion do Sussuapara' "\n" '✔ Cachoeira da Velha' "\n" '✔ Prainha do Rio Novo' "\n" '(Lanche as 12:00, no percurso não tem restaurantes)' "\n" '✔ Rio Novo (comunidade Quilombola)' "\n" '✔ Dunas' "\n" '(Chegada à Mateiros as 19:30, jantar e pernoite)' "\n""\n" '3° dia' "\n""\n"'(Saída às 8:00h de Mateiros)' "\n" '✔ Fervedouro Buriti' "\n" '✔ Fervedouro Bananeiras(Ceiça)' "\n" '✔ Mumbuca (Comunidade Quilombola)' "\n"'✔ Fervedouro Rio Sono' "\n" '(Almoço às 12:30)'"\n"'✔ Cachoeira do Formiga'"\n"'(Segue para São Felix, chegada às 18h, jantar às 19:30, pernoite)'"\n""\n"'4° dia'"\n""\n"'(Saída às 08:00h para visitação dos Atrativos)'"\n"'✔ Fervedouro Alecrim'"\n"'✔ Praia do Alecrim'"\n"'✔ Fervedouro Bela vista (maior do Jalapão)'"\n"'(Almoço as 12:00h)'"\n"'✔ Serra da Catedral'"\n"'✔ Morro vermelho'"\n"'(Saída para Palmas as 13h e chegada às 18:00h).'"\n""\n"'Digite "Sim" para confirmar a solicitação ou "menu" para voltar'


        elif mensagem == 'B' or mensagem == 'b':
          return f'Roteiro de 4 dias e 3 noites Nº02:'"\n""\n"'1° dia'"\n""\n"'✔ Cachoeira da Roncadeira (trilha 1500m)'"\n"'✔ Cachoeira Escorrega Macaco'"\n"'(Almoço as 12:30, em Ponte Alta do Tocantins)'"\n"'✔ Canyon do Sussuapara'"\n"'✔ Por do sol Pedra Furada'"\n"'(Pernoite em Ponte Alta)'"\n""\n"'2° dia'"\n""\n"'(Saída as 7:30h de Ponte Alta do Tocantins)'"\n"'✔ Cachoeira da Velha'"\n"'✔ Prainha do Rio Novo'"\n"'(Lanche as 12:00, no percurso não tem restaurantes)'"\n"'✔ Rio Novo (comunidade Quilombola)'"\n"'✔ Dunas'"\n"'(Chegada à Mateiros as 19:30, jantar e pernoite)'"\n""\n"'3° dia'"\n""\n"'(Saída às 8:00h de Mateiros)'"\n"'✔ Fervedouro Buriti'"\n"'✔ Fervedouro Bananeiras(Ceiça)'"\n"'✔ Mumbuca (Comunidade Quilombola)'"\n"'✔ Fervedouro Rio Sono'"\n"'(Almoço às 12:30)'"\n"'✔ Fervedouro Encontro dos Rios'"\n"'✔ Encontro do Rio Formiga e Rio Sono'"\n"'✔ Cachoeira do Formiga'"\n"'(Segue para São Felix, chegada às 18h, jantar às 19:30, pernoite)'"\n""\n"'4° dia'"\n""\n"'(Saída às 08:00h para visitação dos Atrativos)'"\n"'✔ Fervedouro Alecrim'"\n"'✔ Praia do Alecrim'"\n"'✔ Fervedouro Bela vista (maior do Jalapão)'"\n"'✔ Cachoeira das Araras'"\n"'(Almoço as 12:00h)'"\n"'✔ Serra da Catedral'"\n"'✔ Morro vermelho'"\n"'(Saída para Palmas as 13h e chegada às 18:00h)'"\n""\n"'Digite "Sim" para confirmar a solicitação ou "menu" para voltar'
        

        elif mensagem == 'C' or mensagem == 'c':
          return f'Roteiro de 6 dias e 5 noites: \n \n 1° dia \n \n''(Saída de Palmas as 8:00h)''\n''✔ Cachoeira Roncadeira''\n''opcional:Rappel (vide Esportes Radicais)''\n''✔ Cachoeira escorrega macaco''\n''(Almoço em Ponte Alta as 12:30h)''\n''✔ Cachoeira do soninho'"\n"'✔ Rio soninho'"\n"'✔ Por do sol pedra furada'"\n"'(Janta e Pernoite em Ponte Alta)''\n\n''2° dia'"\n\n"'✔ Lagoa do Japonês ( um dia de lazer)'"\n"'(Almoço às 12:00h)'"\n"'✔ Praia do Buriti'"\n\n "'3° dia'"\n\n"'(Saída as 7:30h de Ponte Alta do Tocantins)'"\n"'✔ Canyon do Sussuapara'"\n"'✔ Cachoeira da Velha'"\n"'✔ Prainha do Rio Novo'"\n"'(Lanche as 12:00, no percurso não tem restaurantes)'"\n"'✔ Rio Novo (comunidade Quilombola)'"\n"'✔ Dunas'"\n"'(Chegada à Mateiros as 19:30, jantar e pernoite)'"\n\n"'4° dia'"\n\n"'(Saída às 8:00h de Mateiros)'"\n"'✔ Cachoeira do Formiga'"\n"'✔ Fervedouro Encontro águas ( mais forte do Jalapão)'"\n"'✔ Encontro das Aguas ( Rio formiga e Rio sono)'"\n"'✔ Fervedouro Buritizinho'"\n"'(Almoço às 12:30)'"\n"'(Segue para São Felix, chegada às 18h, jantar às 19:30, pernoite)'"\n\n"'5° dia'"\n\n"'(Saída às 08:00h para visitação dos Atrativos)'"\n"'✔ Fervedouro Buritis'"\n"'✔ Fervedouro Bananeiras(Ceiça)'"\n"'✔ Mumbuca (Comunidade Quilombola)'"\n"'✔ Fervedouro Rio Sono'"\n\n"'6° dia'"\n""\n"'(Saída às 08:00h para visitação dos Atrativos)'"\n"'✔ Fervedouro Alecrim'"\n"'✔ Praia do Alecrim'"\n"'✔ Fervedouro Bela vista (maior do Jalapão)'"\n"'✔ Cachoeira das Araras'"\n"'(Almoço as 12:00h)'"\n"'✔ Serra da Catedral'"\n"'✔ Morro vermelho'"\n"'(Saída para Palmas as 13h e chegada às 18:00h)\n\n"Digite "Sim" para confirmar a solicitação ou "menu" para voltar'
        

        if mensagem == '3':
          return f'👩‍💼 Você será redirecionado para um de nossos atendentes assim que possível.'


        if mensagem == 'sobre':
          return f'Acesse o site da Capim de Ouro para conhecer todos os pacotes disponíveis! Disponível em: https://www.capimdeouro.com.br/pacotes.html# 😉 \n Este BOT é um projeto pessoal de Engenharia de Software, incetivado pela UniCatólica do Tocantins.\n V0.5 '

        elif mensagem.lower() in ('s', 'sim'):
          return 'Sua solicitação acaba de ser registrada e logo será confirmada por um de nossos atendentes. Obrigado por escolher a TurismoTocantins!🥳'
        elif mensagem.lower() in ('n', 'não'):
          return '😐 Gostaria de acessar novamente o menu? digite "menu"!'
        else:
          return 'Gostaria de acessar o menu de opções? Digite "menu"'

    def resposta_chat(self, resposta, chat_id): # Envio da mensagem para o chat em específico
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = JaoJalapao()
bot.iniciar()
