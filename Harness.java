import java.util.HashMap;
import java.util.Map;
public class Harness
{
  static Map<Character, Integer> countCharacters(String str){
    HashMap<Character, Integer> counts = new HashMap<Character, Integer>();
    for (int i=0; i<str.length(); i++){
      Character c = str.charAt(i);
      Integer count = counts.get(c);
      if (count == null){
        counts.put(c, 1);
      }else{
        counts.put(c, count+1);
      }
    }
    return counts;
  }

  static boolean isPermutation(String one, String two){
    Map<Character, Integer> oneCounts = countCharacters(one);
    Map<Character, Integer> twoCounts = countCharacters(two);
    return oneCounts.equals(twoCounts);
  }

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
    System.out.println("String "+args[0]+" is permutation of " + args[1]+" ? "+ isPermutation(args[0], args[1]));
  }
}
