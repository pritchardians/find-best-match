import os


def get_project_root(project_name: str) -> str:
    """
    Get the path of the project root, to use in relative path processing
    :param project_name: Name of the current project
    :return: Project root path
    :rtype: str
    """
    # Create a list of the path nodes i the current working directory
    full_path_list: list[str] = os.getcwd().split(os.sep)
    # Get all the path nodes from the list up to the project path,
    # and join is by the os. sep
    # (probably \ or / depending on whether you are running on Unix or Windows)
    try:
        return os.sep.join(os.getcwd().split(os.sep)[:full_path_list.index(project_name) + 1:])
    except ValueError:
        err_mess: str = "Incorrect project name sent to get_project_root function. "
        err_mess += f"Argument given was {project_name}. Returning current path"
        # Since in this project, the logger uses this function as setup, the assumption is that I should print this
        # warning to standard output, instead of logging it out
        print(err_mess)
        # Return full current path - do not fail entire process for this error
        return os.getcwd()

# TESTING NOTE: Note tested because the output depends on the directory path,
# which changes between developers
