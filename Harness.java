import java.util.HashMap;
public class Harness
{
  static boolean unique(String s){
    HashMap<Character, Boolean> map = new HashMap<Character, Boolean>();
    for (int i=0; i<s.length(); i++){
      Boolean prior = map.get(s.charAt(i));
      if (prior != null && prior){
          return false;
      }
      map.put(s.charAt(i), Boolean.TRUE);
    }
    return true;
  }


  public static void main(String[] args)
  {
    System.out.println("String "+args[0]+" is unique? "+ unique(args[0]));
  }
}
