from string_utils import StringUtils

string_utils = StringUtils()

# Позитивные сценарии

def test_capitalize():
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("hello world") == "Hello world"
    

def test_trim():
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("testing") == "testing"

def test_to_list():
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    

def test_contains():
    assert string_utils.contains("SkyPro", "S") == True
    assert string_utils.contains("SkyPro", "U") == False
    
def test_delete_symbol():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    
def test_starts_with():
    assert string_utils.starts_with("SkyPro", "S") == True
    assert string_utils.starts_with("SkyPro", "P") == False
    

def test_end_with():
    assert string_utils.end_with("SkyPro", "o") == True
    assert string_utils.end_with("SkyPro", "y") == False
    

def test_is_empty():
    assert string_utils.is_empty("") == True
    assert string_utils.is_empty("SkyPro") == False

def test_list_to_string():
    assert string_utils.list_to_string([1,2,3,4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    


# Негативные сценарии

def test_capitalize_negative():
    assert string_utils.capitilize("") == ""  # Пустая строка

def test_trim_negative():
    assert string_utils.trim(" ") == ""  # Строка с пробелом
    assert string_utils.trim("") == ""  # Пустая строка

def test_to_list_negative():
    assert string_utils.to_list("") == []  # Пустая строка
    assert string_utils.to_list(" ") == [" "]  # Строка с пробелом

def test_contains_negative():
    assert string_utils.contains("", "a") == False  # Пустая строка
    assert string_utils.contains("  ", " ") == True  # Строка с пробелом

def test_delete_symbol_negative():
    assert string_utils.delete_symbol("", "a") == ""  # Пустая строка
    assert string_utils.delete_symbol("   ", " ") == ""  # Строка с пробелами

def test_starts_with_negative():
    assert string_utils.starts_with("", "a") == False  # Пустая строка
    assert string_utils.starts_with("   ", " ") == True  # Строка с пробелами

def test_end_with_negative():
    assert string_utils.end_with("", "a") == False  # Пустая строка
    assert string_utils.end_with(" ", " ") == True  # Строка с пробелом

def test_is_empty_negative():
    assert string_utils.is_empty("a") == False  # Не пустая строка
    assert string_utils.is_empty("  ") == True  # Строка с пробелами

def test_list_to_string_negative():
    assert string_utils.list_to_string([]) == ""  # Пустой список
    assert string_utils.list_to_string([" "]) == " "  # Список с пробелом
