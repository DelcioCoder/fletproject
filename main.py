import flet as ft


def main(pagina):
    logo = ft.Text('WHATSAPP CLONE MESSAGE')
    chat = ft.Column()
    campo_nome = ft.TextField(label='Digite o seu nome')
    pagina.add(chat)

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(e):
        pagina.pubsub.send_all(campo_mensagem.value)
        campo_mensagem.value = ''
        pagina.update()


    campo_mensagem = ft.TextField(label='Escreva sua mensagem')
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    def entrar_popup(e):
        popup.open = False
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar]
        ))
        pagina.update()


    popup = ft.AlertDialog(
        open = False,
        title = ft.Text('Bem vindo ao whatsapp clone'),
        content = campo_nome,
        actions = [
            ft.ElevatedButton('Entrar', on_click=entrar_popup)
        ]

    )

    def entrar_chat(e):
        pagina.remove(logo)
        pagina.remove(botao_entrar)
        pagina.dialog = popup
        popup.open = True
        pagina.update()



    botao_entrar = ft.ElevatedButton('Entrar', on_click=entrar_chat)
    pagina.add(logo)
    pagina.add(botao_entrar)
    pagina.update()



ft.app(target=main, view=ft.WEB_BROWSER)