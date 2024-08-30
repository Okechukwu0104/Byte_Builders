def nokia():
    while True:
        print("""
            NOKIA MENU

            1 -> Phonebook
            2 -> Messages
            3 -> Chat
            4 -> Call Register
            5 -> Tones
            6 -> Settings
            7 -> Call divert
            8 -> Games Sections
            9 -> Calculator
            10 -> Reminders
            11 -> Clock
            12 -> Profiles
            13 -> SIM services
            0 -> Exit
        """)

        main_menu = int(input("Select an option: "))

        match main_menu:
            case 1:
                phonebook_menu()
            case 2:
                messages_menu()
            case 3:
                chats_menu()
            case 4:
                call_register_menu()
            case 5:
                tones_menu()
            case 6:
                settings_menu()
            case 7:
                call_divert_menu()
            case 8:
                games_sections_menu()
            case 9:
                calculator_menu()
            case 10:
                reminders_menu()
            case 11:
                clock_menu()
            case 12:
                profiles_menu()
            case 13:
                sim_services_menu()
            case 0:
                print("NOKIA....CONNECTING PEOPLE")
                break
            case _:
                print("Pls pick a valid number")


def phonebook_menu():
    while True:
        print("""
            PHONE BOOK

            1 -> Search
            2 -> Service Nos.
            3 -> Add Name 
            4 -> Erase
            5 -> Edit
            6 -> Assign Tone
            7 -> Send bcard
            8 -> Options
            9 -> Speed dials
            10 -> Voice tags
            0 -> Main menu
        """)

        phonebook_options = int(input("Select option: "))

        match phonebook_options:
            case 1: 
                print("Search")
            case 2: 
                print("Service Nos")
            case 3: 
                print("Add name")
            case 4: 
                print("Erase")
            case 5: 
                print("Edit")
            case 6: 
                print("Assign Tone")
            case 7: 
                print("Send b card")
            case 8: 
                options_menu() 
            case 9: 
                print("Speed dials")
            case 10:
                print("Voice tags")
            case 0: 
                return
            case _:
                print("Pls pick a valid number")


def options_menu():
    while True:
        print("""
            OPTIONS

            1 -> Type of view
            2 -> Memory status
            0 -> Main menu
        """)

        options_input = int(input("Select an option: "))

        match options_input:
            case 1:
                print("Type of view")
            case 2:
                print("Memory status")
            case 0:
                return
            case _:
                print("Pls pick a valid number")


def messages_menu():
    while True:
        print("""
            MESSAGES

            1 -> Write messages
            2 -> Inbox
            3 -> Outbox
            4 -> Picture messages
            5 -> Templates
            6 -> Smileys
            7 -> Message settings
            0 -> Main menu
        """)

        message_options = int(input("Select an option:"))

        match message_options:
            case 1:
                print("Write message...")
            case 2: 
                print("Inbox...")
            case 3: 
                print("Outbox")
            case 4: 
                print("Picture messages")
            case 5: 
                print("Templates")
            case 6: 
                print("Smileys")
            case 7: 
                message_settings_menu()
            case 0: 
                return
            case _: 
                print("Pls pick a valid number")

def message_settings_menu():
    while True:
        print("""
            MESSAGE SETTINGS

            1 -> Set 1
            2 -> Common
            0 -> Back
        """)

        settings_options = int(input("Select an option:"))

        match settings_options:
            case 1:
                print("""
                    1 -> Message center number
                    2 -> Message sent as
                    3 -> Message validity
                    0 -> Back
                """)
                set1_options = int(input("Select option:"))
                match set1_options:
                    case 1:
                        print("Message center number")
                    case 2:
                        print("Message sent as")
                    case 3:
                        print("Message validity")
                    case 0:
                        return
                    case _:
                        print("Pls pick a valid number")
            case 2:
                print("""
                    1 -> Delivery reports
                    2 -> Reply via same centre
                    3 -> Character support
                    0 -> Back
                """)
                common_options = int(input("Select option:"))
                match common_options:
                    case 1:
                        print("Delivery reports")
                    case 2:
                        print("Reply via same centre")
                    case 3:
                        print("Character support")
                    case 0:
                        return
                    case _:
                        print("Pls pick a valid number")
            case 0:
                return
            case _:
                print("Pls pick a valid number")


def chats_menu():
    while True:
        print("""
            CHATS...

            1. Okechukwu Jeffery
            2. Henry Cavendish
            3. Louis Kleon

            0 -> Main menu
        """)

        chats_options = int(input("Enter option: "))
        match chats_options:
            case 0: 
                return
            case _: 
                print("Pls don't select the chat. They won't chat you back")


def call_register_menu():
    while True:
        print("""
            CALL REGISTER

            1 -> Missed calls
            2 -> Received calls
            3 -> Dialed Numbers
            4 -> Erase recent call lists
            5 -> Show call duration
            6 -> Show call cost
            7 -> Clear counters
            8 -> Prepaid credit
            0 -> Main menu
        """)

        call_register_options = int(input("Enter option: "))
        match call_register_options:
            case 1: 
                print("Missed calls")    
            case 2: 
                print("Received calls")
            case 3: 
                print("Dialed Numbers")
            case 4: 
                print("Erase recent call lists")    
            case 5: 
                show_call_duration_menu()
            case 6: 
                show_call_cost_menu()
            case 7: 
                clear_counters_menu()
            case 8: 
                print("Prepaid credit")
            case 0:
                return
            case _: 
                print("Pls pick a valid number")


def show_call_duration_menu():
    while True:
        print("""
            SHOW CALL DURATION

            1 -> Last call duration
            2 -> All calls' duration
            3 -> Received calls' duration
            4 -> Dialed calls' duration
            5 -> Clear Timers
            0 -> Back
        """)

        show_call_duration_options = int(input("Enter option: "))
        match show_call_duration_options:
            case 1: 
                print("Last call duration")    
            case 2: 
                print("All calls' duration")
            case 3: 
                print("Received calls' duration")
            case 4: 
                print("Dialed calls' duration")
            case 5: 
                print("Clear Timers")
            case 0: 
                return
            case _: 
                print("Pls pick a valid number")


def show_call_cost_menu():
    while True:
        print("""
            SHOW CALL COST

            1 -> Last call cost
            2 -> All calls' cost
            3 -> Clear counters
            0 -> Back
        """)

        show_call_cost_options = int(input("Enter option: "))
        match show_call_cost_options:
            case 1: 
                print("Last call cost")    
            case 2: 
                print("All calls' cost")
            case 3: 
                print("Clear counters")
            case 0: 
                return
            case _: 
                print("Pls pick a valid number")




def clear_counters_menu():
    while True:
        print("""
            CLEAR COUNTERS

            1 -> Clear call timers
            2 -> Clear call costs
            0 -> Back
        """)

        clear_counters_options = int(input("Enter option: "))
        match clear_counters_options:
            case 1: 
                print("Clear call timers")    
            case 2: 
                print("Clear call costs")
            case 0: 
                return
            case _: 
                print("Pls pick a valid number")





def tones_menu():
    while True:
        print("""
            TONES

            1 -> Ringing tone
            2 -> Ringing volume
            3 -> Incoming call alert 
            4 -> Composer
            5 -> Message alert tone
            6 -> Keypad tones
            7 -> Warning and game tones
            8 -> Vibrating alert
            9 -> Screen saver
            0 -> Main menu
        """)

        tones_options = int(input("Enter option: "))
        match tones_options:
            case 1:
                print("Ringing tone...")
            case 2:
                print("Ringing volume...")
            case 3:
                print("Incoming call alert...")
            case 4:
                print("Composer...")
            case 5:
                print("Message alert tone...")
            case 6:
                print("Keypad tones...")
            case 7:
                print("Warning and game tones...")
            case 8:
                print("Vibrating alert...")
            case 9:
                print("Screen saver...")
            case 0:
                return
            case _: 
                print("Pls pick a valid number")


def settings_menu():
    while True:
        print("""
            SETTINGS

            1 -> Call settings
            2 -> Phone settings
            3 -> Security settings
            4 -> Restore factory settings
            0 -> Main menu
        """)
        
        settings_options = int(input("Select an option: "))

        match settings_options:
            case 1:
                call_settings_menu()
            case 2:
                phone_settings_menu()
            case 3:
                security_settings_menu()
            case 4:
                print("Restore factory settings...")
            case 0:
                return
            case _:
                print("Pls pick a valid number")


def call_settings_menu():
    while True:
        print("""
            CALL SETTINGS

            1 -> Automatic redial
            2 -> Speed dialing
            3 -> Call waiting service
            4 -> Own number sending
            5 -> Phone line in use
            6 -> Automatic answer
            0 -> Back
        """)

        call_settings_options = int(input("Select an option: "))

        match call_settings_options:
            case 1:
                print("Automatic redial...")
            case 2:
                print("Speed dialing...")
            case 3:
                print("Call waiting service...")
            case 4:
                print("Own number sending...")
            case 5:
                print("Phone line in use...")
            case 6:
                print("Automatic answer...")
            case 0:
                return
            case _:
                print("Pls pick a valid number")





def phone_settings_menu():
    while True:
        print("""
            PHONE SETTINGS

            1 -> Language
            2 -> Cell info display
            3 -> Welcome note
            4 -> Network selection
            5 -> Lights
            6 -> Confirm SIM service actions
            0 -> Back
        """)

        phone_settings_options = int(input("Select an option: "))

        match phone_settings_options:
            case 1:
                print("Language...")
            case 2:
                print("Cell info display...")
            case 3:
                print("Welcome note...")
            case 4:
                print("Network selection...")
            case 5:
                print("Lights...")
            case 6:
                print("Confirm SIM service actions...")
            case 0:
                return
            case _:
                print("Pls pick a valid number")


def security_settings_menu():
    while True:
        print("""
            SECURITY SETTINGS

            1 -> PIN code request
            2 -> Call barring service
            3 -> Fixed dialing
            4 -> Closed user group
            5 -> Security level
            6 -> Change access codes
            0 -> Back
        """)

        security_settings_options = int(input("Select an option: "))

        match security_settings_options:
            case 1:
                print("PIN code request...")
            case 2:
                print("Call barring service...")
            case 3:
                print("Fixed dialing...")
            case 4:
                print("Closed user group...")
            case 5:
                print("Security level...")
            case 6:
                print("Change access codes...")
            case 0:
                return
            case _:
                print("Pls pick a valid number")


def call_divert_menu():
    while True:
        print("""
            CALL DIVERT
            0 -> Back
        """)

        call_divert_options = int(input("Select an option: "))

        match call_divert_options:
        
            case 0:
                return
            case _:
                print("Pls pick a valid number")

# Games sections menu
def games_sections_menu():
    while True:
        print("""
            GAMES SECTIONS

            1 -> Snake
            2 -> Space Impact
            3 -> Pairs II
            0 -> Back
        """)

        games_sections_options = int(input("Select an option: "))

        match games_sections_options:
            case 1:
                print("Snake...")
            case 2:
                print("Space Impact...")
            case 3:
                print("Pairs II...")
            case 0:
                return
            case _:
                print("Pls pick a valid number")

# Calculator menu
def calculator_menu():
    while True:
        print("""
            CALCULATOR

            1 -> Add
            2 -> Subtract
            3 -> Multiply
            4 -> Divide
            0 -> Back
        """)

        calculator_options = int(input("Select an option: "))

        match calculator_options:
            case 1:
                print("Add...")
            case 2:
                print("Subtract...")
            case 3:
                print("Multiply...")
            case 4:
                print("Divide...")
            case 0:
                return
            case _:
                print("Pls pick a valid number")


def reminders_menu():
    while True:
        print("""
            REMINDERS

            0 -> Back
        """)

        reminders_options = int(input("Select an option: "))

        match reminders_options:
         
            case 0:
                return
            case _:
                print("Pls pick a valid number")



def clock_menu():
    while True:
        print("""
            CLOCK

            1 -> Alarm clock
            2 -> Clock settings
            3 -> Date setting
            4 -> Stopwatch
            5 -> Countdown timer
            6 -> Auto update of date and time
            0 -> Back
        """)

        clock_options = int(input("Select an option: "))

        match clock_options:
            case 1:
                print("Alarm clock...")
            case 2:
                print("Clock settings...")
            case 3:
                print("Date setting...")
            case 4:
                print("Stopwatch...")
            case 5:
                print("Countdown timer...")
            case 6:
                print("Auto update of date and time...")
            case 0:
                return
            case _:
                print("Pls pick a valid number")


def profiles_menu():
    while True:
        print("""
            PROFILES
        """)

       

def sim_services_menu():
    while True:
        print("""
            SIM SERVICES

                    """)

        sim_services_options = int(input("Select an option: "))


nokia()