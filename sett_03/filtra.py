import csv

def filtra(origine, destinazione, marca, anno_minimo):
    selezionate = []
    with open(origine, "r", encoding="utf-8", newline="") as f:
        for auto in csv.DictReader(f):
            if auto["Manufacturer"] == marca and int(auto["Year of manufacture"]) >= anno_minimo:
                selezionate.append([auto["Model"], auto["Year of manufacture"], auto["Price"]])

    selezionate.sort(key=lambda r: int(r[2]), reverse=True)

    with open(destinazione, "w", encoding="utf-8", newline="") as f:
        scrittore = csv.writer(f)
        scrittore.writerow(["Model", "Year", "Price"])
        scrittore.writerows(selezionate)

    return len(selezionate)

quante = filtra("dati/car_sales_data.csv", "porsche.csv", "Porsche", 2015)
print("auto salvate:", quante)

with open("porsche.csv", "r", encoding="utf-8") as f:
    for i, riga in enumerate(f):
        if i == 4:
            break
        print(riga.strip())