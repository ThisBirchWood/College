import java.util.Scanner;
import java.util.HashMap;

public class strings {
    public static void main(String[] args) {

        // get 2 inputs
        Scanner sc = new Scanner(System.in);    //setup scanner object
        System.out.print("Line 1: ");   // print "Line 1: " to the terminal
        String string1 = sc.nextLine();   // read what user typed and store in "string1"
        
        System.out.print("Line 2: ");   // print "Line 2: " to terminal
        String string2 = sc.nextLine();   // read what user typed and store in "string2"

        sc.close(); //close scanner

        // add two strings
        String result = string1 + ' ' + string2;    // concat the two strings
        int length = 0; // set length to 0
        
        // calculate length
        for (int i = 0; i < result.length(); i++){  // loop through all the characters in the result string
            if (result.charAt(i) != ' '){   // if the char is not a space char
                length += 1;    // add one to length var
            }
        }

        // setup a hash map to get count of each char in the string
        HashMap<Character, Integer> letterCount = new HashMap<Character, Integer>();    // setup hash map with keys as chars and values as integers
        for (int i = 0; i < result.length(); i++){  // iterate through the result string
            char key = Character.toLowerCase(result.charAt(i)); // get that char and make it lower case and make "key" var
            // exclude whitespace
            if (key != ' '){   // check if key var is an space char
                if (letterCount.containsKey(key)){  // check if value exists in hashmap
                    // increment if exists in hashmap
                    letterCount.merge(key, 1, Integer::sum);
                } else { // doesn't exist in hashmap
                    // add to hashmap
                    letterCount.put(key, 1);
                }
            }
        }

        // print result, length and reversed st ring
        System.out.println(result); // print result
        System.out.println("Length: " + length);    // print length of result excluding whitespace
        System.out.println(reverse_words(result));  // use the reverse_words function to print the string in reverse order

        // iterate through hashmap and print letters with an assigned value of 2
        for (Character key : letterCount.keySet()){ // iterate through the keys in the hashmap
            if (letterCount.get(key) == 2){ // if the value associated with the key is 2
                System.out.print(key);  // print the key
            }
        }

    }

    public static String reverse_words(String text){
        // split string on space, to split by words
        String[] temp = text.split(" ");    // split on space, store in list called temp
        String new_string = "";     // setup new string that will be returned

        // reverse iterate through list and add to string
        for (int i = temp.length-1; i >= 0; i--){   // reverse iterate, start at the last value and go down
            if (i != 0){    // if it's not the first element in the list
                new_string += (temp[i] + " ");  // add that word to the new string and add an extra space at the end
            } else {    // if it is the first element in "text" element
                new_string += temp[i]; // add word to new_string but no extra space
            }
            
        }
        // return the reversed string
        return new_string;
    }
}
