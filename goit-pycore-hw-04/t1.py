
with open('goit-pycore-hw-04/t1_data.txt', 'w') as t1_data:
    t1_data.write("""Alex Korp,3000
                  Nikita Borisenko,2000
                  Sitarama Raju,1000""")


def total_salary(path):
    try:
      with open(path, 'r+', encoding='utf-8') as file:
        salaries = []
        total_salary = 0
        for line in file:
          _ , salary = line.split(',')
          total_salary += int(salary.strip())
          salaries.append(salary.strip())
          average_salary = total_salary // len(salaries)
        return(salaries, total_salary, average_salary)
    except FileNotFoundError:
      print("Файл не знайдено.")
      return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0
    

total_salary('/Users/ottice.milch/Desktop/neo_hws/t1_data.txt')