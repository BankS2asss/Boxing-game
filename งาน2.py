import tkinter as tk
import random

window = tk.Tk()
window.title("🥊 Boxing Game")

player_hp = 100
bot_hp = 100
game_over = False

status_label = tk.Label(window, font=("Arial", 14))
status_label.pack(pady=10)

result_label = tk.Label(window, font=("Arial", 12))
result_label.pack(pady=5)

def update_status():
    status_label.config(text=f"Your HP: {player_hp} | Bot HP: {bot_hp}")

def check_game_over():
    global game_over
    if player_hp <= 0 or bot_hp <= 0:
        game_over = True
        if player_hp > 0:
            result_label.config(text="🎉 YOU WIN!")
        else:
            result_label.config(text="💀 YOU LOSE!")
        return True   # ทำงานเหมือน break
    return False

def bot_attack(blocking=False):
    global player_hp
    damage = random.randint(10, 20)
    if blocking:
        damage //= 2
    player_hp -= damage

def light():
    global bot_hp
    if game_over: 
        return
    bot_hp -= random.randint(10, 15)
    if check_game_over(): 
        return
    bot_attack()
    update_status()
    check_game_over()

def heavy():
    global bot_hp
    if game_over: 
        return
    bot_hp -= random.randint(15, 25)
    if check_game_over(): 
        return
    bot_attack()
    update_status()
    check_game_over()

def block():
    if game_over: 
        return
    bot_attack(blocking=True)
    update_status()
    check_game_over()

tk.Button(window, text="Light Punch", width=15, command=light).pack(pady=5)
tk.Button(window, text="Heavy Punch", width=15, command=heavy).pack(pady=5)
tk.Button(window, text="Block", width=15, command=block).pack(pady=5)

update_status()
window.mainloop()