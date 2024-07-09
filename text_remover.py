import re


def text_remover_mummy(command):
    try :

        # Compile the regular expression pattern to match the new conditions
        pattern = re.compile(r'(?:(?:please\s+)?note\s+)(.*)\s+(?:for|said\s+by|order\s+by)\s+mummy')

        # Prompt the user to enter a string
        # user_input = input("Enter a string that starts with 'note' or 'please note' and ends with 'for mummy', 'said by mummy', or 'order by mummy': ")

        # Search for the pattern in the user input
        match = pattern.search(command)

        # Extract and print the desired part
        if match:
            return match.group(1).strip()
            # print(match.group(1).strip())
        else:
            print("No match found. Make sure the input starts with 'note' or 'please note' and ends with 'for mummy', 'said by mummy', or 'order by mummy'.")
    except Exception as e :
        print(e)



def text_remover(command):
    try :

        # Compile the regular expression pattern to match the new conditions
        pattern = re.compile(r'(?:(?:please\s+)?note\s+)(.*)')

        # Prompt the user to enter a string
        # user_input = input("Enter a string that starts with 'note' or 'please note' and ends with 'for mummy', 'said by mummy', or 'order by mummy': ")

        # Search for the pattern in the user input
        match = pattern.search(command)

        # Extract and print the desired part
        if match:
            return match.group(1).strip()
            # print(match.group(1).strip())
        else:
            print("No match found. Make sure the input starts with 'note' or 'please note'")
    except Exception as e :
        print(e)


def text_remover_search(command):
    try :

        # Compile the regular expression pattern to match the new conditions
        pattern = re.compile(r'(?:(?:search\s+)?(?:for|in\s+youtube\s+for\s+)?)(.*)')

        # Prompt the user to enter a string
        # user_input = input("Enter a string that starts with 'note' or 'please note' and ends with 'for mummy', 'said by mummy', or 'order by mummy': ")

        # Search for the pattern in the user input
        match = pattern.search(command)

        # Extract and print the desired part
        if match:
            return match.group(1).strip()
            # print(match.group(1).strip())
        else:
            print("No match found. Make sure the input starts with 'note' or 'please note'")
    except Exception as e :
        print(e)

if __name__ == "__main__":
    print(text_remover_mummy("please note to bring 10kg onion for mummy"))
    print(text_remover("please note to water my plants for ever"))
    print(text_remover_youtube("search kurulus osman season 5"))