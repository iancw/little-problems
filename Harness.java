public class Harness
{
  static boolean unique(String s){
    for (int i=0; i<s.length(); i++){
      for (int j=0; j<s.length(); j++){
        if (i == j) {
          continue;
        }
        if (s.charAt(i) == s.charAt(j)){
          return false;
        }
      }
    }
    return true;
  }


  public static void main(String[] args)
  {
    System.out.println("String "+args[0]+" is unique? "+ unique(args[0]));
  }
}
