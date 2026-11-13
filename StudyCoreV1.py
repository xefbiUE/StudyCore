import math
import os
import time
from groq import Groq

# Inserisci qui la tua chiave API di Groq (inizia con gsk_...)
client = Groq(api_key="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")

# MATEMATICA
def matematica():
    print("WIP")

# FISICA
def fisica():
    print("\n---SEZIONE DI FISICA---")
    print("WIP")

    

# LATINO
def latino():
    print("\n---SEZIONE DI LATINO---")
    print("WIP")

# SCIENZE
def scienze():
    print("\n---SEZIONE DI SCIENZE---")
    print("WIP")

# STORIA (Integrata con Groq IA)
def storia():
    print("\n---SEZIONE DI STORIA---")
    print("Chiedi un riassunto, un ripasso o fatti interrogare.")
    print("Scrivi 'esci' per tornare al menu principale.\n")
    
    cronologia = [
        {
            "role": "system",
            "content": (
                "Sei un tutor di storia per uno studente di seconda liceo scientifico in Italia "
                "(programma: crisi della Repubblica Romana, Impero Romano, Alto Medioevo). "
                "Spiega in modo chiaro, schematico e preciso. Se lo studente ti chiede di essere "
                "interrogato, fagli una domanda alla volta e valuta la sua risposta."
            )
        }
    ]
    
    while True:
        domanda = input("Tu: ")
        if domanda.lower() == "esci":
            print("Ritorno al menu principale...")
            time.sleep(1)
            break
            
        cronologia.append({"role": "user", "content": domanda})
        
        try:
            risposta_ia = client.chat.completions.create(
                messages=cronologia,
                model="openai/gpt-oss-120b",
            )
            
            testo_risposta = risposta_ia.choices[0].message.content
            print(f"\nProfessore IA: {testo_risposta}\n")
            
            cronologia.append({"role": "assistant", "content": testo_risposta})
            
        except Exception as e:
            print(f"\nErrore di connessione con Groq: {e}\n")


#POESIA
def poesia():
    print("\n---SEZIONE DI POESIA---")
    print("Chiedi un'analisi del testo, un ripasso di letteratura/grammatica o fatti interrogare.")
    print("Scrivi 'esci' per tornare al menu principale.\n")
    
    cronologia = [
        {
            "role": "system",
            "content": (
                "Sei un tutor di italiano per uno studente di seconda liceo scientifico in Italia "
                "(programma: analisi del testo poetico e narrativo, I Promessi Sposi di Manzoni, "
                "letteratura delle origini, stilnovismo e grammatica/sintassi del periodo). "
                "Spiega in modo chiaro, schematico e preciso. Se lo studente ti chiede di essere "
                "interrogato o di analizzare un brano, fagli una domanda alla volta e valuta la sua risposta."
            )
        }
    ]
    
    while True:
        domanda = input("Tu: ")
        if domanda.lower() == "esci":
            print("Ritorno al menu principale...")
            time.sleep(1)
            break
            
        cronologia.append({"role": "user", "content": domanda})
        
        try:
            risposta_ia = client.chat.completions.create(
                messages=cronologia,
                model="openai/gpt-oss-120b",
            )
            
            testo_risposta = risposta_ia.choices[0].message.content
            print(f"\nProfessore IA: {testo_risposta}\n")
            
            cronologia.append({"role": "assistant", "content": testo_risposta})
            
        except Exception as e:
            print(f"\nErrore di connessione con Groq: {e}\n")


# GRAMMATICA 
def grammatica():
    print("\n---SEZIONE DI GRAMMATICA---")
    print("Chiedi aiuto per analisi logica, analisi del periodo, regole o esercizi.")
    print("Scrivi 'esci' per tornare al menu principale.\n")
    
    cronologia = [
        {
            "role": "system",
            "content": (
                "Sei un tutor di grammatica italiana per uno studente di seconda liceo scientifico in Italia "
                "(programma: analisi grammaticale, analisi logica, analisi del periodo con proposizioni "
                "principali, coordinate e subordinate, uso dei modi e tempi verbali, ortografia e punteggiatura). "
                "Spiega in modo chiaro, schematico e preciso. Se lo studente ti scrive una frase da analizzare, "
                "scomponila passo dopo passo. Se chiede esercizi, proponi una frase alla volta e correggi la sua risposta."
            )
        }
    ]
    
    while True:
        domanda = input("Tu: ")
        if domanda.lower() == "esci":
            print("Ritorno al menu principale...")
            time.sleep(1)
            break
            
        cronologia.append({"role": "user", "content": domanda})
        
        try:
            risposta_ia = client.chat.completions.create(
                messages=cronologia,
                model="openai/gpt-oss-120b",
            )
            
            testo_risposta = risposta_ia.choices[0].message.content
            print(f"\nProfessore IA: {testo_risposta}\n")
            
            cronologia.append({"role": "assistant", "content": testo_risposta})
            
        except Exception as e:
            print(f"\nErrore di connessione con Groq: {e}\n")





# WIKI
def wiki():
    print("\n---WIKI CODICI ERRORI---")
    print("Error Code 1: Il numero inserito non rientra nel range.")

# MENU
def menu():
    while True:
        print("\n===============================")
        print("---ASSISTENTE STUDIO---")
        print("1. Matematica")
        print("2. Fisica")
        print("3. Latino")
        print("4. Scienze")
        print("5. Storia")
        print("6. Poesia")
        print("7. Grammatica")
        print("8. Wiki Errori")
        print("0. Esci")
        print("===============================")
        scelta = input("Scegli un'opzione (0-8): ")
        
        if scelta == "1":
            matematica()
        elif scelta == "2":
            fisica()
        elif scelta == "3":
            latino()
        elif scelta == "4":
            scienze()
        elif scelta == "5":
            storia()
        elif scelta == "6":
            poesia()
        elif scelta == "7":
            grammatica()
        elif scelta == "8":
            wiki()
        elif scelta == "0":
            print("Fine programma in 3 secondi.")
            time.sleep(3)
            break
        else:
            print("Error 1. Vedi wiki")

# Avvia il programma
if __name__ == "__main__":
    menu()
