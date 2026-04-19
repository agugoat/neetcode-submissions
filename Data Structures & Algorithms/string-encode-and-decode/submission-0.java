class Solution {

    public String encode(List<String> strs) {
    StringBuilder sb = new StringBuilder();

    for (String s : strs) {
       sb.append(s.length()).append("!").append(s);
    }

    String result = sb.toString();

    System.out.print(result);
   
   return result;

    }

    public List<String> decode(String str) {
    List<String> lst = new ArrayList<>();
    int i = 0;

    while (i < str.length()) {
    int colIndex = str.indexOf('!', i);
    int length = Integer.parseInt(str.substring(i, colIndex));
    i = colIndex + length + 1;
    // manually moving the index past length
    String code = str.substring(colIndex+1, i);
       lst.add(code);

}
     return lst;
    }
}