import pandas as pd

# Загружаем Excel-файл
xls = pd.ExcelFile("s7_data_sample_rev4_50k.xlsx")

# Показываем названия всех листов
print("Листы в файле:")
print(xls.sheet_names)

# Загружаем первый лист
df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

# Показываем названия всех столбцов
print("\nСтолбцы в первом листе:")
for col in df.columns:
    print(f"- {col!r}")
