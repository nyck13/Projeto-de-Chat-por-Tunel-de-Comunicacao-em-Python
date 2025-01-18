import flet as ft # importar a biblioteca flet para criação do protótipo 

def main(pagina): # criação da interface main 
    # criação do título da página
    titulo = ft.Text('NyZAP')

    # criação da organização do chat
    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem): # função que envia a mensagem pelo túnel de comunicação 
        texto = ft.Text(mensagem)
        chat.controls.append(texto) # inserção no final da página, a mensagem enviada e por quem foi
        pagina.update() # atualização da página para novas informações serem processadas 

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # criação do túnel de comunicação

    def enviar_mensagem(evento): # função que envia as mensagens no chat 
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f'{nome_usuario}: {texto_campo_mensagem}'
        pagina.pubsub.send_all(mensagem) # envio da mensagem pelo túnel

        campo_enviar_mensagem.value = '' # limpar caixa de enviar mensagem para uso posterior
        pagina.update()

    # criação do campo de enviar mensagem com a devida formatação e aparência 
    campo_enviar_mensagem = ft.TextField(label='Digite aqui sua mensagem', on_submit=enviar_mensagem)
    
    # criação do botão com a formação deseja e a ação que realizará ao ser pressionado
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    # criação da linha para escrita de mensagens organizados em sequência por uma lista 
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])


    def entrar_chat(evento):
        # remoção dos antigos atributos
        popup.open = False 
        pagina.remove(titulo)
        pagina.remove(botao)
        
        # inserção dos novos itens para página
        pagina.add(chat)
        pagina.add(linha_enviar)
        nome_usuario = caixa_nome.value
        mensagem = f'{nome_usuario} entrou no chat' # mensagem executada no túnel assim que um novo integrante entrar no chat 
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    # criação e estilização do PopUp que aparece ao clicar em entrar no chat
    titulo_popup = ft.Text('Bem-vindo ao NyZAP')
    caixa_nome = ft.TextField(label='Digite o seu nome')
    botao_popup = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    def abrir_popup(evento): 
        pagina.dialog = popup
        popup.open = True
        pagina.update()
 
    botao = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)

    # adicionar o título e o botão na pagina
    pagina.add(botao)
    pagina.add(titulo)

ft.app(target=main, port=8551, view=ft.WEB_BROWSER) # função que inicializa a aplicação de fato
  