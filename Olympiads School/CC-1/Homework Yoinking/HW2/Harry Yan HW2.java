import java.util.ArrayList;
import java.util.Objects;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main
{
    public static void main(String[] args)
    {
        System.out.print("Type \"Done\" to end.");
        Scanner s = new Scanner(System.in);
        ArrayList<Integer> nums = new ArrayList<>();
        ArrayList<Integer> printNums = new ArrayList<>();
        String range = "";
        for (int i = 0; i<10000000; i++)
        {
            String next = s.nextLine();
            if(Objects.equals(next, "Done"))
            {
                break;
            }
            range = range + "  " + next;



        }


        Pattern p = Pattern.compile("(\\d+) (\\d+)");
        Matcher m = p.matcher(range);
        while(m.find())
        {
            nums.clear();
            printNums.clear();
            nums.add(Math.min(Integer.parseInt(m.group(1)), Integer.parseInt(m.group(2))));
            nums.add(Math.max(Integer.parseInt(m.group(1)), Integer.parseInt(m.group(2))));
            for (int i = 0; i< nums.size()/2; i++)
                for(int r = nums.get(i); r<=nums.get(i+1); r++)

                {
                    int numCount = 0;
                    int e = r;
                    while(e!=1)
                    {

                        if (e % 2 == 0)
                        {
                            e = e/2;
                            numCount++;
                        }
                        else if(e%2 != 0)
                        {
                            e = 3*e+1;
                            numCount++;
                        }
                        printNums.add(numCount+1);

                    }


                }

            int greatest = 0;
            for (int i = 0; i< printNums.size(); i++)
            {
                if (printNums.get(i)>greatest)
                {
                    greatest = printNums.get(i);
                }
            }
            System.out.print(m.group(1)+" "+m.group(2)+" "+greatest+"\n");

        }
    }
}