from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            sum(data)
            print("Validation: Numeric data verified")
            return True
        except (ValueError, TypeError):
            return False

    def process(self, data: Any) -> str:
        try:
            total = sum(data)
            avg = total / len(data)
            return (f"Processed {len(data)} numeric values, sum={total},"
                    f" avg={avg}")
        except ZeroDivisionError:
            return "Error: Division by zero (empty collection)"
        except Exception as e:
            return f"[ALERT] NumericProcessor ERROR detected: {e}"

    def format_output(self, result: str) -> str:
        return f"Output: {super().format_output(result)}\n"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data.lower()
            print("Validation: Text data verified")
            return True
        except (ValueError, TypeError, AttributeError):
            return False

    def process(self, data: Any) -> str:
        try:
            taille_chaine: int = len(data)
            tab: List = data.split()
            taille_tab: int = len(tab)
            return (f"Processed text: {taille_chaine} characters, {taille_tab}"
                    f" words")
        except (AttributeError, ValueError, TypeError) as e:
            return f"[ALERT] TextProcessor ERROR detected: {e}"

    def format_output(self, result: str) -> str:
        return f"Output: {super().format_output(result)}\n"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            str_log: List = data.split(':', 1)
            if (str_log[0] == "ERROR" or str_log[0] == "INFO") and str_log[1]:
                print("Validation: Log entry verified")
                return True
            return False
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            log_data: Dict[str, str] = {}
            parts: List[str] = data.split(':', 1)
            log_data["level"] = parts[0]
            log_data["message"] = parts[1]
            prefix: Optional[str] = ""
            if log_data["level"] == "ERROR":
                prefix = "[ALERT]"
            elif log_data["level"] == "INFO":
                prefix = "[INFO]"
            else:
                log_data = None
            if len(parts[1]) <= 0:
                log_data = None
            return (f"{prefix} {log_data['level']} level detected: "
                    f"{log_data['message']}")
        except Exception as e:
            return f"[ALERT] LogProcessor ERROR detected: {e}"

    def format_output(self, result: str) -> str:
        return f"Output: {super().format_output(result)}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("Initializing Numeric Processor...")
    polo: Any = NumericProcessor()
    data: List = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    polo.validate(data)
    print(polo.format_output(polo.process(data)))
    sisi = TextProcessor()
    s: str = 123
    print("Initializing Text Processor...")
    print(f"Processing data: {s}")
    sisi.validate(s)
    print(sisi.format_output(sisi.process(s)))
    my_list: List[str, int, str]
    print("Initializing Log Processor...")
    haha = LogProcessor()
    bb: str = "ERROR: "
    print(f"Processing data: {bb}")
    haha.validate(bb)
    print(haha.format_output(haha.process(bb)))