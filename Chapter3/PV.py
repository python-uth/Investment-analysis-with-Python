# Υπολογισμός Μελλοντικής και Παρούσας Αξίας
import numpy_financial as npf # εισάγουμε τη βιβλιοθήκη με τη συντομογραφία npf
# υπολογισμός παρούσας αξίας
npf.pv(rate=0.02, nper=5, pmt=-22, fv=0, when=0)
# εναλλακτικά μπορούμε να μη συμπεριλάβουμε τις ονομασίες των παραμέτρων
npf.pv(0.02, 5, 22,0,0)
# υπολογισμός μελλοντικής αξίας
npf.fv(rate=0.02, nper=5, pmt=-10, pv=0, when=0)
# εναλλακτικά μπορούμε να μη συμπεριλάβουμε τις ονομασίες των παραμέτρων
npf.fv(0.02, 5, 10,0,0)
# υπολογισμός επιτοκίου
npf.rate(nper=5, pmt=-10, pv=0, fv=55.26, when=0)
# εναλλακτικά μπορούμε να μη συμπεριλάβουμε τις ονομασίες των παραμέτρων
npf.rate(5, -10, 0, 55.26,0)

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της παρούσας αξίας μίας χρηματικής ροής
def pvFunction(fv,r,n):
    """
    Μεταβλητές:
    fv (float): μελλοντική αξία
    r (float): επιτόκιο (ως δεκαδικό)
    n (int): αριθμός περιόδων
    """
    return fv/(1+r)**n

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της παρούσας αξίας μίας ράντας
def pvAnnuity(c,r,n):
    """
    Μεταβλητές:
    c (float): περιοδική καταβολή
    r (float): επιτόκιο (ως δεκαδικό)
    n (int): αριθμός περιόδων
    """
    return c/r*(1-1/(1+r)**n)

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της παρούσας αξίας μίας προκαταβλητέας ράντας
def pvAnnuityDue(c,r,n):
    """
    Μεταβλητές:
    c (float): περιοδική καταβολή
    r (float): επιτόκιο (ως δεκαδικό)
    n (int): αριθμός περιόδων
    """
    return c/r*(1-1/(1+r)**n)*(1+r)

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της παρούσας αξίας μίας αυξανόμενης ράντας
def pvGrowingAnnuity(c,r,n,g):
    """
    Μεταβλητές:
    c (float): περιοδική καταβολή
    r (float): επιτόκιο (ως δεκαδικό)
    n (int): αριθμός περιόδων
    g (float): ρυθμός αύξησης (ως δεκαδικό)
    """
    return c/r*(1-(1+g)**n/(1+r)**n)

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της μελλοντικής αξίας μίας χρηματικής ροής
def fvFunction(pv,r,n):
    """
    Μεταβλητές:
    pv (float): παρούσα αξία
    r (float): επιτόκιο (ως δεκαδικό)
    n (int): αριθμός περιόδων
    """
    return pv*(1+r)**n

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της μελλοντικής αξίας μίας ράντας
def fvAnnuity(c,r,n):
    """
    Μεταβλητές:
    c (float): περιοδική καταβολή
    r (float): επιτόκιο (ως δεκαδικό)
    n (int): αριθμός περιόδων
    """
    return c/r*((1+r)**n-1)

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της μελλοντικής αξίας μίας προκαταβλητέας ράντας
def fvAnnuityDue(c,r,n):
    """
    Μεταβλητές:
    c (float): περιοδική καταβολή
    r (float): επιτόκιο (ως δεκαδικό)
    n (int): αριθμός περιόδων
    """
    return c/r*((1+r)**n-1)*(1+r)

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της μελλοντικής αξίας μίας αυξανόμενης ράντας
def fvGrowingAnnuity(c, r, n, g):
    """
    Μεταβλητές:
    c (float): περιοδική καταβολή
    r (float): επιτόκιο (ως δεκαδικό)
    n (int): αριθμός περιόδων
    g (float): ρυθμός αύξησης (ως δεκαδικό)
    """
    return c * ((1 + r)**n - (1 + g)**n) / (r - g)

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της παρούσας αξίας μίας διηνεκούς ράντας
def pvPerpetuity(c,r):
    """
    Μεταβλητές:
    c (float): περιοδική καταβολή
    r (float): επιτόκιο (ως δεκαδικό)
    """
    return c/r

# Ορίζουμε μια συνάρτηση για τον υπολογισμό της παρούσας αξίας μίας αυξανόμενης διηνεκούς ράντας
def pvGrowingPerpetuity(c,r,g):
    """
    Μεταβλητές:
    c (float): περιοδική καταβολή
    r (float): επιτόκιο (ως δεκαδικό)
    g (float): ρυθμός αύξησης (ως δεκαδικό)
    """
    return c/(r-g)

# Ορισμός Συνάρτησης που υπολογίζει την τιμή ενός έντοκου γραμματίου 
def calculate_bill_price(nominal_value, interest_rate, time_days):
    """
    Υπολογίζει την τιμή ενός έντοκου γραμματίου (ΕΓ)

    Παράμετροι:
    - nominal_value: η ονομαστική αξία του ΕΓ
    - interest_rate: το ετήσιο επιτόκιο (ως δεκαδικό)
    - time_days: Αριθμός ημερών διάρκειας του ΕΓ

    Αποτέλεσμα:
    - Η παρούσα αξία (τιμή) του έντοκου γραμματίου (με τρία δεκαδικά)
    """
    price = nominal_value / (1 + interest_rate * time_days / 360)
    return round(price, 3)

# Ορισμός Συνάρτησης που υπολογίζει την απόδοση ενός έντοκου γραμματίου
def calculate_bill_rate(nominal_value, price, time_days):
    """
    Υπολογίζει την απόδοση ενός έντοκου γραμματίου (ΕΓ) με δεδομένη μια τρέχουσα αγοραία τιμή

    Παράμετροι:
    - nominal_value: Η ονομαστική αξία του ΕΓ
    - price: Η τρέχουσα τιμή του ΕΓ
    - time_days: Αριθμός ημερών διάρκειας του ΕΓ

    Αποτέλεσμα:
    - Το ετησιοποιημένο επιτόκιο-απόδοση του ΕΓ (ως ποσοστό με δύο δεκαδικά)
    """
    interest_rate = ((nominal_value / price) - 1) * (360 / time_days)
    return round(interest_rate * 100, 2)



