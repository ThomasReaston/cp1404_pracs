"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    """Get score fron user"""
    score = float(input("Please Enter Score: "))

    """Check if valid between 1-100"""
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        if score > 50:
            print("Passable")
        if score > 90:
            print("Excellent")
        if score < 50:
            print("Bad")

"""Give feedback based on score given"""

main()

"""Fixed incorrect indenting"""
