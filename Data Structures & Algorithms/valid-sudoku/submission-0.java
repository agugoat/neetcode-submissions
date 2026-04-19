class Solution {
    public boolean isValidSudoku(char[][] board) {
     // doesnt contain dups
     return !containsDups(board);
    }
    private static boolean containsDups(char [][] board) {     
        // Check each row and column
        for (int i = 0; i < 9; i++) {
            Set<Character> rowSet = new HashSet<>();
            Set<Character> colSet = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                // Check row
                if (board[i][j] != '.') {
                    if (rowSet.contains(board[i][j])) {
                        return true;  // Duplicate found in row
                    }
                    rowSet.add(board[i][j]);
                }
                // Check column
                // flip dat shit to check the collums
                if (board[j][i] != '.') {
                    if (colSet.contains(board[j][i])) {
                        return true;  // Duplicate found in column
                    }
                    colSet.add(board[j][i]);
                }
            }
        }

        // Check each 3x3 sub-box
        for (int row = 0; row < 9; row += 3) {
            for (int col = 0; col < 9; col += 3) {
        // loops to 9, skips every 3 to get that 3x3 subbox
                Set<Character> boxSet = new HashSet<>();
                for (int i = row; i < 3; i++) {
                    for (int j = col; j < 3; j++) {
                    // now looping through each subox to check
                        if (board[i][j] != '.') {
                            if (boxSet.contains(board[i][j])) {
                                return true;  // Duplicate found in sub-box
                            }
                            boxSet.add(board[i][j]);
                        }
                    }
                }
            }
        }

        return false; // No duplicates found
    }
}
      



    

