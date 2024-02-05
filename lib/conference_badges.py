def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges =[]
    for name in names:
        badge_message = badge_maker(name)
        badges.append(badge_message)
    return badges

def assign_rooms(names):
    rooms = range(1, 8)
    room_assignment = []

    for i, speaker in enumerate(names):
        room_number = rooms[i]
        assignment_message = f"Hello, {speaker}! You'll be assigned to room {room_number}!"
        room_assignment.append(assignment_message)
    return room_assignment

def printer(names):
    badges = batch_badge_creator(speakers)
    room_assignment = assign_rooms(speakers)

    print("Printing Badges:")
    for badge in badges:
        print(badge)

    print("\nPrinting Room Assignments:") 
    for assignment in room_assignment:
        print(assignment)   
    
