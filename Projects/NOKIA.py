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
                call_Register_menu()
            case 5:
                tones_menu()
            case 6:
                settings_menu()
            case 7:
                call_divert_menu()
            case 8:
                games_Sections_menu()
            case 9:
                calculator_menu()
            case 10:
                reminders_menu()
            case 11:
                clock_menu()
            case 12:
                profiles_menu()
            case 13:
                sim_service_menu()
            case 0:
                print("NOKIA....CONNECTING PEOPLE")
                break
            case _:
                print("Wrong input")
                nokia()

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
                nokia()
            case _:
                print("Wrong input")
                phonebook_menu()

def options_menu() :
    while True:
        print("""
        Options

        1 -> Type of view
        2 -> Memory status
        0 -> Main menu
        """)

        options_input = int(input("Select a option: "))

        match options_input:
            case 1:
                print("Type of view")
            case 2:
                print("Memory status")
            case 0:
                nokia()  
            case _:
                print("Wrong input.")
                nokia()

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

        message_options = int(input("Select option:"))

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
                print("""
                1 -> Set 1
                2 -> Common
                0 -> Back 
                """)

                case7_option = int(input("Select option: "))
                match case7_option:
                    case 1:
                        print("""
                        1 -> Message center number
                        2 -> Message sent as
                        3 -> Message validity
                        0 -> Back 
                        """)
                        set1_options = int(input("Select option"))
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
                                print("Wrong input")
                                break
                    case 2:
                        print("""
                        	1 -> Message center number
                        	2 -> Message sent as
                        	3 -> Message validity
                        	0 -> Back 
                        	""")
                        common_options = int(input("Select option"))
                        match common_options:
                            case 1:
                                print("Message center number")
                            case 2:
                                print("Message sent as")
                            case 3:
                                print("Message validity")
                            case 0:
                                return
                            case _:
                                print("Wrong input")
                                break
            case 8:
                print("Info service")
            case 9:
                print("Voice mailbox number")  
            case 10:
                print("Service command editor")
            case 0: 
                nokia()
            case _: 
                print("Wrong input")
                messages_menu()

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
                nokia()
            case _: 
                nokia("Pls dont select the chat. They won't chat you back")
		

def call_Register_menu():
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
        call_Register_options = int(input("Enter option: "))
        match call_Register_options:
            case 1: 
                print("Missed calls")    
            case 2: 
                print("Received calls")
            case 3: 
                print("Dialed Numbers")
            case 4: 
                print("Erase recent call lists")    
            case 5: 
                print("""
                Show call duration

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
                        print("Wrong input")
            case 0:
                nokia()
            case _: 
                print("Wrong input")
                call_Register_menu()


nokia()
