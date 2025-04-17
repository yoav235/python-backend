from django.shortcuts import render
import json
import os
from django.http import JsonResponse, HttpResponseNotFound
from django.conf import settings

# מבנה שבו נאחסן את המשתמשים
# המפתח הוא תעודת זהות, והערך הוא מילון עם הנתונים של המשתמש
user_map = {}


# קריאת קובץ JSON בעת טעינת המודול
def load_users_from_json():
    global user_map
    file_path = os.path.join(settings.BASE_DIR, 'users.json')  # מניח שהקובץ נמצא בתיקיית הבסיס של הפרויקט
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            users = json.load(f)
            for user in users:
                user_map[user['id']] = user
    except FileNotFoundError:
        print(f"⚠️ File {file_path} not found.")
    except Exception as e:
        print(f"⚠️ Error loading users: {e}")


# טוען את המשתמשים ברגע שהמודול נטען
load_users_from_json()


# GET /users/ - מחזיר רשימת שמות
def get_all_users(request):
    names = [user["name"] for user in user_map.values()]
    return JsonResponse(names, safe=False)


# GET /users/<name>/ - מחזיר את המשתמש עם השם הספציפי
def get_user_by_name(request, name):
    for user in user_map.values():
        if user["name"].lower() == name.lower():  # השוואה לא רגישה לרישיות
            return JsonResponse(user)
    return HttpResponseNotFound(f"User with name '{name}' not found")


def create_user(request):
    if (request.method != 'POST'):
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    data = json.loads(request.body)

    required_fields = ['id', 'name', 'phone', 'address']
    for field in required_fields:
        if field not in data:
            return JsonResponse({'error': f'Missing field: {field}'}, status=400)
    if not is_valid_israeli_id(data["id"]):
        return JsonResponse({'error': 'Invalid Israeli ID'}, status=400)
    if not is_valid_israeli_phone(data["phone"].replace("-", "", 1)):
        return JsonResponse({'error': f'Invalid Israeli phone number - {data["phone"]}'}, status=400)

    user_map[data["id"]] = data

    return JsonResponse(data, status=201)


def control_digit(id_num):
    total = 0
    for i in range(8):
        val = int(id_num[i]) # converts char to int
        if i%2 == 0:        # even index (0,2,4,6,8)
            total += val
        else:               # odd index (1,3,5,7,9)
            if val < 5:
                total += 2*val
            else:
                total += ((2*val)%10) + 1 # sum of digits in 2*val
                                          # 'tens' digit must be 1
    total = total%10            # 'ones' (rightmost) digit
    check_digit = (10-total)%10 # the complement modulo 10 of total
                                # for example 42->8, 30->0
    return str(check_digit)


def is_valid_israeli_id(id_number):
    """
    Check if the given ID number is a valid Israeli ID number.
    """
    if not id_number.isdigit() or len(id_number) < 5 or len(id_number) > 9:
        return False

    id_number = id_number.zfill(9)  # Add leading zeros if needed
    return id_number[-1] == control_digit(id_number[:-1])  # Check the last digit


def is_valid_israeli_phone(phone_number):
    """
    Check if the given phone number is a valid Israeli phone number.
    """
    phone_number.replace("-", "", 1)
    if not phone_number.isdigit() or phone_number[0:2] != '05':
        return False
    # Israeli phone numbers are 10 digits long
    return len(phone_number) == 10
