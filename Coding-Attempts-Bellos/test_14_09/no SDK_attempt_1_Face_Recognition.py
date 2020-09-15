import cv2

# Φορτωσε το machine learning βοήθημα μας
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Αυτό ισχύει για λήψη βίντεο από κάμερα web, ομως αν εχω συνδεσει την D435i την διαβάζει πρώτη και χρησιμοποιεί αυτήν
cap = cv2.VideoCapture(0)


while True:
    # Διάβασε το frame
    _, img = cap.read()

    # Μετέτρεψε σε κλίμακα του γκρι
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Εντόπισε τα πρόσωπα
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Φτιάξε τετράγωνο γυρω από κάθε πρόσωπο
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Εμφάνισε
    cv2.imshow('img', img)


    key = cv2.waitKey(1)
    # Πάτα το 'q' για να κλείσει το παράθυρο αφού πρώτα το έχεις επιλέξει
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# Αποδέσμευσε την κάμερα
cap.release()
