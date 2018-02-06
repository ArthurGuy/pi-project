from guizero import App, Text

app = App(title="System status")

welcome_message = Text(app, text="System temp:")

app.display()
