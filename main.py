from sqlalchemy.orm import sessionmaker

from modelis import engine, Person, Account, Bank

Session = sessionmaker(bind=engine)
session = Session()

def sukurti_vartotoja():
    name = input("Įveskite vardą: ")
    surname = input("Įveskite pavardę: ")
    social_nr = int(input("Įveskite asmens kodą: "))
    phone_nr = input("Įveskite telefono numerį: ")

    person = Person(name=name, surname=surname, social_nr=social_nr, phone_nr=phone_nr)
    # account = Account(person=person)

    session.add(person)
    # session.add(account)
    session.commit()

def sukurti_banka():
    name = input("Įveskite pavadinimą: ")
    adress = input("Įveskite adresą: ")
    swif_code = input("Įveskite SWIF kodą: ")

    bank = Bank(name=name, adress=adress, swif_code=swif_code)
    session.add(bank)
    session.commit()

def sukurti_saskaita():
    person_id = input("Įveskite vartotojo ID: ")
    bank_id = input("Įveskite banko ID: ")
    iban_nr = input("Įveskite sąskaitos numerį: ")
    account = Account(person_id=person_id,bank_id=bank_id,iban_nr=iban_nr, balance=0)
    session.add(account)
    session.commit()

def prideti_pajamas_islaidas():
    select = input(print("Pasirinkite: 1 - Pridėti; 2 - Atimti"))
    if select == '1':
        person_id = int(input("Įveskite vartotojo ID: "))
        suma = int(input("Įveskite pridedamą sumą: "))
        account = session.query(Account).filter_by(person_id=person_id).first()
        account.balance += suma
        print("Suma pridėta.")
        session.commit()

    elif select == '2':
        person_id = int(input("Įveskite vartotojo ID: "))
        suma = int(input("Įveskite atimamą sumą: "))
        account = session.query(Account).filter_by(person_id=person_id).first()
        account.balance -= suma
        print("Suma atimta.")
        session.commit()
    else:
        print("Bloga opcija. Prašome pabandyti dar.")
        session.commit()

def perziureti_saskaitas():
    accounts = session.query(Account).all()
    if accounts:
        for account in accounts:
            print("Vartotojo ID: ", account.person_id)
            print("Sąskaitos ID: ", account.id)
            print("IBAN numeris: ", account.iban_nr)
            print("Balansas: ", account.balance)
            print("Banko ID: ", account.bank_id)
            print("------------------")
    else:
        print("Nėra jokių duomenų.")

def perziureti_vartotojus():
    persons = session.query(Person).all()
    if persons:
        for person in persons:
            print("Vartotojo ID: ", person.id)
            print("Vardas: ", person.name)
            print("Pavardė: ", person.surname)
            print("Asmens kodas: ", person.social_nr)
            print("Telefono numeris: ", person.phone_nr)
            print("------------------")
    else:
        print("Nėra jokių duomenų.")

def perziureti_bankus():
    banks = session.query(Bank).all()
    if banks:
        for bank in banks:
            print("Vartotojo ID: ", bank.id)
            print("Vardas: ", bank.name)
            print("Pavardė: ", bank.adress)
            print("SWIF kodas: ",bank.swif_code)
            print("------------------")
    else:
        print("Nėra jokių duomenų.")

def main_menu():
    while True:
        print("\nBankeris")
        print("1. Pridėti vartotoją")
        print("2. Pridėti banką")
        print("3. Pridėti sąskaitą")
        print("4. Pridėti pajamas/išlaidas")
        print("5. Peržiūrėti sąskaitas")
        print("6. Peržiūrėti vartotojus")
        print("7. Peržiūrėti bankus")
        print("8. Išeiti")

        choice = input("Pasirinkite opciją: ")

        if choice == '1':
            sukurti_vartotoja()
        elif choice == '2':
            sukurti_banka()
        elif choice == '3':
            sukurti_saskaita()
        elif choice == '4':
            prideti_pajamas_islaidas()
        elif choice == '5':
            perziureti_saskaitas()
        elif choice == '6':
            perziureti_vartotojus()
        elif choice == '7':
            perziureti_bankus()
        elif choice == '8':
            print("Programos pabaiga.")
            break
        else:
            print("Bloga opcija. Prašome pabandyti dar.")

main_menu()