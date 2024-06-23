import os
import logging


def get_project_root(project_name: str) -> str:
    """
    Get the path of the project root, to use in relative path processing
    :param project_name: Name of the current project
    :return: Project root path
    :rtype: str
    """
    # Create a list of the path nodes i the current working directory
    full_path_list: list[str] = os.getcwd().split(os.sep)
    # Get all the path nodes from the list up to the project path, and join is by the os. sep
    # (probably \ or / depending on whether you are running on Unix or Windows)
    try:
        return os.sep.join(os.getcwd().split(os.sep)[:full_path_list.index(project_name) + 1:])
    except ValueError:
        err_mess: str = "Incorrect project name sent to get_project_root function. "
<<<<<<< HEAD
        err_mess += f"Argument given was {project_name}. Returning curren path"
        # Since in this project, the logger uses this function as setup, the assumption is that I should print this
        # warning to standard output, instead of logging it out
        print(err_mess)
        # Return full current path - di not fail entire process for this error
        return os.getcwd()

# Testing Note: I did not build automated tests for this function because the output depends on where you store your
# project code so it would need to be customized for your instance of this project. So - proceed with caution
# using this code :)
=======
        err_mess += f"Argument given was {project_name}"
        logging.error(err_mess)
        raise ValueError(err_mess)


if __name__ == '__main__':
    print(get_project_root("find-best-matchy"))
>>>>>>> 759315e0a0538a0f4960231f1ed679af2ee5c20a
