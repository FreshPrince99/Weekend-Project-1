from openai import OpenAI
import subprocess

def main():
    print("Choose a chef personality:")
    print("1. Young and spirited Thai Jamaican chef that loves to incorporate flavours from these cultures into fusion food, creating new and novel recipes")
    print("2. Wise and experienced Italian chef that loves to make pasta")
    print("3. Focused and detailist vegan French chef")
    print("4. Fun and energetic Mexican chef that loves spicy food")
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
    if script_to_run:
        subprocess.run(["python", script_to_run])
    else:
        print("Invalid choice. Please run the script again and choose a valid option.")

if __name__ == "__main__":
    main()