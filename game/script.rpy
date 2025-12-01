label start:
    jump prologue

label after_chapter_01:
    jump chapter_02_meeting

label after_chapter_02:
    jump chapter_03_secret

label after_chapter_03:
    jump chapter_04_decision

label after_chapter_04:
    jump story_ending

label story_ending:
    scene solid "#0e1621"
    
    "История подошла к концу."
    "Спасибо за прохождение!"
    
    return