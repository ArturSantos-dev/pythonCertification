from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass
    
    @abstractmethod
    def get_scanner_status(self):
        pass

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass
    
    @abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Scanner, Printer):
    def scan_document(self):
        return "MFD1: Document scanned at low resolution."

    def get_scanner_status(self):
        return "MFD1: Scanner status - Max Resolution: 300dpi, Serial Number: 12345-Low"

    def print_document(self):
        return "MFD1: Document printed at low resolution."

    def get_printer_status(self):
        return "MFD1: Printer status - Max Resolution: 300dpi, Serial Number: 67890-Low"


class MFD2(Scanner, Printer):
    def __init__(self):
        self.history = []

    def scan_document(self):
        result = "MFD2: Document scanned at medium resolution."
        self.history.append(result)
        return result

    def get_scanner_status(self):
        return "MFD2: Scanner status - Max Resolution: 600dpi, Serial Number: 54321-Medium"

    def print_document(self):
        result = "MFD2: Document printed at medium resolution."
        self.history.append(result)
        return result

    def get_printer_status(self):
        return "MFD2: Printer status - Max Resolution: 600dpi, Serial Number: 09876-Medium"

    def print_operation_history(self):
        return "\n".join(self.history)


class MFD3(Scanner, Printer):
    def __init__(self):
        self.history = []

    def scan_document(self):
        result = "MFD3: Document scanned at high resolution."
        self.history.append(result)
        return result

    def get_scanner_status(self):
        return "MFD3: Scanner status - Max Resolution: 1200dpi, Serial Number: 11111-High"

    def print_document(self):
        result = "MFD3: Document printed at high resolution."
        self.history.append(result)
        return result

    def get_printer_status(self):
        return "MFD3: Printer status - Max Resolution: 1200dpi, Serial Number: 22222-High"

    def print_operation_history(self):
        return "\n".join(self.history)

    def send_fax(self, fax_number, document):
        return f"MFD3: Sending fax to {fax_number} - {document}"

def main():
    mfd1 = MFD1()
    mfd2 = MFD2()
    mfd3 = MFD3()

    print(mfd1.scan_document())
    print(mfd1.get_scanner_status())
    print(mfd1.print_document())
    print(mfd1.get_printer_status())

    print(mfd2.scan_document())
    print(mfd2.get_scanner_status())
    print(mfd2.print_document())
    print(mfd2.get_printer_status())
    print(mfd2.print_operation_history())

    print(mfd3.scan_document())
    print(mfd3.get_scanner_status())
    print(mfd3.print_document())
    print(mfd3.get_printer_status())
    print(mfd3.print_operation_history())
    print(mfd3.send_fax("123456789", "Important Document"))

if __name__ == "__main__":
    main()
