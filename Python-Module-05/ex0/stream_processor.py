#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  stream_processor.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 13:18:39 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/11 14:34:44 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    This class represents an interface that can implemented to represent
    various processor types. It provides 3 different methods to be overwritten.
    """
    @abstractmethod
    def process(self, data: Any) -> str:
        """
        This function processes data. The meaning of process
        depends on the type of processor.

        Args:
            data (Any): A valid data linked to the processor.

        Returns:
            str: A succes message on process.
        """
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        This function checks if a data is valid.

        Args:
            data (Any): The data to be checked.

        Returns:
            bool: True if the data is valid, False otherwise.
            The meaning of valid depends on the type of
            processor.
        """
        ...

    def format_output(self, result: str) -> str:
        """
        This function provides a format for the different
        outputs ommited by the processors.

        Args:
            result (str): The result of the process.

        Returns:
            str: A string of the form: 'Output: -result-'.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    This class represents a special type of processor 'NumericProcessor'
    that accepts lists of numbers.
    """
    def __init__(self) -> None:
        """
        This function initializes the state of the current
        class according to it's super class.
        """
        super().__init__()
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        """
        This function processes a list of numbers by performing
        operations on them. It calculates the sum and the average
        of the numbers.

        Args:
            data (Any): The list of numbers.

        Returns:
            str: A string mentioning the sum and the average.
        """
        try:
            data_sum: int = 0
            for num in data:
                data_sum += int(num)
            if len(data) > 0:
                avg: float = data_sum / len(data)
            else:
                avg: int = 0
            return f"Processed {len(data)} numeric values, \
sum={data_sum}, avg={avg}"
        except (ValueError, TypeError):
            return "Invalid numeric data"

    def validate(self, data: Any) -> bool:
        """
        This function validates the data given by checking
        if every element is a number.

        Args:
            data (Any): The data to be checked.

        Returns:
            bool: True if all of the elements are numbers,
            False otherwise.
        """
        try:
            for num in data:
                int(num)
            return True
        except (ValueError, TypeError):
            return False


class TextProcessor(DataProcessor):
    """
    This class represents a special type of processor 'TextProcessor'
    that accepts strings.
    """
    def __init__(self) -> None:
        """
        This function initializes the state of the current
        class according to it's super class.
        """
        super().__init__()
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        """
        This function processes a string by performing
        operations on it. It calculates the number of characters
        and the number of words.

        Args:
            data (Any): The string to be processed.

        Returns:
            str: A string mentioning the number of characters
            and the number of words.
        """
        data: str = str(data)
        words: int = len(data.split(" "))
        return f"Processed text: {len(data)} characters, \
{words} words"

    def validate(self, data: Any) -> bool:
        """
        This function validates the data given by checking
        if it is or can be transformed to a string.

        Args:
            data (Any): The data to be checked.

        Returns:
            bool: True if the data is or can be transformed to
            a string, False otherwise.
        """
        try:
            str(data)
            return True
        except ValueError:
            return False


class LogProcessor(DataProcessor):
    """
    This class represents a special type of processor 'LogProcessor'
    that accepts logs. Logs are special types of string mentioning the
    meaning of the alert.
    """
    def __init__(self) -> None:
        """
        This function initializes the state of the current
        class according to it's super class.
        """
        super().__init__()
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        """
        This function processes a log message by performing
        operations on it. It creates a message mentioning the log
        type and the message.

        Args:
            data (Any): The log message to be processed.

        Returns:
            str: A string mentioning the log type and the
            log message.
        """
        elements: List[str] = data.split(":")
        if len(elements) >= 2:
            if elements[0] == "ERROR":
                return f"[ALERT] ERROR level detected: {elements[1].strip()}"
            elif elements[0] == "INFO":
                return f"[INFO] INFO level detected: {elements[1].strip()}"
        return ""

    def validate(self, data: Any) -> bool:
        """
        This function validates the data given by checking
        if it respects the form of a log message.

        Args:
            data (Any): The data to be checked.

        Returns:
            bool: True if the data has the form of a log message,
            False otherwise.
        """
        try:
            elements: List[str] = str(data).split(":")
            if elements[0] != "ERROR" and elements[0] != "INFO":
                return False
            return True
        except (ValueError, TypeError):
            return False


def main() -> None:
    """
    Main function that initializes objects and
    runs the required tests.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    np = NumericProcessor()
    valid_data = [1, 2, 3, 4, 5]
    invalid_data = [1, 2, "a"]
    print(f"Processing data: {valid_data}")
    validation = np.validate(valid_data)
    if validation:
        print("Validation: Numeric data verified")
        print(np.format_output(np.process(valid_data)))
        print("")
    print(f"Processing data: {invalid_data}")
    validation = np.validate(invalid_data)
    if not validation:
        print("Validation: Numeric data not verified\n")

    tp = TextProcessor()
    data = "Hello Nexus World"
    print(f'Processing data: {data}')
    validation = tp.validate(data)
    if validation:
        print("Validation: Text data verified")
        print(tp.format_output(tp.process(data)))
        print("")

    lp = LogProcessor()
    data = "ERROR: Connection timeout"
    print(f"Processing data: {data}")
    validation = lp.validate(data)
    if validation:
        print("Validation: Log entry verified")
        print(lp.format_output(lp.process(data)))
        print("")

    print("=== Polymorphic Processing Demo ===\n")

    print("Processing multiple data types through same interface")
    print(np.format_output(np.process([1, 2, 3])))
    print(tp.format_output(tp.process("Hello world!")))
    print(lp.format_output(lp.process("INFO: System ready")))


if __name__ == "__main__":
    main()
