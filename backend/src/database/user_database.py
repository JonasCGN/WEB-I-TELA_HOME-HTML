from datetime import datetime
from src.database.db import connection
from decimal import Decimal
import random
class UserDatabase:

    @staticmethod
    def format_user_data(user_tuple):
        return {
            "idUser": user_tuple[0],
            "nome": user_tuple[1],
            "sobrenome": user_tuple[2],
            "email": user_tuple[3],
            "senha": user_tuple[4],
            "limite": float(user_tuple[5]) if isinstance(user_tuple[5], Decimal) else user_tuple[5],
            "criado": user_tuple[6].strftime("%Y-%m-%d %H:%M:%S.%f") if isinstance(user_tuple[6], datetime) else user_tuple[6],
            "atualizado": user_tuple[7].strftime("%Y-%m-%d %H:%M:%S.%f") if isinstance(user_tuple[7], datetime) else user_tuple[7]
        }
    
    @staticmethod
    def get_all_users():
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
            conn.close()
            return users
        return []

    @staticmethod
    def get_user_by_id(user_id):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE idUser = %s", (user_id,))
                user = cursor.fetchone()
            conn.close()
            return UserDatabase.format_user_data(user)
        return None

    @staticmethod
    def create_user(nome, sobrenome, email, senha):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (nome, sobrenome, email, senha, limite ,criado, atualizado) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (nome, sobrenome, email, senha, random.randrange(1000, 10000), datetime.now(), datetime.now())
                )
                conn.commit()
            conn.close()

    @staticmethod
    def update_user(user_id, **kwargs):
        if not kwargs:
            return

        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                campos = ", ".join([f"{campo} = %s" for campo in kwargs.keys()])
                valores = list(kwargs.values()) + [user_id]

                query = f"UPDATE users SET {campos}, atualizado = %s WHERE idUser = %s"
                valores.insert(-1, datetime.now())  # Insere a data antes do ID

                cursor.execute(query, valores)
                conn.commit()
            conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE idUser = %s", (user_id,))
                conn.commit()
            conn.close()
    
    @staticmethod
    def connect_user(email,senha) -> tuple:
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                        SELECT * FROM users 
                        WHERE email = %s AND senha = crypt(%s, senha);
                    ''', 
                    (email,senha)
                )
                user = cursor.fetchone()
                print('Usuario', user)
            conn.close()
            if user:
                return (True, UserDatabase.format_user_data(user))
        return False, None

