# Основные стили интерфейса
style message_window:
    xsize 1200
    ysize 800
    xalign 0.5
    yalign 0.5
    background "#0e1621"
    padding (0, 0, 0, 0)

style interface_header:
    size 18
    bold True
    color "#ffffff"
    xalign 0.0

style incoming_message:
    xalign 0.0
    xmaximum 700
    padding (12, 16, 16, 12)
    margin (10, 5, 10, 5)
    background Frame(Solid("#182533"), borders=12)

style outgoing_message:
    xalign 1.0
    xmaximum 700
    padding (12, 16, 16, 12)
    margin (10, 5, 10, 5)
    background Frame(Solid("#2b5278"), borders=12)

style message_content:
    size 14
    color "#ffffff"
    line_leading 2

style timestamp:
    size 11
    color "#a8b2bd"
    italic False

style info_text:
    size 12
    color "#a8b2bd"

style close_button:
    background "#1e2c3d"
    hover_background "#e81123"
    color "#ffffff"
    padding (15, 5, 15, 5)

style load_button:
    background "#2b5278"
    hover_background "#3a6a97"
    color "#ffffff"
    padding (12, 8, 12, 8)

# Иконки участников диалога
image partner_icon = Composite(
    (40, 40),
    (0, 0), "#6ab3f3",
    (0, 0), "#00000008",
    (15, 13), Text("П", size=14, color="#ffffff")
)

image user_icon = Composite(
    (40, 40),
    (0, 0), "#6ab3f3",
    (0, 0), "#00000008",
    (15, 13), Text("Я", size=14, color="#ffffff")
)

# Анимации
transform message_appear:
    alpha 0.0
    yoffset 10
    easein 0.2 alpha 1.0 yoffset 0

transform typing_animation:
    alpha 0.5
    easein 0.6 alpha 1.0
    easeout 0.6 alpha 0.5
    repeat
