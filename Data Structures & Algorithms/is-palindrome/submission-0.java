class Solution {
    public boolean isPalindrome(String s) {

     String filtered = s.toLowerCase();
     String donnos = filtered.replaceAll("[^a-z0-9]", "");
    
    String reversed = new StringBuilder(donnos).reverse().toString();

    return donnos.equals(reversed);


    }
}
