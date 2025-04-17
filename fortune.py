
print("🔮 Welcome to Aakash Raj's Fortune Teller (21JE0002) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Aakash! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Tough times don’t last, but tough people like you do. ✨")
elif mood == "neutral":
    print("✨ Your fortune: Balance is the key. A surprise is coming your way. ✨")
else:
    print("🤔 I couldn't recognize that mood. Please try again with happy/sad/neutral.")