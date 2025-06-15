#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> addMatrices(const vector<vector<int>>& matrix1,
                                          const vector<vector<int>>& matrix2) {
    int rows = matrix1.size();
    int cols = matrix1[0].size();
    vector<vector<int>> result(rows, vector<int>(cols));
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
    return result;
}
void displayMatrix(const vector<vector<int>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}
int main() {
    vector<vector<int>> matrix1 = {{1, 2, 3},
                                             {4, 5, 6},
                                             {7, 8, 9}};
    vector<vector<int>> matrix2 = {{9, 8, 7},
                                             {6, 5, 4},
                                             {3, 2, 1}};
    cout << "Matrix 1:" << endl;
    displayMatrix(matrix1);
    cout << "Matrix 2:" << endl;
    displayMatrix(matrix2);
    vector<vector<int>> sum = addMatrices(matrix1, matrix2);
    cout << "Sum of Matrices:" << endl;
    displayMatrix(sum);
    return 0;
}
