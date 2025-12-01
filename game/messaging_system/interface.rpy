# game/messaging_system/interface.rpy

# Основной интерфейс сообщений (без настроек)
screen message_interface():
    $ visible_messages = message_system.get_visible_messages()
    $ stats = message_system.get_conversation_stats()
    
    frame:
        style "message_window"
        
        vbox:
            spacing 0
            
            # Панель заголовка (только крестик для закрытия)
            frame:
                background "#1e2c3d"
                padding (12, 8, 12, 8)
                xsize 1200
                
                hbox:
                    xfill True
                    text "Мессенджер" style "interface_header" yalign 0.5
                    
                    # Только крестик для закрытия
                    textbutton "×":
                        action Return()
                        style "close_button"
                        xalign 1.0
            
            # Область диалога
            frame:
                background "#0e1621"
                padding (20, 20, 20, 20)
                xsize 1200
                ysize 700
                
                viewport:
                    id "dialog_viewport"
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    ysize 660
                    
                    vbox:
                        spacing 12
                        
                        # Сообщение если чат пуст
                        if stats["total"] == 0:
                            text "💬 Начните диалог..." style "info_text" xalign 0.5 yalign 0.5
                        
                        # Кнопка загрузки старых сообщений
                        if message_system.can_display_more():
                            textbutton "🔄 Показать предыдущие сообщения" action Function(message_system.increase_display_limit):
                                style "load_button"
                                xalign 0.5
                        
                        # Отображение сообщений
                        for msg in visible_messages:
                            if msg["sender"] == "partner":
                                # Сообщения собеседника слева
                                hbox:
                                    spacing 12
                                    at message_appear
                                    add "partner_icon"
                                    vbox:
                                        xmaximum 700
                                        frame:
                                            style "incoming_message"
                                            text msg["content"] style "message_content"
                                        hbox:
                                            text msg["timestamp"] style "timestamp"
                                            null width 8
                                            text "✓✓" style "timestamp" color "#6ab3f3"
                            else:
                                # Сообщения пользователя справа
                                hbox:
                                    spacing 12
                                    at message_appear
                                    xalign 1.0
                                    xoffset 400
                                    hbox:
                                        spacing 8
                                        vbox:
                                            xmaximum 700
                                            xalign 1.0
                                            frame:
                                                style "outgoing_message"
                                                text msg["content"] style "message_content"
                                            hbox:
                                                xalign 1.0
                                                text "✓✓" style "timestamp" color "#6ab3f3"
                                                null width 8
                                                text msg["timestamp"] style "timestamp"
                                        add "user_icon"
                        
                        # Индикатор "печатает..."
                        if message_system.user_typing:
                            hbox:
                                spacing 12
                                add "partner_icon"
                                vbox:
                                    xmaximum 700
                                    frame:
                                        style "incoming_message"
                                        text "печатает..." style "message_content" at typing_animation
            
            # Простая статусная строка
            frame:
                background "#1e2c3d"
                padding (15, 12, 15, 12)
                xsize 1200
                
                hbox:
                    xfill True
                    text "💾 Сообщения: {}/{}".format(
                        stats["visible"], 
                        stats["total"]
                    ) style "info_text" yalign 0.5