# Write your solution here
editor = ""
while editor.lower() != "visual studio code":
    editor = input("Editor: ")
    if "visual studio code" == editor.lower():
        print("an excellent choice!")
    elif "word" == editor.lower() or "notepad" == editor.lower():
        print("awful")
    else:
        print("not good")