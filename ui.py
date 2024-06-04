from logger import changeData, deleteData, inputData, outputData

def interface():

  flag = True
  while(flag):
    command = int(input('Добрый день!\n Выберите функцию: \n 1 - запись данных\n 2 - вывод данных\n 3 - изменение данных\n 4 - удаление данных\n 5 - завершение программы\nВведите число: '))
    if command == 1:
      inputData()
    elif command == 2:
      outputData()
    elif command == 3:
      changeData()
    elif command == 4:
      deleteData()
    elif command == 5:
      flag = False
    else:
      print("введена не правильная команда, повторите ввод: ")