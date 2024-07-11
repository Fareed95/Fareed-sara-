import os
from text_remover import text_remover_mummy


def file_saver(directory,file_name,command):
    
    try:
        # Specify the directory and file name
        # directory = r'C:\Users\Admin\OneDrive - RizviCollegeOfEngineering\Documents\Saara documents'
        # file_name = 'example.txt'
        file_path = os.path.join(directory, file_name)

        # Text to append
        # text_to_append = text_remover_mummy(command)

        # Open the file in append mode and write the text
        with open(file_path, 'a') as file:
            file.write(f"* {command} \n")

        print(f"Text appended to {file_path}")
    except Exception as e :
        print(e)


def file_saver_bot(question,answer):
    try:
        # Specify the directory and file name
        directory = r'C:\Users\Admin\OneDrive - RizviCollegeOfEngineering\Documents\Saara documents'
        file_name = 'bot.txt'
        file_path = os.path.join(directory, file_name)

        # Text to append
        # text_to_append = text_remover_mummy(command)

        # Open the file in append mode and write the text
        with open(file_path, 'a') as file:
            file.write(
                f"Q.{question.capitalize()}\n----> {answer.capitalize()}\n\n"
            )

        print(f"Text appended to {file_path}")
    except Exception as e :
        print(e)

if __name__ == "__main__":
    # file_saver(r'C:\Users\Admin\OneDrive - RizviCollegeOfEngineering\Documents\Saara documents','exa.txt',"please note bring onions for mummy")
    file_saver_bot("what is waer","water is paani")