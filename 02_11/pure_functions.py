# פןנקציה טהורה כי אין side effect ועבור כל פרמטר נכנס יצא אותה תוצאה
def square(n):
    return n * n
 # פןנקציה טהורה כי אין side effect ועבור כל פרמטר נכנס יצא אותה תוצאה
def log_square(n):
    print("squaring", n)
    return n * n
 # פונקציה לא טהורה כי היא משנה רשימה 
def add_item(cart, item):
    cart.append(item)
    return cart
# פונקציה טהורה כי היא מחזירה רשימה חדשה
def with_item(cart, item):
    return cart + [item]
