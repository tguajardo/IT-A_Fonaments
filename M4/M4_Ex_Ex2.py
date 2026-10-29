# Demana a l'usuari/ària un número entre 0 i 99 i mostra'l escrit en lletres (pots fer-ho en català o castellà).
# Exemple: 56 (cinquanta-sis) o 56 (cincuenta y seis)

# Variables
num: int
text_num_in: str
dec: str = ""
uni: str = ""
text_num_out: str

# Get Data
text_num_in = input("Introdueix un número entre 0 i 99: ")

# Check Data
if text_num_in.isdigit():
    num = int(text_num_in)
    if num > 99:
        print("Error: has d'introduir un nombre enter entre 0 i 99.")
        exit()
else:
    print("Error: has d'introduir un nombre enter entre 0 i 99.")
    exit()

# Operations
# Numbers with no replicability
if num == 0:
    text_num_out = "Zero"
elif num < 20 and num >= 10:
    match num:
        case 10:
            text_num_out = "Deu"
        case 11:
            text_num_out = "Onze"
        case 12:
            text_num_out = "Dotze"
        case 13:
            text_num_out = "Tretze"
        case 14:
            text_num_out = "Catorze"
        case 15:
            text_num_out = "Quinze"
        case 16:
            text_num_out = "Setze"
        case 17:
            text_num_out = "Disset"
        case 18:
            text_num_out = "Divuit"
        case 19:
            text_num_out = "Dinou"

# Numbers that follow {dec}-{uni} writing
else:
    if num >= 20:
        match text_num_in[0]:
            case "2":
                if text_num_in[-1] == "0":
                    dec = "Vint"
                else:
                    dec = "Vint-i"
            case "3":
                dec = "Trenta"
            case "4":
                dec = "Quaranta"
            case "5":
                dec = "Cinquanta"
            case "6":
                dec = "Seixanta"
            case "7":
                dec = "Setanta"
            case "8":
                dec = "Vuitanta"
            case "9":
                dec = "Noranta"
        if text_num_in[-1] != "0":
            dec = f"{dec}-"
    match text_num_in[-1]:
        case "1":
            uni = "un"
        case "2":
            uni = "dos"
        case "3":
            uni = "tres"
        case "4":
            uni = "quatre"
        case "5":
            uni = "cinc"
        case "6":
            uni = "sis"
        case "7":
            uni = "set"
        case "8":
            uni = "vuit"
        case "9":
            uni = "nou"
        case "0":
            uni = ""
    text_num_out = f"{dec}{uni}"

# Output
print(f"{num} -> {text_num_out}")
