init python:
    def new_message(sender, content):
        """Отправить новое сообщение"""
        message_system.send_message(sender, content)
        
    def simulate_typing(duration=1.5):
        """Симулировать печатание собеседника"""
        message_system.indicate_typing()
        renpy.pause(duration)
        message_system.stop_typing_indicator()
    
    def show_message_interface():
        """Показать интерфейс сообщений"""
        message_system.show_interface()
        
    def hide_message_interface():
        """Скрыть интерфейс сообщений"""
        message_system.hide_interface()
        