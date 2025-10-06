import java.util.*;

public class Leo_Luo_HW2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String nums = input.nextLine();
        String[] numbers = nums.split(" ");
        int i = Integer.parseInt(numbers[0]);
        int j = Integer.parseInt(numbers[1]);
        int start = Math.min(i, j);
        int end = Math.max(i, j);
        int maxCycleCount = 0;
        if (start > 0 && end < 1000000) {
            if (i < j) {
                for (int a = i; a < j; a++) {
                    int cycleCount = 1;
                    int n = a;
                    while (n != 1) {
                    if (n % 2 != 0) {
                        n = n * 3 + 1;
                        cycleCount++;
                    } else {
                        n /= 2;
                        cycleCount++;
                    }
                    if (cycleCount > maxCycleCount) {
                        maxCycleCount = cycleCount;
                    }
                    }
                }
            }
            System.out.println(i + " " +  j + " " + maxCycleCount);
        }
    }
}
