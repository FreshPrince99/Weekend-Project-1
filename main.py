from openai import OpenAI
import subprocess
import os
import sys

client = OpenAI(
         api_key=os.environ.get("OPENAI_API_KEY"),
     )

def main():
    print("Choose a chef personality:")
    print("1. Knowledgable and experienced Indian chef who lives in the coastal area and loves making seafood")
    print("2. Famous chef in Italy who specialises in making pasta and has vast knowledge about the Italian cuisine")
    print("3. Kind Japanese chef who specialises in making the best Japanese dishes and also has a soft spot for Ramen ;)")
    print("4. Fun and energetic Mexican chef who owns a large chain of restraunts across the world spreading his famous Mexican recipes")
    # Add additional options for other group members
    choice = input("Enter the number of your choice: ")

    script_mapping = {
        "1": "chef_a.py",
        "2": "chef_b.py",
        "3": "chef_c.py",
        "4": "chef_d.py",
        # Add additional mappings for other group members
    }

    script_to_run = script_mapping.get(choice)
    python_executable = sys.executable
    if script_to_run:
        subprocess.run([python_executable, script_to_run])
    else:
        print("Invalid choice. Please run the script again and choose a valid option.")

if __name__ == "__main__":
    main()