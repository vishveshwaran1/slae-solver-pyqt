
from operator import contains
from PyQt6 import QtWidgets
from PyQt6.QtCore import QCoreApplication
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QBoxLayout, QDoubleSpinBox, QFileDialog, QGridLayout, QLabel, QMessageBox, QPushButton, QMainWindow, QSizePolicy, QWidget

import numpy as np


def add_or_replace(matrix, index, value):
    if index[0] < matrix.shape[0] and index[1] < matrix.shape[1]:
        # Заменяем значение, если индекс в пределах матрицы
        matrix[index] = value
    else:
        # Добавляем значение, если индекс выходит за пределы матрицы
        new_shape = (max(index[0] + 1, matrix.shape[0]), max(index[1] + 1, matrix.shape[1]))
        new_matrix = np.zeros(new_shape)
        new_matrix[:matrix.shape[0], :matrix.shape[1]] = matrix
        new_matrix[index] = value
        matrix = new_matrix
    return matrix
def subscript(number):
    subscript_map = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(number).translate(subscript_map)

from method_kramera import MethodKramera
from Method_Gausa import GaussElimination
from GaussJordanElimination import GaussJordanElimination



def subscript(number):
    subscript_map = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(number).translate(subscript_map)

def int_to_roman(num):
    roman_dict = {
    50: "L",
    49: "XLIX",
    48: "XLVIII",
    47: "XLVII",
    46: "XLVI",
    45: "XLV",
    44: "XLIV",
    43: "XLIII",
    42: "XLII",
    41: "XLI",
    40: "XL",
    39: "XXXIX",
    38: "XXXVIII",
    37: "XXXVII",
    36: "XXXVI",
    35: "XXXV",
    34: "XXXIV",
    33: "XXXIII",
    32: "XXXII",
    31: "XXXI",
    30: "XXX",
    29: "XXIX",
    28: "XXVIII",
    27: "XXVII",
    26: "XXVI",
    25: "XXV",
    24: "XXIV",
    23: "XXIII",
    22: "XXII",
    21: "XXI",
    20: "XX",
    19: "XIX",
    18: "XVIII",
    17: "XVII",
    16: "XVI",
    15: "XV",
    14: "XIV",
    13: "XIII",
    12: "XII",
    11: "XI",
    10: "X",
    9: "IX",
    8: "VIII",
    7: "VII",
    6: "VI",
    5: "V",
    4: "IV",
    3: "III",
    2: "II",
    1: "I"
}

    return roman_dict[num]


def main():
    try:


        form.Vse_matix = dict()
        form.Vse_svobonie_chleni = dict()
        form.Vse_Otvet = dict()
        
        
        form.nomer_method = "Kramer"
        
        base_razmer = 2 # 2 финальный индекс 2*3
        
        # Оформление Крамера
        form.Vse_horizontalLayout_oformlenie = dict()
        form.Vse_verticalLayout_oformlenie = dict()
        
        form.Vse_verticalLayout_oformlenie[form.nomer_method] = form.verticalLayout_dla_Kramera
        form.Vse_horizontalLayout_oformlenie[form.nomer_method] = form.horizontalLayout_dla_Kramera
        form.create_Kram_Oformlenie_for_ver_and_hor(base_razmer, base_razmer, form.Vse_verticalLayout_oformlenie[form.nomer_method], form.Vse_horizontalLayout_oformlenie[form.nomer_method])
        # Оформление Крамера
        
        form.Vse_gridLayout_for_matrix = dict()
        form.Vse_gridLayout_for_matrix[form.nomer_method] = form.gridLayout_main


        form.Vstavka_elementov_v_gridLayout(base_razmer, form.gridLayout_main)
        form.v_mathrix_and_b(base_razmer, form.nomer_method) #Запоминается начальная матрица
        

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        

        
def method_kramera():
    try:
        #метод обновления value матриц для агрументов ниже
        # form.curent_page = 1;
        
        form.Obnovlenie_gridLayout_matrix__svobonie_chleni(int(form.spinBox_RowElem.value()),int(form.spinBox_RowElem.value()), form.gridLayout_main)
        matrix, B = form.Vse_matix[form.nomer_method].tolist(), form.Vse_svobonie_chleni[form.nomer_method].flatten().tolist()
        form.stackedWidget_main.setCurrentIndex(1) # Переключение на страницу с form.listWidget_for_reshenia
        form.listWidget_for_reshenia.clear()
        form.Otvet_Kr = MethodKramera(matrix, B, form.listWidget_for_reshenia)
        form.Vse_Otvet["Kramer"] = form.Otvet_Kr
        form.pushButton_bolshe.setEnabled(True)

        # excel_file = "output.xlsx" 
        # form.Otvet_Kr.save_to_excel(excel_file)
        
    except ValueError as e:
        print(f"Произошла ошибка: {e}")
        form.show_error(f"Произошла ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        form.show_error(f"Произошла ошибка")
        
def Vstavka_elementov_v_gridLayout(razmer, layout):
    print("Vstavka_elementov_v_gridLayout()")
      # gridLayout_main -   крамер
        

    for i in range(razmer):
            for j in range(razmer+1):
                spin_box = QDoubleSpinBox()
                spin_box.setMinimum(-float('inf'))
                layout.addWidget(spin_box, i, j)   

def v_mathrix_and_b(razmer, nomer):
    print("v_mathrix_and_b")
    if nomer == "Kramer":
        form.matrix = np.zeros((razmer, razmer), dtype=float)
        form.svobonie_chleni = np.zeros((razmer, 1), dtype=float)  
        
        form.Vse_matix[nomer] = form.matrix
        form.Vse_svobonie_chleni[nomer] = form.svobonie_chleni
    elif nomer == "Gaus":
        form.matrix_Gausa = np.zeros((razmer, razmer), dtype=float)
        form.svobonie_chleni_Gausa = np.zeros((razmer, 1), dtype=float)
        
        form.Vse_matix[nomer] = form.matrix_Gausa
        form.Vse_svobonie_chleni[nomer] = form.svobonie_chleni_Gausa
        #
        form.Vse_verticalLayout_oformlenie[form.nomer_method] = form.verticalLayout_dla_GaussElimination
        form.Vse_horizontalLayout_oformlenie[form.nomer_method] = form.horizontalLayout_dla_GaussElimination
        
        form.Vse_gridLayout_for_matrix[form.nomer_method] = form.gridLayout_main_for_GaussElimination
    elif nomer == "Gaus_Gordan":
        print("Gaus_Gordan")
        form.matrix_Gaus_Gordan = np.zeros((razmer, razmer), dtype=float)
        form.svobonie_chleni_Gaus_Gordan = np.zeros((razmer, 1), dtype=float)
        
        form.Vse_matix[nomer] = form.matrix_Gaus_Gordan
        form.Vse_svobonie_chleni[nomer] = form.svobonie_chleni_Gaus_Gordan
    
        form.Vse_verticalLayout_oformlenie[form.nomer_method] = form.verticalLayout_dla_GaussJordanElimination
        form.Vse_horizontalLayout_oformlenie[form.nomer_method] = form.horizontalLayout_dla_GaussJordanElimination
        
        form.Vse_gridLayout_for_matrix[form.nomer_method] = form.gridLayout_main_for_GaussJordanElimination
    elif nomer == 3:
        pass
    
def Obnovlenie_gridLayout_matrix__svobonie_chleni(col_row, col_element, layout):
    print("Obnovlenie_gridLayout_matrix__svobonie_chleni")
    print(f"col_row = {col_row}")
    print(f"col_element = {col_element}")
    for row in range(col_row):
        print(f"Svobonie {layout.itemAtPosition(row, col_element).widget().value()}")
        print(f"Из всех свободных {form.nomer_method} = {form.Vse_svobonie_chleni[form.nomer_method]}")
        add_or_replace(form.Vse_svobonie_chleni[form.nomer_method], (row, 0), layout.itemAtPosition(row, col_element).widget().value())

        for element in range(col_element):
            print(f"[row][element] = [{row}][{element}]")
            add_or_replace(form.Vse_matix[form.nomer_method], (row, element), layout.itemAtPosition(row, element).widget().value())

def Obnovlenie_value_matrix__svobonie_chleni(col_row, col_element, layout):
    print("Obnovlenie_value_matrix__svobonie_chleni")
    
    form.Vse_matix[form.nomer_method] = np.zeros((col_row, col_element), dtype=float)
    print(f"form.Vse_matix[form.nomer_method] = {form.Vse_matix[form.nomer_method]}")
    form.Vse_svobonie_chleni[form.nomer_method] = np.zeros((col_row, 1), dtype=float)                      

    row, element = 0, -1
    for i in  range(layout.count()):
        element = element + 1
        child = layout.itemAt(i)
        if child.widget():
            if element == col_element:
                form.Vse_svobonie_chleni[form.nomer_method][row, 0] = child.widget().value()
                print(f"svobonie_chleni [{row}][{element}] = {child.widget().value()}")
                row = row + 1
                element = -1
                continue
                
            print(f"matrix [{row}][{element}] {child.widget().value()}")
            form.Vse_matix[form.nomer_method][row, element] = child.widget().value()
        else:
            print("child.widget() == false")
        
def clear_layout(layout):
    print("clear_layout")
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()






def dobovlenie_row_for_matrix(): # Для плюса
    print("dobovlenie_row_for_matrix")
    

    try:
        new_razmer = int(form.Vse_matix[form.nomer_method].shape[0]) + 1 
        form.setSpinBox_RowElemValue(new_razmer, form.spinBox_RowElem)
        form.Enebled_button_minus()
        
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        form.show_error(f"Произошла ошибка при добовлении ряда")
  
def create_row_for_matrix():
    print("Create_row_for_matrix ")
    try:
        
        new_razmer = int(form.spinBox_RowElem.value())
        
        max_razmer = 12
        if new_razmer > max_razmer: 
            form.show_warning(f"Матрица размером {new_razmer} не может корректно отобразиться.")
            form.setSpinBox_RowElemValue(max_razmer, form.spinBox_RowElem)
            return
        
        # Оптимизация
        if new_razmer <= 1: return print("Попытка создать матрицу размером менее 2х3") #raise("Попытка создать матрицу размером менее 2х3")
        if new_razmer == int(form.Vse_matix[form.nomer_method].shape[0]): return print("Значение изменино через setSpinBox_RowElemValue или новый размер матрицы = старому")    
        # Оптимизация
        
        form.create_Kram_Oformlenie_for_ver_and_hor(new_razmer, new_razmer, form.Vse_verticalLayout_oformlenie[form.nomer_method], form.Vse_horizontalLayout_oformlenie[form.nomer_method]) # Оформление
        

        if new_razmer > 2: form.Enebled_button_minus()
        else: form.unEnebled_button_minus()


        
        form.Obnovlenie_value_matrix__svobonie_chleni(form.Vse_matix[form.nomer_method].shape[0], form.Vse_matix[form.nomer_method].shape[0], form.gridLayout_main)
        clear_layout(form.gridLayout_main)
        
        for i in range(new_razmer):
            for j in range(new_razmer+1):
                spin_box = QDoubleSpinBox()
                spin_box.setMinimum(-float('inf'))
                
                if i > int(form.Vse_matix[form.nomer_method].shape[0] - 1) or  j > int(form.Vse_matix[form.nomer_method].shape[0] - 1):
                    form.gridLayout_main.addWidget(spin_box, i, j)
                    continue
                else:
                    spin_box.setValue(form.Vse_matix[form.nomer_method][i, j])
                form.gridLayout_main.addWidget(spin_box, i, j)
                

        for i in range(new_razmer): ## Задаем значение свободных членов в уже созданные элементы layout
            
        # try:  
        # except Exception as e:
        #     print(f"Произошла ошибка: {e}")    

            print(f"form.svobonie_chleni.shape[0] = {form.Vse_svobonie_chleni[form.nomer_method].shape[0]}")
            if i < int(form.Vse_svobonie_chleni[form.nomer_method].shape[0]): ## [[],[],[]] - если оно так выглядит
                print(f"Create_row_for_matrix form.svobonie_chleni[{i}][0] = {form.Vse_svobonie_chleni[form.nomer_method][i][0]}")
                form.gridLayout_main.itemAtPosition(i, new_razmer).widget().setValue(form.Vse_svobonie_chleni[form.nomer_method][i][0])
            else: break
            
                    
        form.Obnovlenie_gridLayout_matrix__svobonie_chleni(new_razmer, new_razmer, form.gridLayout_main)
        form.Obnovlenie_value_matrix__svobonie_chleni(new_razmer, new_razmer, form.gridLayout_main)
            


    except Exception as e:
        print(f"Произошла ошибка: {e}")
   
def ubovlenie_row_for_matrix():
    print("ubovlenie_row_for_matrix")
    
    new_razmer = int(form.Vse_matix[form.nomer_method].shape[0]) - 1 ##### 
    
    
    form.setSpinBox_RowElemValue(new_razmer, form.spinBox_RowElem)
    if new_razmer == 2: form.unEnebled_button_minus() 

def Enebled_button_minus():
    print("Enebled_button_minus")
    form.pushButton_minus.setEnabled(True)
    
def unEnebled_button_minus():
    print("unEnebled_button_minus")
    form.pushButton_minus.setEnabled(False)
    
def setSpinBox_RowElemValue(value, SpinBox):
    print("setSpinBox_RowElemValue")
    SpinBox.setValue(value)
    
def checkGridLayout(Layout): 
    if Layout.count() == 0: return True 
    else: False
    
def create_Kram_Oformlenie_for_ver_and_hor(row, col, verticalLayout, horizontalLayout): # Добовляет Хn свержу и 1234... с боку
    print("create_Kram_Oformlenie_for_ver_and_hor")
    form.clear_layout(verticalLayout)
    form.clear_layout(horizontalLayout)

    form.create_Kram_for_ver(row, verticalLayout)
    form.create_Kram_for_hor(col, horizontalLayout)

def create_Kram_for_ver(row, verticalLayout):
    print(f"create_Kram_for_ver, row = {row}")
    for i in range(row):
            PushButton = QPushButton()
            PushButton.setEnabled(False)
            PushButton.setText(f"{int_to_roman(i+1)}")
            verticalLayout.addWidget(PushButton)

def create_Kram_for_hor(col , horizontalLayout): 
    print(f"create_Kram_for_hor, col = {col}")
    for i in range(col):
            PushButton = QPushButton()
            PushButton.setEnabled(False)
            PushButton.setText(f"X{subscript(i+1)}")
            horizontalLayout.addWidget(PushButton)
    # Для свободных
    PushButton = QPushButton()
    PushButton.setEnabled(False)
    PushButton.setText(f"B")
    horizontalLayout.addWidget(PushButton)

def main_MethodKramera():
    try:
        print("main_MethodKramera")
        if form.stackedWidget_main.currentIndex() != 0:
            form.stackedWidget_main.setCurrentIndex(0)
            form.nomer_method = "Kramer"
        else:
            return print("Попытка переключится на текущий метод")


    except Exception as e:
        print(f"Произошла ошибка: {e}")
        form.show_error(f"Произошла неизвестная ошибка")



## MGausa
def main_Gaus():
     try:
        print("main_Gaus")
        if form.stackedWidget_main.currentIndex() != 2:
            form.stackedWidget_main.setCurrentIndex(2)
            form.nomer_method = "Gaus"
        else:
            return print("Попытка переключится на текущий метод")


        if form.checkGridLayout(form.gridLayout_main_for_GaussElimination): # Если пуст то
            base_razmer = 2 # 2 финальный индекс 2*3
            
            form.Vstavka_elementov_v_gridLayout(base_razmer, form.gridLayout_main_for_GaussElimination)
            form.v_mathrix_and_b(base_razmer, form.nomer_method) #Запоминается начальная матрица
            form.create_Kram_Oformlenie_for_ver_and_hor(int(form.spinBox_for_row_Gausa.value()), int(form.spinBox_for_neRow_Gausa.value()), form.Vse_verticalLayout_oformlenie[form.nomer_method], form.Vse_horizontalLayout_oformlenie[form.nomer_method])

     except Exception as e:
        form.show_error(f"Произошла ошибка: {e}")

def create_Row_for_matrix_Gausa():
    print("create_Row_for_matrix_Gausa ")
    try:
        new_razmer = int(form.spinBox_for_row_Gausa.value())

        # Оптимизация
        if new_razmer <= 1: return print("Попытка создать матрицу размером менее 2х3")
        if new_razmer == int(form.Vse_matix[form.nomer_method].shape[0]): return print("Значение изменено через setSpinBox_RowElemValue(Gaus) или новый размер матрицы = старому")
        # if new_razmer == 2: form.unEnebled_button_minus() 
        # Оптимизация
        
        max_razmer = 12
        if new_razmer > max_razmer: 
            form.show_warning(f"Матрица размером {new_razmer}x{int(form.spinBox_for_neRow_Gausa.value())} не может корректно отобразиться.")
            form.setSpinBox_RowElemValue(max_razmer, form.spinBox_for_row_Gausa)
            return
        
        # if new_razmer > 2: form.Enebled_button_minus()
        # else: form.unEnebled_button_minus()
        form.create_Kram_Oformlenie_for_ver_and_hor(new_razmer, int(form.spinBox_for_neRow_Gausa.value()), form.Vse_verticalLayout_oformlenie[form.nomer_method], form.Vse_horizontalLayout_oformlenie[form.nomer_method])
        
        form.Obnovlenie_value_matrix__svobonie_chleni(form.Vse_matix[form.nomer_method].shape[0], form.Vse_matix[form.nomer_method].shape[1], form.gridLayout_main_for_GaussElimination)
        clear_layout(form.gridLayout_main_for_GaussElimination)
        

        print("Создание spinBox")
        for i in range(new_razmer):
            for j in range(form.Vse_matix[form.nomer_method].shape[1] + 1):
                spin_box = QDoubleSpinBox()
                spin_box.setMinimum(-float('inf'))
                

                if i > int(form.Vse_matix[form.nomer_method].shape[0] - 1) or  j > int(form.Vse_matix[form.nomer_method].shape[1] - 1):
                    form.gridLayout_main_for_GaussElimination.addWidget(spin_box, i, j)
                    continue
                else:
                    spin_box.setValue(form.Vse_matix[form.nomer_method][i, j])
                form.gridLayout_main_for_GaussElimination.addWidget(spin_box, i, j)
                    

        
        
        if form.Vse_matix[form.nomer_method].shape[0] >= int(form.spinBox_for_row_Gausa.value()): # Количество рядов(до обнавления) будет всегда меньшим значением, елси уменьшили размер то у spinBox, увеличели значит у matrix
            curent_col_row = int(form.spinBox_for_row_Gausa.value())
        else:
            curent_col_row = form.Vse_matix[form.nomer_method].shape[0] 
            
        for i in range(curent_col_row): ## Задаем значение свободных членов в уже созданные элементы layout
                print(f"form.Vse_matix[form.nomer_method].shape[0] = {form.Vse_matix[form.nomer_method].shape[0]}")
                form.gridLayout_main_for_GaussElimination.itemAtPosition(i, int(form.spinBox_for_neRow_Gausa.value())).widget().setValue(form.Vse_svobonie_chleni[form.nomer_method][i][0])


        form.Obnovlenie_gridLayout_matrix__svobonie_chleni(int(form.spinBox_for_row_Gausa.value()),int(form.spinBox_for_neRow_Gausa.value()), form.gridLayout_main_for_GaussElimination) 
        form.Obnovlenie_value_matrix__svobonie_chleni(new_razmer, form.Vse_matix[form.nomer_method].shape[1], form.gridLayout_main_for_GaussElimination)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def create_NeRow_for_matrix_Gausa():
    print("create_NeRow_for_matrix_Gausa")

    try:
        new_razmer = int(form.spinBox_for_neRow_Gausa.value())

        # Оптимизация
        if new_razmer <= 1:
            return print("Попытка создать матрицу размером менее 2х2")
        if new_razmer == int(form.Vse_matix[form.nomer_method].shape[1]):
            return print("Значение изменено через setSpinBox_ColumnElemValue(Gauss) или новый размер матрицы = старому")
        # Оптимизация
        
        max_razmer = 12
        if new_razmer > max_razmer: 
            form.show_warning(f"Матрица размером {int(form.spinBox_for_row_Gausa.value())}x{new_razmer} не может корректно отобразиться.")
            form.setSpinBox_RowElemValue(max_razmer, form.spinBox_for_neRow_Gausa)
            return

        form.create_Kram_Oformlenie_for_ver_and_hor(int(form.spinBox_for_row_Gausa.value()), new_razmer, form.Vse_verticalLayout_oformlenie[form.nomer_method], form.Vse_horizontalLayout_oformlenie[form.nomer_method])

        form.Obnovlenie_value_matrix__svobonie_chleni(
            form.Vse_matix[form.nomer_method].shape[0],
            form.Vse_matix[form.nomer_method].shape[1],
            form.gridLayout_main_for_GaussElimination
        )
        clear_layout(form.gridLayout_main_for_GaussElimination)

        print("Создание spinBox")
        for i in range(form.Vse_matix[form.nomer_method].shape[0]):
            for j in range(new_razmer + 1):  # +1 для свободных членов
                spin_box = QDoubleSpinBox()
                spin_box.setMinimum(-float('inf'))

                if j > int(form.Vse_matix[form.nomer_method].shape[1] - 1) or i > int(form.Vse_matix[form.nomer_method].shape[0] - 1):
                    form.gridLayout_main_for_GaussElimination.addWidget(spin_box, i, j)
                    continue
                else:
                    spin_box.setValue(form.Vse_matix[form.nomer_method][i, j])
                form.gridLayout_main_for_GaussElimination.addWidget(spin_box, i, j)

        
        
        if form.Vse_matix[form.nomer_method].shape[0] >= int(form.spinBox_for_row_Gausa.value()): # Текущее будет всегда меньшим значением, елси уменьшили размер то у spinBox, увеличели значит у matrix
            curent_col_row = int(form.spinBox_for_row_Gausa.value())
        else:
            curent_col_row = form.Vse_matix[form.nomer_method].shape[0]
            
        for i in range(curent_col_row):  # Устанавливаем значения свободных членов
                print(f"form.Vse_matix[form.nomer_method].shape[0] = {form.Vse_matix[form.nomer_method].shape[0]}")
                form.gridLayout_main_for_GaussElimination.itemAtPosition(i, new_razmer).widget().setValue(form.Vse_svobonie_chleni[form.nomer_method][i][0])

        
        
        form.Obnovlenie_gridLayout_matrix__svobonie_chleni(int(form.spinBox_for_row_Gausa.value()),int(form.spinBox_for_neRow_Gausa.value()), form.gridLayout_main_for_GaussElimination) 
        form.Obnovlenie_value_matrix__svobonie_chleni(form.Vse_matix[form.nomer_method].shape[0], new_razmer, form.gridLayout_main_for_GaussElimination)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def method_Gausa():
    try:
        #метод обновления value матриц для агрументов ниже
        form.Obnovlenie_gridLayout_matrix__svobonie_chleni(int(form.spinBox_for_row_Gausa.value()),int(form.spinBox_for_neRow_Gausa.value()), form.gridLayout_main_for_GaussElimination)
        
        matrix, B = form.Vse_matix[form.nomer_method].tolist(), form.Vse_svobonie_chleni[form.nomer_method].tolist()
        
        form.stackedWidget_main.setCurrentIndex(3) # Переключение на страницу с form.listWidget_for_reshenia
        form.listWidget_for_reshenia_Gausa.clear()

        form.Otvet_Gausa = GaussElimination(matrix, B, form.listWidget_for_reshenia_Gausa)
        form.Vse_Otvet["Gaus"] = form.Otvet_Gausa
        form.pushButton_bolshe_Gaus.setEnabled(True)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}") 
        
def plus_row_Gaus():
    curent_razmer = int(form.spinBox_for_row_Gausa.value())
    form.setSpinBox_RowElemValue(curent_razmer + 1, form.spinBox_for_row_Gausa)
    
def minus_row_Gausa():
    curent_razmer = int(form.spinBox_for_row_Gausa.value())
    form.setSpinBox_RowElemValue(curent_razmer - 1, form.spinBox_for_row_Gausa)
    
    
def plus_x_Gausa():
    curent_razmer = int(form.spinBox_for_neRow_Gausa.value())
    form.setSpinBox_RowElemValue(curent_razmer + 1, form.spinBox_for_neRow_Gausa)

def minus_x_Gausa():
    curent_razmer = int(form.spinBox_for_neRow_Gausa.value())
    form.setSpinBox_RowElemValue(curent_razmer - 1, form.spinBox_for_neRow_Gausa)


# Gaus_Gordan
def main_Gaus_Gordan():
    try:
        print("main_Gaus_Gordan")

        if form.stackedWidget_main.currentIndex() != 4:
            form.stackedWidget_main.setCurrentIndex(4)
            form.nomer_method = "Gaus_Gordan"
        else:
            return print("Попытка переключится на текущий метод")


        if form.checkGridLayout(form.gridLayout_main_for_GaussJordanElimination): # Если пуст то
            base_razmer = 2 # 2 финальный индекс 2*3
            form.Vstavka_elementov_v_gridLayout(base_razmer, form.gridLayout_main_for_GaussJordanElimination)
            form.v_mathrix_and_b(base_razmer, form.nomer_method) #Запоминается начальная матрица
            form.create_Kram_Oformlenie_for_ver_and_hor(int(form.spinBox_for_row_GaussJordanElimination.value()), int(form.spinBox_for_neRow_GaussJordanElimination.value()), form.Vse_verticalLayout_oformlenie[form.nomer_method], form.Vse_horizontalLayout_oformlenie[form.nomer_method])

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def create_Row_for_matrix_GaussJordanElimination():
    print("create_Row_for_matrix_Gausa ")
    try:
        new_razmer = int(form.spinBox_for_row_GaussJordanElimination.value())
        

        # Оптимизация
        if new_razmer <= 1: return print("Попытка создать матрицу размером менее 2х3")
        if new_razmer == int(form.Vse_matix[form.nomer_method].shape[0]): return print("Значение изменено через setSpinBox_RowElemValue(Gaus_Gordan) или новый размер матрицы = старому")
        # Оптимизация
        
        max_razmer = 12
        if new_razmer > max_razmer: 
            form.show_warning(f"Матрица размером {new_razmer}x{int(form.spinBox_for_neRow_GaussJordanElimination.value())} не может корректно отобразиться.")
            form.setSpinBox_RowElemValue(max_razmer, form.spinBox_for_row_GaussJordanElimination)
            return
        
        # if new_razmer > 2: form.Enebled_button_minus()
        # else: form.unEnebled_button_minus()
        form.create_Kram_Oformlenie_for_ver_and_hor(new_razmer, int(form.spinBox_for_neRow_GaussJordanElimination.value()), form.Vse_verticalLayout_oformlenie[form.nomer_method], form.Vse_horizontalLayout_oformlenie[form.nomer_method])
        
        form.Obnovlenie_value_matrix__svobonie_chleni(form.Vse_matix[form.nomer_method].shape[0], form.Vse_matix[form.nomer_method].shape[1], form.gridLayout_main_for_GaussJordanElimination)
        clear_layout(form.gridLayout_main_for_GaussJordanElimination)
        

        print("Создание spinBox")
        for i in range(new_razmer):
            for j in range(form.Vse_matix[form.nomer_method].shape[1] + 1):
                spin_box = QDoubleSpinBox()
                spin_box.setMinimum(-float('inf'))
                

                if i > int(form.Vse_matix[form.nomer_method].shape[0] - 1) or  j > int(form.Vse_matix[form.nomer_method].shape[1] - 1):
                    form.gridLayout_main_for_GaussJordanElimination.addWidget(spin_box, i, j)
                    continue
                else:
                    spin_box.setValue(form.Vse_matix[form.nomer_method][i, j])
                form.gridLayout_main_for_GaussJordanElimination.addWidget(spin_box, i, j)
                    

        
        
        if form.Vse_matix[form.nomer_method].shape[0] >= int(form.spinBox_for_row_GaussJordanElimination.value()): # Количество рядов(до обнавления) будет всегда меньшим значением, елси уменьшили размер то у spinBox, увеличели значит у matrix
            curent_col_row = int(form.spinBox_for_row_GaussJordanElimination.value())
        else:
            curent_col_row = form.Vse_matix[form.nomer_method].shape[0] 
            
        for i in range(curent_col_row): ## Задаем значение свободных членов в уже созданные элементы layout
                print(f"form.Vse_matix[form.nomer_method].shape[0] = {form.Vse_matix[form.nomer_method].shape[0]}")
                form.gridLayout_main_for_GaussJordanElimination.itemAtPosition(i, int(form.spinBox_for_neRow_GaussJordanElimination.value())).widget().setValue(form.Vse_svobonie_chleni[form.nomer_method][i][0])


        form.Obnovlenie_gridLayout_matrix__svobonie_chleni(int(form.spinBox_for_row_GaussJordanElimination.value()),int(form.spinBox_for_neRow_GaussJordanElimination.value()), form.gridLayout_main_for_GaussJordanElimination) 
        form.Obnovlenie_value_matrix__svobonie_chleni(new_razmer, form.Vse_matix[form.nomer_method].shape[1], form.gridLayout_main_for_GaussJordanElimination)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
def create_NeRow_for_matrix_GaussJordanElimination():
    print("create_NeRow_for_matrix_GaussJordanElimination")

    try:
        new_razmer = int(form.spinBox_for_neRow_GaussJordanElimination.value())

        # Оптимизация
        if new_razmer <= 1:
            return print("Попытка создать матрицу размером менее 2х2")
        if new_razmer == int(form.Vse_matix[form.nomer_method].shape[1]):
            return print("Значение изменено через setSpinBox_ColumnElemValue(Gauss) или новый размер матрицы = старому")
        # Оптимизация
        
        max_razmer = 12
        if new_razmer > max_razmer: 
            form.show_warning(f"Матрица размером {int(form.spinBox_for_row_GaussJordanElimination.value())}x{new_razmer} не может корректно отобразиться.")
            form.setSpinBox_RowElemValue(max_razmer, form.spinBox_for_neRow_GaussJordanElimination)
            return

        
        form.create_Kram_Oformlenie_for_ver_and_hor(int(form.spinBox_for_row_GaussJordanElimination.value()), new_razmer, form.Vse_verticalLayout_oformlenie[form.nomer_method], form.Vse_horizontalLayout_oformlenie[form.nomer_method])

        form.Obnovlenie_value_matrix__svobonie_chleni(
            form.Vse_matix[form.nomer_method].shape[0],
            form.Vse_matix[form.nomer_method].shape[1],
            form.gridLayout_main_for_GaussJordanElimination
        )
        clear_layout(form.gridLayout_main_for_GaussJordanElimination)

        print("Создание spinBox")
        for i in range(form.Vse_matix[form.nomer_method].shape[0]):
            for j in range(new_razmer + 1):  # +1 для свободных членов
                spin_box = QDoubleSpinBox()
                spin_box.setMinimum(-float('inf'))

                if j > int(form.Vse_matix[form.nomer_method].shape[1] - 1) or i > int(form.Vse_matix[form.nomer_method].shape[0] - 1):
                    form.gridLayout_main_for_GaussJordanElimination.addWidget(spin_box, i, j)
                    continue
                else:
                    spin_box.setValue(form.Vse_matix[form.nomer_method][i, j])
                form.gridLayout_main_for_GaussJordanElimination.addWidget(spin_box, i, j)

        
        
        if form.Vse_matix[form.nomer_method].shape[0] >= int(form.spinBox_for_row_GaussJordanElimination.value()): # Текущее будет всегда меньшим значением, елси уменьшили размер то у spinBox, увеличели значит у matrix
            curent_col_row = int(form.spinBox_for_row_GaussJordanElimination.value())
        else:
            curent_col_row = form.Vse_matix[form.nomer_method].shape[0]
            
        for i in range(curent_col_row):  # Устанавливаем значения свободных членов
                print(f"form.Vse_matix[form.nomer_method].shape[0] = {form.Vse_matix[form.nomer_method].shape[0]}")
                form.gridLayout_main_for_GaussJordanElimination.itemAtPosition(i, new_razmer).widget().setValue(form.Vse_svobonie_chleni[form.nomer_method][i][0])

        
        
        form.Obnovlenie_gridLayout_matrix__svobonie_chleni(int(form.spinBox_for_row_GaussJordanElimination.value()),int(form.spinBox_for_neRow_GaussJordanElimination.value()), form.gridLayout_main_for_GaussJordanElimination) 
        form.Obnovlenie_value_matrix__svobonie_chleni(form.Vse_matix[form.nomer_method].shape[0], new_razmer, form.gridLayout_main_for_GaussJordanElimination)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def method_GaussJordanElimination():
    try:
        #метод обновления value матриц для агрументов ниже
        form.Obnovlenie_gridLayout_matrix__svobonie_chleni(int(form.spinBox_for_row_GaussJordanElimination.value()),int(form.spinBox_for_neRow_GaussJordanElimination.value()), form.gridLayout_main_for_GaussJordanElimination)
        
        matrix, B = form.Vse_matix[form.nomer_method].tolist(), form.Vse_svobonie_chleni[form.nomer_method].tolist()
        
        form.stackedWidget_main.setCurrentIndex(5) # Переключение на страницу с form.listWidget_for_reshenia
        form.listWidget_for_reshenia_GaussJordanElimination.clear()

        form.Otvet_GaussJordanElimination = GaussJordanElimination(matrix, B, form.listWidget_for_reshenia_GaussJordanElimination)
        form.Vse_Otvet["Gaus_Gordan"] = form.Otvet_GaussJordanElimination
        
        form.pushButton_bolshe_GaussJordan.setEnabled(True)
    except Exception as e:
        print(f"Произошла ошибка: {e}") 

def set_value_for_all_doublespinboxes(layout, value): # Проходим по всем элементам макета 
        print("set_value_for_all_doublespinboxes")    
        for i in range(layout.count()): 
            widget = layout.itemAt(i).widget() # Если виджет является QDoubleSpinBox, устанавливаем заданное значение 
            widget.setValue(value)

def actionClean_click():
    print("actionClean_click")    
    set_value_for_all_doublespinboxes(form.Vse_gridLayout_for_matrix[form.nomer_method], 0.0)
    
def action_exit_click():
    QCoreApplication.quit()
    
def Export_Excel_xlsx():
    print("Export_Excel_xlsx")
    print(f"form.nomer_method = {form.nomer_method}")
    try:
        if form.nomer_method in form.Vse_Otvet:
       

            # Уберите использование `Options()`, если оно недоступно
            file_name, _ = QFileDialog.getSaveFileName(
                window,
                "Save File",
                "",
                "Excel Files (*.xlsx);;All Files (*)"
            )

            if file_name:
                if not file_name.endswith('.xlsx'):
                    file_name += '.xlsx'
                form.Vse_Otvet[form.nomer_method].save_to_excel(file_name)



 
        else:
            form.show_warning("Для начала, я все же рекомендую найти решение матрицы!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        form.show_error("Неизвестная ошибка! Давайте больше небудем так делать.")
        
    # excel_file = "output.xlsx" 
    
def show_warning(text): # Создаем предупреждающее сообщение 
    print("show_warning")
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Icon.Warning) 
    msg.setText(text) 
    msg.setWindowTitle("Warning") 
    msg.setStandardButtons(QMessageBox.StandardButton.Ok) 
    msg.exec()
    
def show_error(text):  # Создаем сообщение об ошибке
    print("show_error")
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)  # Устанавливаем значок "Ошибка"
    msg.setText(text)
    msg.setWindowTitle("Error")  # Заголовок окна
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Кнопка "ОК"
    msg.exec()
    
def plus_row_GaussJordanElimination():
    curent_razmer = int(form.spinBox_for_row_GaussJordanElimination.value())
    form.setSpinBox_RowElemValue(curent_razmer + 1, form.spinBox_for_row_GaussJordanElimination)
    
def minus_row_GaussJordanElimination():
    curent_razmer = int(form.spinBox_for_row_GaussJordanElimination.value())
    form.setSpinBox_RowElemValue(curent_razmer - 1, form.spinBox_for_row_GaussJordanElimination)
    
def plus_x_GaussJordanElimination():
    curent_razmer = int(form.spinBox_for_neRow_GaussJordanElimination.value())
    form.setSpinBox_RowElemValue(curent_razmer + 1, form.spinBox_for_neRow_GaussJordanElimination)

def minus_x_GaussJordanElimination():
    curent_razmer = int(form.spinBox_for_neRow_GaussJordanElimination.value())
    form.setSpinBox_RowElemValue(curent_razmer - 1, form.spinBox_for_neRow_GaussJordanElimination)

def ToResh():
    print("ToResh") 
    try:
            current_index = form.stackedWidget_main.currentIndex()
            form.stackedWidget_main.setCurrentIndex(current_index + 1)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
   
        
def ToMethod():
    print("ToMethod") 
    current_index = form.stackedWidget_main.currentIndex()
    if current_index == 1:
        form.main_MethodKramera()
    elif current_index == 3:
        form.main_Gaus()
    elif current_index == 5:
        form.main_Gaus_Gordan()
    

    

# def vpered():
#     pass


Form, Window = uic.loadUiType("mainUi.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.method_kramera = method_kramera
form.Obnovlenie_gridLayout_matrix__svobonie_chleni = Obnovlenie_gridLayout_matrix__svobonie_chleni
form.Obnovlenie_value_matrix__svobonie_chleni = Obnovlenie_value_matrix__svobonie_chleni
form.v_mathrix_and_b = v_mathrix_and_b
form.Vstavka_elementov_v_gridLayout = Vstavka_elementov_v_gridLayout
form.dobovlenie_row_for_matrix = dobovlenie_row_for_matrix
form.ubovlenie_row_for_matrix = ubovlenie_row_for_matrix
form.create_row_for_matrix = create_row_for_matrix

form.setSpinBox_RowElemValue = setSpinBox_RowElemValue
form.Enebled_button_minus = Enebled_button_minus
form.unEnebled_button_minus = unEnebled_button_minus
form.main_Gaus = main_Gaus
form.checkGridLayout = checkGridLayout
form.create_NeRow_for_matrix_Gausa = create_NeRow_for_matrix_Gausa
form.create_Row_for_matrix_Gausa = create_Row_for_matrix_Gausa
form.method_Gausa = method_Gausa

form.create_Kram_Oformlenie_for_ver_and_hor = create_Kram_Oformlenie_for_ver_and_hor
form.create_Kram_for_hor = create_Kram_for_hor
form.create_Kram_for_ver = create_Kram_for_ver
form.clear_layout = clear_layout
form.main_MethodKramera = main_MethodKramera


form.main_Gaus_Gordan = main_Gaus_Gordan
form.create_NeRow_for_matrix_GaussJordanElimination = create_NeRow_for_matrix_GaussJordanElimination
form.create_Row_for_matrix_GaussJordanElimination = create_Row_for_matrix_GaussJordanElimination
form.method_GaussJordanElimination = method_GaussJordanElimination


form.minus_x_Gausa = minus_x_Gausa
form.plus_x_Gausa = plus_x_Gausa
form.minus_row_Gausa = minus_row_Gausa
form.plus_row_Gaus = plus_row_Gaus

form.minus_x_GaussJordanElimination = minus_x_GaussJordanElimination
form.plus_x_GaussJordanElimination = plus_x_GaussJordanElimination
form.minus_row_GaussJordanElimination = minus_row_GaussJordanElimination
form.plus_row_GaussJordanElimination = plus_row_GaussJordanElimination



# Menu
form.Export_Excel_xlsx = Export_Excel_xlsx
form.action_exit_click = action_exit_click
form.actionClean_click = actionClean_click

# Навигация 
form.ToResh = ToResh
form.ToMethod = ToMethod
# form.nathad = nathad

#Excel
form.action_Excel_xlsx.triggered.connect(form.Export_Excel_xlsx)

# MsBoxError
form.show_warning = show_warning
form.show_error = show_error

main()

form.action_exit.triggered.connect(form.action_exit_click)
form.actionClean_2.triggered.connect(form.actionClean_click)




#Kramer
form.pushButton_resh.clicked.connect(form.method_kramera)
form.pushButton_plus.clicked.connect(form.dobovlenie_row_for_matrix)
form.pushButton_minus.clicked.connect(form.ubovlenie_row_for_matrix)
form.spinBox_RowElem.valueChanged.connect(form.create_row_for_matrix)
form.action_MethodKramera.triggered.connect(form.main_MethodKramera)

form.pushButton_bolshe.clicked.connect(form.ToResh)
form.pushButton_menshe_Kr.clicked.connect(form.ToMethod)

# Gaus
form.action_GaussElimination.triggered.connect(form.main_Gaus)
form.spinBox_for_neRow_Gausa.valueChanged.connect(form.create_NeRow_for_matrix_Gausa)
form.spinBox_for_row_Gausa.valueChanged.connect(form.create_Row_for_matrix_Gausa)
form.pushButton_GaussElimination.clicked.connect(form.method_Gausa)


form.pushButton_bolshe_Gaus.clicked.connect(form.ToResh)
form.pushButton_menshe_Gaus.clicked.connect(form.ToMethod)

form.pushButton_del_stolb_Gaus.clicked.connect(form.minus_x_Gausa)
form.pushButton_new_stolb_Gaus.clicked.connect(form.plus_x_Gausa)
form.pushButton_del_row_Gaus.clicked.connect(form.minus_row_Gausa)
form.pushButton_new_row_Gaus.clicked.connect(form.plus_row_Gaus)


form.pushButton_del_stolb_2.clicked.connect(form.minus_x_Gausa)
form.pushButton_new_stolb_2.clicked.connect(form.plus_x_Gausa)
form.pushButton_del_row_2.clicked.connect(form.minus_row_Gausa)
form.pushButton_new_row_2.clicked.connect(form.plus_row_Gaus)



# Gaus_Gordan
form.action_GaussElimination_Gordan.triggered.connect(form.main_Gaus_Gordan)
form.spinBox_for_neRow_GaussJordanElimination.valueChanged.connect(form.create_NeRow_for_matrix_GaussJordanElimination)
form.spinBox_for_row_GaussJordanElimination.valueChanged.connect(form.create_Row_for_matrix_GaussJordanElimination)
form.pushButton_GaussJordanElimination.clicked.connect(form.method_GaussJordanElimination)


form.pushButton_bolshe_GaussJordan.clicked.connect(form.ToResh)
form.pushButton_menshe_GaussJordan.clicked.connect(form.ToMethod)


form.pushButton_del_stolb_GaussJordanElimination.clicked.connect(form.minus_x_GaussJordanElimination)
form.pushButton_new_stolb_GaussJordanElimination.clicked.connect(form.plus_x_GaussJordanElimination)
form.pushButton_del_row_GaussJordanElimination.clicked.connect(form.minus_row_GaussJordanElimination)
form.pushButton_new_row_GaussJordanElimination.clicked.connect(form.plus_row_GaussJordanElimination)





form.pushButton_del_stolb_3.clicked.connect(form.minus_x_GaussJordanElimination)
form.pushButton_new_stolb_3.clicked.connect(form.plus_x_GaussJordanElimination)
form.pushButton_del_row_3.clicked.connect(form.minus_row_GaussJordanElimination)
form.pushButton_new_row_3.clicked.connect(form.plus_row_GaussJordanElimination)

app.exec()




