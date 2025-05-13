# ----------------------------
# Who Said That? - Full Game Script 
# Python + Tkinter + Pygame implementation
# ----------------------------

import tkinter as tk
from tkinter import ttk
import random
import os
from PIL import Image, ImageTk
import re
import pygame

# ----------------------------
# Initialize Pygame mixer for sound
# ----------------------------
pygame.mixer.init()

# ----------------------------
# Global Audio Settings
# ----------------------------
AUDIO_DIR = "Audio"
SOUND_ENABLED = True
VOLUME = 0.5

# ----------------------------
# Sound & Music Utilities
# ----------------------------
def play_sound(filename):
    if SOUND_ENABLED:
        try:
            sound = pygame.mixer.Sound(os.path.join(AUDIO_DIR, filename))
            sound.set_volume(VOLUME)
            sound.play()
            #sound error code
        except Exception as e:
            print(f"Sound error: {filename}", e)

def play_music(track, loop=-1):
    if SOUND_ENABLED:
        try:
            pygame.mixer.music.stop()
            path = os.path.join(AUDIO_DIR, track)
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(VOLUME)
            pygame.mixer.music.play(loops=loop)
        except Exception as e:
            print(f"Music error: {track}", e)
#
def stop_music():
    pygame.mixer.music.stop()
#for timing of sound to match "animations"
def stop_typewriter_sound():
    pygame.mixer.stop()

def stop_shuffle_sound():
    pygame.mixer.stop()

# ----------------------------
# Quotes presented during gameplay
# ----------------------------
RUDE_QUOTES = [
    "You’re so articulate—for someone like you.",
    "Can I touch your hair?",
    "Where are you really from?",
    "That's an interesting name. How do you say it again?",
    "You must be on scholarship, right?",
    "Oh, I didn’t expect you to live here.",
    "I don’t see color—I treat everyone the same.",
    "It’s just a joke, calm down.",
    "Wow, you're surprisingly good at this.",
    "Do you even pay taxes?",
    "You’re one of the good ones.",
    "You're not like the others.",
    "Your English is really good!",
    "Is that your real hair?",
    "You don't look gay.",
    "You don’t act Black.",
    "I wish I was exotic like you.",
    "You're really pretty for a dark-skinned girl.",
    "That's so ghetto.",
    "You speak so well!",
    "I don't see why people are so sensitive nowadays.",
    "It must be nice getting into college for free.",
    "So, you're the diversity hire?",
    "You're not that intimidating once I get to know you.",
    "You look so ethnic in that outfit.",
    "You have a white name!",
    "You're basically white.",
    "You probably grew up in the hood, right?",
    "You're not oppressed anymore—get over it.",
    "Why do you people always make it about race?",
    "It’s reverse racism if I can’t say it too.",
    "Black people are so loud.",
    "You must be good at sports.",
    "You must know how to dance.",
    "That's not how you pronounce it in America.",
    "You're lucky you're not darker.",
    "I bet you can cook soul food, huh?",
    "You guys are always late.",
    "You all look alike to me.",
    "Do you even celebrate Christmas?",
    "You probably voted for Biden, right?",
    "Why are you so angry all the time?",
    "You're actually really nice!",
    "You're smarter than I expected.",
    "I just don't think racism is a thing anymore.",
    "You probably don’t even need sunscreen.",
    "Oh, you must be mixed.",
    "You people have such rhythm.",
    "You’re not like other Muslims.",
    "Do you know how to twerk?",
    "You’re too pretty to be trans.",
    "You’re too sensitive.",
    "That’s not racist, it’s just a joke!",
    "Calm down, you’re overreacting.",
    "I don't see what's wrong with that word.",
    "I have Black friends, I can say it.",
    "If you worked harder, you'd get ahead.",
    "You probably got in because of affirmative action.",
    "You people are so dramatic.",
    "I don’t see color, I only see people.",
    "You all have such strong genes.",
    "You don’t look Native.",
    "You sound white on the phone.",
    "You're not one of those woke people, are you?",
    "You're too loud for the office.",
    "You dress so urban.",
    "Do you even eat meat?",
    "You're so lucky you can tan.",
    "You talk so white.",
    "You don't even act gay.",
    "Is it hard being a woman in tech?",
    "You should smile more.",
    "Are you even from here?",
    "You're intimidating when you speak up.",
    "That's not how it's done in America.",
    "So what are you, really?",
    "But you people are so athletic!",
    "Wow, you're not what I expected.",
    "Do you know how to braid?",
    "You don't look autistic.",
    "You're disabled? But you're so normal!",
    "Is that your real name?",
    "You’re so exotic looking.",
    "You’re so independent—for a woman.",
    "Why don’t you wear makeup?",
    "You don’t look Jewish.",
    "I didn't think you'd be into that kind of music.",
    "You look like you have attitude.",
    "You're basically white on the inside.",
    "You’re really clean for a guy.",
    "You probably love spicy food, huh?",
    "You're not offended by that, are you?",
    "You’re just being politically correct.",
    "You must be from Africa somewhere.",
    "Why do you people always play the victim?",
    "Your people are always so creative.",
    "I can't tell what race you are—so cool!",
    "That’s your real skin tone?",
    "You guys are so lucky with your scholarships.",
    "Oh, I thought you were the help.",
    "So how many baby daddies do you have?",
    "I love Black culture, but not the drama.",
    "So who's the man in the relationship?",
    "I bet you know how to fight.",
    "I love how sassy you are!"
]

# ----------------------------
# Calculate score based on character-by-character match
# ----------------------------

def calculate_score(player_input, correct_text):
    correct_text = correct_text.lower()
    player_input = player_input.lower()
    total_chars = len(correct_text)
    match_count = sum(1 for i, c in enumerate(player_input) if i < total_chars and c == correct_text[i])
    return round((match_count / total_chars) * 100)

# ----------------------------
# Holds configuration per round
# ----------------------------
class GameConfig:
    def __init__(self):
        self.difficulty = "Easy"
        self.num_people = 10
        self.display_time = 5
        self.score = 0
        self.point_multiplier = 0.1

# ----------------------------
# Main Game Application Class
# ----------------------------
class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Who Said That?")
        self.config = GameConfig()
        self.total_score = 0
        self.image_folder = "Character Assets"
        self.available_images = self.find_valid_images()

        # Variable original locat
        self.selected_person = None
        self.character_image = None
        self.current_character_file = None
        self.rude_text = None
        self.guess_images = []
        self.guess_image_objs = {}
        self.image_buttons = {}
        self.shuffle_count = 0

        self.sound_enabled_var = tk.BooleanVar(value=True)
        self.volume_var = tk.DoubleVar(value=0.5)

        play_music("intro_track.wav", loop=-1)
        self.create_main_menu()

    def find_valid_images(self):
        files = os.listdir(self.image_folder)
        #naming key for image assets
        pattern = re.compile(r"output \((\d+)\)\.(jpg|jpeg)", re.IGNORECASE)
        return [f for f in files if pattern.match(f)]

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ----------------------------
    # Main Menu Screen
    # ----------------------------
    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Who Said That?", font=("Helvetica", 24)).pack(pady=20)

        tk.Label(self.root, text="Select Starting Difficulty:").pack()
        self.difficulty_var = tk.StringVar(value="Easy")
        ttk.Combobox(self.root, textvariable=self.difficulty_var, values=("Easy", "Medium", "Hard"), state="readonly").pack(pady=10)

        #Sound settings section
        sound_frame = tk.Frame(self.root)
        sound_frame.pack(pady=10)
        tk.Checkbutton(sound_frame, text="Enable Sound", variable=self.sound_enabled_var, command=self.toggle_sound).pack(side="left", padx=5)
        tk.Label(sound_frame, text="Volume:").pack(side="left")
        tk.Scale(sound_frame, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, variable=self.volume_var, command=self.set_volume).pack(side="left")

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=20)
        play_sound("intro_chord.wav")

    def toggle_sound(self):
        global SOUND_ENABLED
        SOUND_ENABLED = self.sound_enabled_var.get()
        if not SOUND_ENABLED:
            stop_music()
        else:
            play_music("intro_track.wav", loop=1)

    def set_volume(self, val):
        global VOLUME
        VOLUME = float(val)
        pygame.mixer.music.set_volume(VOLUME)

    def start_game(self):
        stop_music()
        play_music("game_loop.wav", loop=-1)
        self.choose_round_difficulty()

    # ----------------------------
    # Prompt difficulty before each round
    # ----------------------------
    def choose_round_difficulty(self):
        self.clear_window()
        tk.Label(self.root, text="Choose Round Difficulty:", font=("Helvetica", 18)).pack(pady=10)

        def select(diff):
            self.config.difficulty = diff
            settings = {
                "Easy": (10, 2000, 0.1),
                "Medium": (25, 1500, 0.5),
                "Hard": (50, 1000, 1.0)
            }
            self.config.num_people, self.config.display_time, self.config.point_multiplier = settings[diff]
            self.show_rude_person()

        for diff in ["Easy", "Medium", "Hard"]:
            tk.Button(self.root, text=diff, command=lambda d=diff: select(d)).pack(pady=5)

    def show_rude_person(self):
        self.clear_window()
        self.guess_images = random.sample(self.available_images, self.config.num_people)
        self.current_character_file = random.choice(self.guess_images)
        self.rude_text = random.choice(RUDE_QUOTES)

        img = Image.open(os.path.join(self.image_folder, self.current_character_file)).resize((200, 200))
        self.character_image = ImageTk.PhotoImage(img)
        tk.Label(self.root, image=self.character_image).pack(pady=20)

        text_display = tk.Label(self.root, font=("Helvetica", 16), wraplength=600)
        text_display.pack(pady=10)

        def typewriter(text, index=0):
            if index == 1:
                play_sound("typewriter.wav")
                self.root.after(1500, stop_typewriter_sound)
            if index < len(text):
                text_display.config(text=text[:index + 1])
                self.root.after(40, lambda: typewriter(text, index + 1))
            else:
                self.root.after(self.config.display_time, self.start_guessing_phase)

        typewriter(f'"{self.rude_text}"')

    def start_guessing_phase(self):
        self.shuffle_count = 0
        self.max_shuffles = {"Medium": 3, "Hard": 5}.get(self.config.difficulty, 0)
        self.show_guessing_stage()

    def show_guessing_stage(self):
        self.clear_window()
        self.selected_person = tk.StringVar(value="")
        self.guess_image_objs = {}
        self.image_buttons = {}

        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)

        self.answer_entry = tk.Entry(self.root, width=60)
        self.answer_entry.pack(pady=10)
        self.submit_btn = tk.Button(self.root, text="Submit", command=self.check_answer, state="disabled")
        self.submit_btn.pack(pady=10)

        self.shuffle_images()

    def shuffle_images(self):
        play_sound("card_shuffle.wav")
        if self.config.difficulty == "Medium":
            self.root.after(1000, stop_shuffle_sound)
        elif self.config.difficulty == "Hard":
            self.root.after(1500, stop_shuffle_sound)

        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        random.shuffle(self.guess_images)

        for idx, filename in enumerate(self.guess_images):
            img = Image.open(os.path.join(self.image_folder, filename)).resize((64, 64))
            tk_img = ImageTk.PhotoImage(img)
            self.guess_image_objs[filename] = tk_img

            btn = tk.Button(self.grid_frame, image=tk_img, borderwidth=4, relief="flat", state="disabled",
                            command=lambda f=filename: self.select_person(f))
            btn.grid(row=idx//10, column=idx%10, padx=4, pady=4)
            self.image_buttons[filename] = btn

        if self.config.difficulty in ["Medium", "Hard"] and self.shuffle_count < self.max_shuffles:
            self.shuffle_count += 1
            self.root.after(500, self.shuffle_images)
        else:
            for btn in self.image_buttons.values():
                btn.config(state="normal")
            self.submit_btn.config(state="normal")

    def select_person(self, filename):
        self.selected_person.set(filename)
        for f, btn in self.image_buttons.items():
            btn.config(highlightbackground="gray", highlightthickness=0, bg="SystemButtonFace")
        self.image_buttons[filename].config(highlightbackground="yellow", highlightthickness=2)

    def check_answer(self):
        selected = self.selected_person.get()
        typed = self.answer_entry.get().strip()

        for f, btn in self.image_buttons.items():
            btn.config(highlightbackground="gray", highlightthickness=0)

        if selected == self.current_character_file:
            base_score = calculate_score(typed, self.rude_text)
            round_score = round(base_score * self.config.point_multiplier)
            self.total_score += round_score
            play_sound("success_chime.wav")
            self.image_buttons[selected].config(highlightbackground="green", highlightthickness=3)
        else:
            self.total_score = 0
            play_sound("buzzer.wav")
            if selected:
                self.image_buttons[selected].config(highlightbackground="red", highlightthickness=3)
            self.image_buttons[self.current_character_file].config(highlightbackground="green", highlightthickness=3)

        self.root.after(1500, self.ask_to_continue)

    def ask_to_continue(self):
        self.clear_window()
        play_sound("score_count.wav")
        tk.Label(self.root, text=f"Your Total Score: {self.total_score} pts", font=("Helvetica", 20)).pack(pady=20)
        tk.Label(self.root, text="Keep playing? Select next round difficulty:").pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        for diff in ["Easy", "Medium", "Hard"]:
            tk.Button(btn_frame, text=diff, command=lambda d=diff: self.choose_next_round(d)).pack(side="left", padx=5)
        tk.Button(self.root, text="End Game", command=self.create_main_menu).pack(pady=10)

    def choose_next_round(self, diff):
        settings = {
            "Easy": (10, 2000, 0.1),
            "Medium": (25, 1500, 0.5),
            "Hard": (50, 1000, 1.0)
        }
        self.config.difficulty = diff
        self.config.num_people, self.config.display_time, self.config.point_multiplier = settings[diff]
        self.show_rude_person()

# ----------------------------
# Start the application
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x800")
    app = GameApp(root)
    root.mainloop()