import java.util.Scanner;

public class Main {

//   # 4.2.1
// # Entier val, double
// # Début
// # Val ← 231
// # Double ← Val * 2
// # Ecrire Val
// # Ecrire Double
// # Fin
  public static void exo4_2_1() {
    int value = 231;
    int double_value = 231*2;
    System.out.println(value);
    System.out.println(double_value);
  }

//   # 4.2.2
// # Ecrire un programme qui demande un nombre à l’utilisateur, puis qui calcule et
// # affiche le carré de ce nombre.
// # Indices :
// # Pour convertir la chaîne « 123 » en nombre 123 écrire :
// # Val = int(“123”)
// # Pour élever A à la puissance B : A ** B

public static void exo4_2_2() {
   Scanner user_input = new Scanner(System.in);
   System.out.println("Entrez un nombre");
   String user_number = user_input.nextLine();
   user_input.close();

   try {
    int number = Integer.valueOf(user_number);
    System.out.println(Math.pow(number, 2));
   } catch (Exception e) {
      System.out.println("Invalid integer input");
   }
}
  public static void main(String[] args) {
    exo4_2_1();
    exo4_2_2();
  }
}