def main():
    print("This is my main function running!")

if __name__ == "__main__":
    main()                      # runs only when you run this file directly
    print("This extra code runs only in myscript.py")

# every .py file is a "module". You can import modules (files) to resue their functions
# A file can also be run as a script (from the command line). Same file, two roles.

# Python gives every module a built-in variable __name__
# If you run the file directly, __name__ is "__main__"
# If you import the file, __name__ is the module’s name (e.g., "myscript")

# myscript.py defines a function and a guarded “entry point.” It prints from main()
# and also prints an extra line—but only when the file is run directly

# def main(): ... creates a callable function you can import elsewhere
# The if __name__ == "__main__": ... block runs only when you do python myscript.py,
# not when another file imports it

# otherscript.py imports myscript and then decides what to do: it prints its own line
# and explicitly calls myscript.main(). Because of the guard in myscript.py,
# the “extra code” in myscript.py does not auto-run on import.