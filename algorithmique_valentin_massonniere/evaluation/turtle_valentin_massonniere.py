from turtle import *
import os

class Triangle:
    @staticmethod
    def triangle1(a):
        try:
            a = float(a)
            for i in range(3):
                forward(a)
                left(120)
            return
        except ValueError:
            print("Veuillez entrer un nombre")
            return
        
    @staticmethod
    def triangle2(a):
        try:
            a = float(a)
            right(180)
            for i in range(3):
                forward(a)
                left(120)
            return
        except ValueError as v:
            print(f"Une erreur est survenue : {v} : Veuillez entrer un nombre")
            return   

    @staticmethod
    def triangle3(a, angle):
        try:
            a = float(a)
            angle = float(angle)
            right(angle)
            for i in range(3):
                forward(a)
                left(120)
            return
        except ValueError as v:
            print(f"Une erreur est survenue : {v} : Veuillez entrer un nombre")
            return
    
    @staticmethod
    def triangle_color(a):
        try:
            a = float(a)
            color("violet", "orange")
            pensize(5)
            begin_fill()
            for i in range(3):
                forward(a)
                left(120)
            end_fill()
            penup()
            forward(a)
            pendown()
            return
        except ValueError as v:
            print(f"Une erreur est survenue : {v} : Veuillez entrer un nombre")
            return
        

class Sqaure:
    @staticmethod
    def carre(a):
        try:
            a = float(a)
            for i in range(4):
                forward(a)
                left(90)
        except ValueError as v:
            print(f"Une erreur est survenue : {v} : Veuillez entrer un nombre")
            return

    @staticmethod
    def ligneDeCarres(a, n):
        try:
            a = float(a)
            n = int(n)
            for i in range(n):
                for j in range(4):
                    forward(a)
                    left(90)
                penup()
                forward(a * 2)
                pendown()
                return
        except ValueError as v:
            print(f"Une erreur est survenue : {v} : Veuillez entrer un nombre")
            return

    @staticmethod 
    def carresCroissants(a, n):
        try:
            a = float(a)
            n = int(n)
            espace = a / 4 
            for i in range(n):
                for j in range(4):
                    forward(a)
                    left(90)
                penup()
                forward(a + espace)
                pendown()
                a *= 1.25
                espace *= 1.25
                return
        except ValueError as v:
            print(f"Une erreur est survenue : {v} : Veuillez entrer un nombre")
            return
    
    @staticmethod
    def square_color(a):
        try:
            a = float(a)
            color("violet", "orange")
            pensize(5)
            begin_fill()
            for i in range(4):
                forward(a)
                left(90)
            end_fill()
            penup()
            forward(a)
            pendown()
            return
        except ValueError as v:
            print(f"Une erreur est survenue : {v} : Veuillez entrer un nombre")
            return


class Figures:
    @staticmethod
    def figuresPleines(rep, a):
        try:
            rep = int(rep)
            a = float(a)
            bgcolor("white")
            for i in range(rep):
                Triangle.triangle_color(a)
                Sqaure.square_color(a)
            return
        except ValueError as v:
            print(f"Une erreur est survenue : {v} : Veuillez entrer un nombre")
            return

    @staticmethod    
    def polygone(a, n):
        try:
            a = float(a)
            n = int(n)  
            angle = 360 / n 
            for i in range(n):
                forward(a)
                left(angle) 
            return
        except ValueError as v:
            print(f"Une erreur est survenue : {v}. Veuillez entrer des valeurs numériques correctes.")
            return

    @staticmethod
    def star(a, n):
        try:
            a = float(a)
            n = int(n)
            if n % 2 == 0 or n < 5:
                print("Veuillez entrer un nombre impair supérieur ou égal à 5 pour n.")
                return
    
            angle = 144
            for i in range(n):
                forward(a)
                right(angle)
            return
        except ValueError as v:
            print(f"Une erreur est survenue : {v}. Veuillez entrer des valeurs numériques correctes.")
            return
        

class CursorMover:
    @staticmethod
    def reset_page():
        try:
            reset()
            return
        except Exception as e:
            print(f"Une erreur est survenue lors de la réinitialisation de la page : {e}")
            return

    @staticmethod
    def move_cursor():
        try:
            penup()
            goto(0, 0) 
            setheading(0)
            pendown()
            color("black")
            pensize(1)
            return
        except Exception as e:
            print(f"Une erreur est survenue lors du déplacement du curseur : {e}")
            return


class Radius:
    @staticmethod
    def rayons(n, d):
        try:
            n = int(n)
            d = float(d)
            angle = 360 / n
            for i in range(n):
                forward(d)
                backward(d)
                left(angle)
            return
        except ValueError as v:
            print(f"Une erreur est survenue : {v}. Veuillez entrer des valeurs numériques correctes.")
            return

speed(100)
Triangle.triangle1(100)
CursorMover.move_cursor()
Triangle.triangle2(300)
CursorMover.move_cursor()
Triangle.triangle3(300, 45)
CursorMover.move_cursor()
Sqaure.carre(50)
CursorMover.move_cursor()
Sqaure.ligneDeCarres(50, 5)
CursorMover.move_cursor()
Sqaure.carresCroissants(50, 5)
CursorMover.move_cursor()
Figures.figuresPleines(4, 50)
CursorMover.move_cursor()
Radius.rayons(18, 60)
CursorMover.move_cursor()
Figures.polygone(100, 6)
CursorMover.move_cursor()
Figures.star(100, 5)

os.system("pause")