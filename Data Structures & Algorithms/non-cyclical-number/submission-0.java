class Solution {
    public boolean isHappy(int n) {
    Set<Integer> set = new HashSet<>();

    while(n != 1 && !set.contains(n)) {
        set.add(n);
     n = sumOfSquares(n);
    }
    if (n==1) {
        return true;
    } else {
        return false;
    }

   

    }

private static int sumOfSquares(int n) {
    int sum = 0;
    while(0 < n) {
      int last = n%10;
      sum += last * last;
      n/=10;
      // removing the last digit
    }
    return sum;
}
}
