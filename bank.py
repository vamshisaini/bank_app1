import streamlit as st

# Page Config
st.set_page_config(page_title="Bank App", page_icon="🏦", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .stNumberInput>div>div>input {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Business Logic
class BankApplication:
    bank_name = 'SBI'

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"✅ Withdrawn ₹{amount}\n💰 Balance: ₹{self.balance}"
        else:
            return "❌ Insufficient balance"

    def deposit(self, amount):
        self.balance += amount
        return f"✅ Deposited ₹{amount}\n💰 Balance: ₹{self.balance}"

    def update_mobile(self, new_num):
        self.mobile_number = new_num
        return f"📱 Updated Mobile: {self.mobile_number}"

    def check_balance(self):
        return f"💰 Current Balance: ₹{self.balance}"

# Title
st.markdown("<h1 style='text-align: center;'>🏦 Smart Bank App</h1>", unsafe_allow_html=True)

# Session State
if "account" not in st.session_state:
    st.session_state.account = None

# Sidebar Menu
menu = st.sidebar.selectbox("Navigation", ["Create Account", "Bank Services"])

# Create Account Page
if menu == "Create Account":
    st.subheader("📝 Create New Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Name")
        age = st.number_input("🎂 Age", min_value=1)

    with col2:
        acc_no = st.text_input("🏧 Account Number")
        mobile = st.text_input("📱 Mobile Number")

    balance = st.number_input("💵 Initial Deposit", min_value=0)

    if st.button("🚀 Create Account"):
        st.session_state.account = BankApplication(name, acc_no, age, mobile, balance)
        st.success("🎉 Account Created Successfully!")

# Bank Services Page
elif menu == "Bank Services":
    if st.session_state.account:
        acc = st.session_state.account

        st.subheader(f"👋 Welcome, {acc.name}")

        st.info(f"🏦 Bank: {BankApplication.bank_name} | 🆔 Acc No: {acc.account_number}")

        service = st.selectbox("Choose Service", [
            "Deposit 💵",
            "Withdraw 💸",
            "Check Balance 💰",
            "Update Mobile 📱"
        ])

        if service == "Deposit 💵":
            amount = st.number_input("Enter amount", min_value=0)
            if st.button("Deposit"):
                st.success(acc.deposit(amount))

        elif service == "Withdraw 💸":
            amount = st.number_input("Enter amount", min_value=0)
            if st.button("Withdraw"):
                st.success(acc.withdraw(amount))

        elif service == "Check Balance 💰":
            if st.button("Check Balance"):
                st.info(acc.check_balance())

        elif service == "Update Mobile 📱":
            new_mobile = st.text_input("Enter new number")
            if st.button("Update"):
                st.success(acc.update_mobile(new_mobile))

    else:
        st.warning("⚠️ Please create an account first!")

# Footer
st.markdown("""
---
<p style='text-align: center;'>Made with ❤️ using Streamlit</p>
""", unsafe_allow_html=True)
