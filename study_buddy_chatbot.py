import pywhatkit as kit
import schedule
import time
import json
import os
from datetime import datetime, timedelta

FILE = "student_goals.json"

def load_goals():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

def save_goals(goals):
    with open(FILE, 'w') as f:
        json.dump(goals, f)

def get_phone_number():
    phone_number = input("Enter your WhatsApp number with country code (+1234567890): ")
    with open('phone.txt', 'w') as f:
        f.write(phone_number)
    return phone_number

def send_evening_question():
    try:
        number = open('phone.txt').read().strip()
        message = "🌙 Hey! Study Buddy here!\n\nWhat's ONE thing you want to accomplish tomorrow?"
        kit.sendwhatmsg(number, message, 21, 0)
        print("✓ Evening question scheduled for 9 PM!")
    except:
        print("❌ Set up your phone number first!")

def send_morning_checkin():
    try:
        number = open('phone.txt').read().strip()
        message = "✨ Good evening!\n\nDid you accomplish your goal? YES or NO?"
        kit.sendwhatmsg(number, message, 21, 30)
        print("✓ Check-in scheduled!")
    except:
        print("❌ Set up your phone number first!")

def view_goals():
    goals = load_goals()
    if goals:
        print("\n📚 YOUR GOALS:")
        for i, goal in enumerate(goals, 1):
            print(f"{i}. {goal}")
    else:
        print("\n📝 No goals saved yet!")

def main():
    print("\n🌟 STUDY BUDDY - Your friendly study companion 🌟\n")
    
    if not os.path.exists('phone.txt'):
        print("First time setup!")
        get_phone_number()
    
    while True:
        print("\n" + "="*50)
        print("MENU:")
        print("1 - Send evening question (9 PM)")
        print("2 - Send check-in (9:30 PM)")
        print("3 - View my goals")
        print("4 - Set my phone number")
        print("5 - Exit")
        print("="*50)

        choice = input("\nYour choice (1-5): ").strip()

        if choice == '1':
            send_evening_question()
        elif choice == '2':
            send_morning_checkin()
        elif choice == '3':
            view_goals()
        elif choice == '4':
            get_phone_number()
            print("✓ Phone number saved!")
        elif choice == '5':
            print("\n👋 See you next time! Keep studying!")
            break
        else:
            print("\n❌ Invalid option. Try again.")

if __name__ == '__main__':
    main()