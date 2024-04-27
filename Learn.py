#Bu python dosyasında python öğrenirken yaptığım çalışmalar yer alıyor

#Burada math modülü koda dahil ediliyor
import math
#burada yatak odası ve banyo sayısına göre ev fiyatını veren bir fonksiyon oluşturdum
def get_expected_cost(beds, baths):
    value = (beds * 30000) + (baths * 10000) + 80000
    return value

#burada 4 farklı kombinasyon için ev fiyatı hesaplaması yapılıyor
option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

#print komutu ile hesaplanan değerler ekrana yazdırılıyor
print(option_one)
print(option_two)
print(option_three)
print(option_four)

#burada duvar boyamanın maliyet hesapı için bir fonksiyon oluşturdum
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost

#burada boyama maliyeti hesabı için gerekli değişkenler verilip maliyet hesaplanıyor
project_cost = get_cost(432,144, 400, 15)

#print komutu ile hesaplanan değerler ekrana yazdırılıyor
print(project_cost)


def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    gallons_to_buy = math.ceil(gallons_needed)
    cost = cost_per_gallon * gallons_to_buy
    return cost

#print komutu ile hesaplanan değerler ekrana yazdırılıyor
print(get_actual_cost(594, 288, 400, 15))

#Data types
#x'in değeri 14 olarak beklirleniyor
x = 14
print(x)
#burada x değişkeninin tipi sorgulanıp ekrana yazdırılıyor
print(type(x))

nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
print(type(nearly_pi))

almost_pi = 22/7
print(almost_pi)
print(type(almost_pi))

rounded_pi = round(almost_pi, 5)
print(rounded_pi)
print(type(rounded_pi))

z_one = True
print(z_one)
print(type(z_one))

z_two = False
print(z_two)
print(type(z_two))

z_three = (1 < 2)
print(z_three)
print(type(z_three))

z_four = (5 < 3)
print(z_four)
print(type(z_four))

z_five = not z_four
print(z_five)
print(type(z_five))

w = "Hello, Python!"
print(w)
print(type(w))
print(len(w))

shortest_string = ""
print(type(shortest_string))
print(len(shortest_string))

my_number = "1.12321"
print(my_number)
print(type(my_number))

also_my_number = float(my_number)
print(also_my_number)
print(type(also_my_number))

new_string = "abc" + "def"
print(new_string)
print(type(new_string))

newest_string = "abc" * 3
print(newest_string)
print(type(newest_string))

# Define a float
y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))

print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))

def get_expected_costa(beds, baths, has_basement):
    value = 80000 + 30000 * beds + 10000 * baths + 40000 * has_basement
    return value

get_expected_costa(1, 1, False)
print(get_expected_costa(1, 1, False))

print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)

def cost_of_projectx(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

project_zero = cost_of_projectx('mama', True)
print(project_zero)

project_one = cost_of_projectx("Charlie+Denver", True)
print(project_one)

project_two = cost_of_projectx("08/10/2000", False)
print(project_two)

print(2 > 3)

var_one = 1
var_two = 2

print(var_one < 1)
print(var_two >= var_one)

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))
print(evaluate_temp(39))

def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(37))

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

conda = evaluate_temp_with_elif(36)
condb = evaluate_temp_with_elif(34)
print(conda)
print(condb)

def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed
#The next code cell uses the function.

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)

def add_three_or_eight(number):
    if number < 10:
        result = number + 3
    else:
        result = number + 8
    return result

conq = add_three_or_eight(10.0001)
print(conq)

def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose

conv = get_dose(8.4)
print(conv)

def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

print(get_grade(49))
print(get_grade(85))



# option 1
def cost_of_projecta1(engraving, solid_gold):
    num_units = len(engraving)
    if solid_gold == True:
        cost = 100 + 10 * num_units
    else:
        cost = 50 + 7 * num_units
    return cost

# option 2
def cost_of_projecta2(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10 * len(engraving)
    else:
        cost = 50 + 7 * len(engraving)
    return cost

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = 5 * num_gallons / 1000
    elif num_gallons <= 22000:
        bill = 6 * num_gallons / 1000
    elif num_gallons <= 30000:
        bill = 7 * num_gallons / 1000
    else:
        bill = 10 * num_gallons / 1000
    return bill


def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = 100 + (gb - 15) * 100
    return bill

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers))
print(flowers)

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)

# The list has ten entries
print(len(flowers_list))

print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])

#You can also pull a segment of a list (for instance, the first three entries or the last two entries). This is called slicing. For instance:
#to pull the first x entries, you use [:x], and
#to pull the last y entries, you use [-y:].

print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

flowers_list.remove("globe thistle")
print(flowers_list)

flowers_list.append("snapdragon")
print(flowers_list)

hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])

print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))

print("Total books sold in one week:", sum(hardcover_sales))

print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)

# Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

q = avg_first_seven = sum(num_customers[:7])/7
w = avg_last_seven = sum(num_customers[-7:])/7
e = max_month = max(num_customers)
r = min_month = min(num_customers)
print(q, w, e, r)

flowers9 = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
print(flowers.split(","))

# Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

letters = alphabet.split(".")
formatted_address = address.split(",")

test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(test_liked)

def percentage_liked(ratings):
    list_liked = [i >= 4 for i in ratings]
    percentage_liked = sum(list_liked)/len(list_liked)
    return percentage_liked

# should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])

def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth


# Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Should return .036
print(percentage_growth(num_users_test, 1))

# Should return 0.66
print(percentage_growth(num_users_test, 7))