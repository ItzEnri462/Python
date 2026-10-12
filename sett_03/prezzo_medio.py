import csv


def prezzo_medio(nome_file, alimentazione):
    somma, quantita = 0, 0
    with open(nome_file, "r", encoding="utf-8") as f:
        lettore = csv.DictReader(
            f, fieldnames=["Brand", "Model", "Engine", "Fuel type", "Year", "Mileage", "price"]
        )
        for macchine in lettore:
            if macchine["Fuel type"] == alimentazione:
                somma += float(macchine["price"])
                quantita += 1;
        if quantita == 0:
            return None
        return somma / quantita

for tipo in ["Petrol", "Diesel", "Hybrid", "Elettrica"]:
    print(type, ": ", prezzo_medio("dati/car_sales_data.csv", tipo))