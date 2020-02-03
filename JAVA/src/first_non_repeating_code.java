import java.util.*;
public class first_non_repeating_code {
    public static char firstNonRepeatedCharacter(String word) {
        HashMap<Character,Integer> scoreboard = new HashMap<>();
        for (int i = 0; i < word.length(); i++)
        {
            char c = word.charAt(i);
            if (scoreboard.containsKey(c))
            {
                scoreboard.put(c, scoreboard.get(c) + 1);
            }
            else
            { scoreboard.put(c, 1);
            }
        }
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (scoreboard.get(c) == 1)
            { return c; }

        }
        throw new RuntimeException("Undefined behaviour");

    }
    public static void main (String[] args) {
        try{
            System.out.println(firstNonRepeatedCharacter("aabbbbbccfffffgghh"));
        }catch(RuntimeException e){
            System.out.println("no non repeating value exists");
        }

    }
}
