import streamlit as st

st.title("Cadastro de Clientes")

nome = st.text_input("Digite o nome do Cliente")
endereco = st.text_input("Digite o endereço do ")
dt = st.date_input ("Escolha a data de Nascimento")
tipo = st.selectbox ("Tipo de Cliente" , ["Pessoa Física", "Pessoa Jurídica"])

cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("clientes.csv", "a") as arquivo:
        arquivo.write(f"{nome}, {endereco}, {dt}, {tipo}\n")
        st.success("Cliente cadastrado com sucesso!")