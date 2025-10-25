import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyANnykcNWoZKb2ua_DueiUOxLSjf6M6_g8",
  "authDomain": "fyp1-8c5db.firebaseapp.com",
  "databaseURL": "https://fyp1-8c5db-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "projectId": "fyp1-8c5db",
  "storageBucket": "fyp1-8c5db.appspot.com",
  "messagingSenderId": "376978501989",
  "appId": "1:376978501989:web:8fa76223e44da0407d318c"
   }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

x=db.child("Data").get()
#print(x.val())
for user in x.each():
    print(user.val())
