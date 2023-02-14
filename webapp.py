import streamlit as st
from main import BSOption

st.write('''
# Price a Vanilla Option
This application allows you to price either a call or put option
''')

st.sidebar.header('# Parameters to enter')

display = ("Call", "Put")
CP = st.sidebar.selectbox(
    'Do you want to price a Call or a Put ?',
    display
)

with st.form('Pricer'):

    with st.sidebar:
        S = st.slider('The Stock Price : ', 0, 200, 100)
        K = st.slider('The Strike Price : ', 0, 200, 100)
        T = st.slider('The maturity : ', 0.0, 5.0, step=0.5)
        r = st.slider('The interest rate (%) : ', 0, 10, 5)
        v = st.slider('The volatility (%) : ', 0, 20, 5)
        submit_button = st.form_submit_button(label='👉 Compute 👈')


class Pricing:

    def __init__(self):

        self.CP = "C"
        self.S = self.get_S()
        self.K = self.get_K()
        self.T = self.get_T()
        self.r = self.get_r()/100
        self.v = self.get_v()/100
        self.q = 0

        self.option = BSOption(self.CP, S, self.K, self.T, self.r, self.v, self.q).price()

    @staticmethod
    def get_S():
        return S

    @staticmethod
    def get_K():
        return K

    @staticmethod
    def get_T():
        return T

    @staticmethod
    def get_r():
        return r

    @staticmethod
    def get_v():
        return v

    def get_q(self):
        return self.q

    def load_data(self):
        st.write("The price of the Option is : {}".format(self.option))


if submit_button:
    x = Pricing()
    x.load_data()
