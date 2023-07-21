import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ismjcomp-firebase-adminsdk-5wsg0-7342b6cb63.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://ismjcomp-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
        {
            "name": "Hardik",
            "branch": "BAI",
            "reg_no": "20BAI1048",
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "2":
        {
            "name": "Harikishan",
            "branch": "BAI",
            "reg_no": "20BAI1297",
            "total_attendance": 0,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "3":
        {
            "name": "Elon Musk",
            "branch": "BAI",
            "reg_no": "20BAI1310",
            "total_attendance": 0,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
    
}

for key, value in data.items():
    ref.child(key).set(value)