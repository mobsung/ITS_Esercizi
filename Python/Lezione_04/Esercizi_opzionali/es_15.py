'''
15. Text Editor with Basic Functionality:

    Create a simple text editor that allows the user to open, edit, and save text files.
    Implement basic functionality such as inserting, deleting, and copying text.
    Provide undo/redo functionality to allow users to reverse actions.
    Save the edited text to a file when the user chooses to save.
'''

'''
1 - 
'''

def initialInterface() -> str:

    choice:str = input('Type "open"   -> if you want to open an existing file\n'
                       'Type "new"    -> if you want to create a new file\n'
                       'Type "remove" -> if you want to remove an existing file\n')
    
    return choice


def Open(file_container:dict[str, str]):

    choose_file:str = ("")
    

def numFile(file_container:dict[str, str]):

    numerated_file_container:dict[int, tuple[str,str]] = {}

    for file_name, file_content in file_container:
        pass


def fileManager(file_name:str, file_content:str) -> dict[str, str]:

    file_container:dict[str, str] = {}

    file_container[file_name] = file_content

    return file_container


def pickFile(file_container:dict[str, str]):

    file:tuple[str, str] = ()


