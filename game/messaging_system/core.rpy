# Persistent переменная для истории сообщений
default persistent.message_history = []
default persistent.message = []

init python:
    class MessageSystem:
        def __init__(self, max_messages=200, display_count=50):
            self.max_messages = max_messages
            self.display_count = display_count
            self.interface_visible = False
            self.user_typing = False
            
            if not hasattr(persistent, "message_history"):
                persistent.message_history = []
                
            self.all_messages = persistent.message_history
            
        def send_message(self, sender, content):
            import time
            current_time = time.strftime("%H:%M")
            
            self.all_messages.append({
                "sender": sender, 
                "content": content, 
                "timestamp": current_time
            })
            
            if len(self.all_messages) > self.max_messages:
                messages_to_remove = len(self.all_messages) - self.max_messages
                self.all_messages = self.all_messages[messages_to_remove:]
                
            persistent.message_history = self.all_messages
            
            if self.interface_visible:
                renpy.restart_interaction()
                
        def get_visible_messages(self):
            start_index = max(0, len(self.all_messages) - self.display_count)
            return self.all_messages[start_index:]
            
        def can_display_more(self):
            return self.display_count < len(self.all_messages)
            
        def increase_display_limit(self):
            self.display_count = min(self.display_count + 30, len(self.all_messages))
            renpy.restart_interaction()
            
        def get_conversation_stats(self):
            partner_count = len([m for m in self.all_messages if m["sender"] == "partner"])
            user_count = len([m for m in self.all_messages if m["sender"] == "user"])
                
            return {
                "total": len(self.all_messages),
                "visible": self.display_count,
                "partner_messages": partner_count,
                "user_messages": user_count
            }
        
        def show_interface(self):
            self.interface_visible = True
            renpy.show_screen("message_interface")
            
        def hide_interface(self):
            self.interface_visible = False
            renpy.hide_screen("message_interface")
            
        def indicate_typing(self):
            self.user_typing = True
            renpy.restart_interaction()
            
        def stop_typing_indicator(self):
            self.user_typing = False
            renpy.restart_interaction()

default message_system = MessageSystem()
