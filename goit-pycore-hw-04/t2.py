
with open('goit-pycore-hw-04/t2_data.txt', 'w') as t2_data:
  t2_data.write("""60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5""")
    
def get_cats_info(path):
  try:
      with open(path, 'r+') as file:
        cats_list = []
        for line in file:
          cat_id, cat_name, cat_age = line.strip().split(',')
          cats_list.append({'id': cat_id, 'name': cat_name, 'age': cat_age })
        return cats_list
  except FileNotFoundError:
        print("Файл не знайдено.")
        return []
  except Exception as e:
        print(f"Помилка: {e}")
        return []
get_cats_info('goit-pycore-hw-04/t2_data.txt')