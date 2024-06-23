import shutil
import os


class Genarational_datasets():
    def __init__(self, dataset_name: str, extension: str = "log", number_of_generations: int = 3):
        self.dataset_name = dataset_name
        self.number_of_generations = number_of_generations
        self.extension = extension
        # Validate and default data
        if not isinstance(self.number_of_generations, int):
            print('WARNING: Number of generations must be an integer. Defaulting to 3')
            self.number_of_generations = 3
        if self.number_of_generations < 2 or self.number_of_generations > 999:
            print('WARNING: Number of generations must be between 2 and 999. Defaulting to 3')
            self.number_of_generations = 3
        if not isinstance(dataset_name, str):
            raise TypeError('dataset_name must be a string.')
        if not isinstance(extension, str):
            print('Extension must be a string. Defaulting to "log"')
            self.extension = 'log'

        # Set up initial file_set
        for generation_num in range(self.number_of_generations):
            generation_indicator = self.return_two_digit_number(generation_num)
            filename = dataset_name + '_V' + generation_indicator + '.' + self.extension
            # Create empty file
            with open(filename, mode='w') as file:
                pass

    def create_new_generation(self, contents: str = ""):
        if not isinstance(contents, str):
            print('WARNING: contents must be a string. Defaulting to empty string')
            contents = ""
        self.roll_files()
        filename = self.dataset_name + '_V' + '00' + '.' + self.extension
        with open(filename, mode='w') as file:
            file.write(contents)


    def roll_files(self):
        for generation_number in range(self.number_of_generations - 1):
            generation_to_copy_from = self.return_two_digit_number(generation_number)
            generation_to_copy_to = self.return_two_digit_number(generation_number + 1)
            filename_to_copy_from = self.dataset_name + '_V' + generation_to_copy_from + '.' + self.extension
            filename_to_copy_to = self.dataset_name + '_V' + generation_to_copy_to + '.' + self.extension
            shutil.copy(filename_to_copy_from, filename_to_copy_to)
            filename_to_remove = self.dataset_name + '_V' + '00' + '.' + self.extension
            try:
                os.remove(filename_to_remove)
            except FileNotFoundError:
                pass

    def return_two_digit_number(self, number: int) -> str:
        if not isinstance(number, int):
            raise TypeError('number to be converted to 3 digits must be an integer.')
        if number < 10:
            return '0' + str(number)
        return str(number)


# Quick tests
if __name__ == '__main__':
    my_gdg = Genarational_datasets("test_gdg", 3)
    assert my_gdg.return_two_digit_number(3) == "03"
    assert my_gdg.return_two_digit_number(0) == "00"
    assert my_gdg.return_two_digit_number(12) == "12"
    assert my_gdg.return_two_digit_number(14) == "14"
    assert my_gdg.return_two_digit_number(99) == "99"
    my_gdg.create_new_generation("First thing I wrote")
    my_gdg.create_new_generation("2nd thing I wrote")
    my_gdg.create_new_generation("3rd thing I wrote")
    my_gdg.create_new_generation("4th thing I wrote")

