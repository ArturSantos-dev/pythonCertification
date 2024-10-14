class FileError(Exception):
    """Base class for exceptions in this module."""
    pass

class BadLineError(FileError):
    """Exception raised for errors in the input line format."""
    def __init__(self, line):
        self.line = line
        self.message = f"Bad line format: {line}"
        super().__init__(self.message)

class EmptyFileError(FileError):
    """Exception raised when the file is empty."""
    def __init__(self, file_name):
        self.file_name = file_name
        self.message = f"The file {file_name} is empty."
        super().__init__(self.message)

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise EmptyFileError(file_name)
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
        return None
    except EmptyFileError as e:
        print(e)
        return None

    student_points = {}
    for line in lines:
        try:
            parts = line.strip().split()
            if len(parts) != 3:
                raise BadLineError(line)
            
            first_name, last_name, points = parts
            points = float(points)
            student_name = f"{first_name} {last_name}"

            if student_name in student_points:
                student_points[student_name] += points
            else:
                student_points[student_name] = points
        except ValueError:
            raise BadLineError(line)
        except BadLineError as e:
            print(e)
            return None

    return student_points

def print_report(student_points):
    for student, points in sorted(student_points.items()):
        print(f"{student}\t {points:.1f}")

if __name__ == "__main__":
    file_name = input("Enter the name of the file: ")
    student_points = read_file(file_name)
    if student_points:
        print_report(student_points)
