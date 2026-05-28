from tkinter import messagebox

# ==========================================
# USERS
# ==========================================

users = {

    "admin": {
        "password": "admin123",
        "role": "ADMIN"
    },

    "teacher": {
        "password": "teacher123",
        "role": "TEACHER"
    },

    "student": {
        "password": "student123",
        "role": "STUDENT"
    }

}

# ==========================================
# VALIDATE LOGIN
# ==========================================

def validate_login(username, password):

    if username in users:

        if users[username]["password"] == password:

            return (
                True,
                users[username]["role"]
            )

    return (
        False,
        None
    )

# ==========================================
# LOGIN SUCCESS
# ==========================================

def show_login_success(role):

    messagebox.showinfo(
        "Login Success",
        f"Welcome {role}"
    )

# ==========================================
# LOGIN ERROR
# ==========================================

def show_login_error():

    messagebox.showerror(
        "Login Failed",
        "Invalid Username or Password"
    )
