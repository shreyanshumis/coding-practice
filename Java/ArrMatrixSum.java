import java.beans.PropertyEditorSupport;

public class ArrMatrixSum {
    public static void main(String[] args) {
        int[][] mat1 = {{1, 2, 3}, {4, 5, 6}};
        int[][] mat2 = {{2, 4, 4}, {3, 3, 11}};
        int [][] res = {{0,0,0},{0,0,0}};
        //Matrix addition
        for (int i = 0; i < mat1.length; i++) {//row no. of times
            for (int j = 0; j < mat1[i].length; j++) {//coln. no of times
                System.out.format("Setting values for i=%d and j=%d\n", i,j);
                res[i][j]= mat1[i][j] + mat2[i][j];
            }
        }

        for (int i = 0; i < mat1.length; i++) {//row no. of times
            for (int j = 0; j < mat1[i].length; j++) {//coln. no of times
                System.out.format(res[i][j] + " ");
                res[i][j]= mat1[i][j] + mat2[i][j];
            }
            System.out.println("");
        }
    }
}