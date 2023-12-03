package day_1;

import java.util.*;
import java.io.*;
public class Part1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("src/day_1/input.txt"));
        ArrayList<String> input = new ArrayList<>();
        while (scanner.hasNext()){
            input.add(scanner.next());
        }
        int total = 0;
        for (int i = 0; i< input.size(); i++) {
            String str = addNumbers(input.get(i));
            String firstNum, secondNum;
            firstNum = "Hi";
            secondNum = "";
            for (int j = 0; j < str.length(); j++){
                if (str.substring(j, j+1).compareTo("0") >= 0 && str.substring(j, j+1).compareTo("9") <= 0){
                    if (firstNum.equals("Hi")) firstNum = str.substring(j, j+1);
                    else secondNum = str.substring(j, j+1);
                }
            }
            if (secondNum.equals(""))
                secondNum = firstNum;
            String totNum = firstNum+secondNum;
            total += Integer.parseInt(totNum);
            System.out.println(totNum);
        }
        System.out.println(total);
    }

    public static List<String> letters = Arrays.asList("one", "two", "three", "four", "five", "six", "seven", "eight", "nine");

    public static String addNumbers(String str) {
        for (String j : letters) {
            for (int k = 0; k < 3; k++)
                if (str.contains(j)) str = str.substring(0, str.indexOf(j) + 1) + (letters.indexOf(j) + 1) + str.substring(str.indexOf(j) + 1);
        }
        return str;
    }
}