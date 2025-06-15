#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> multiplyMatrices(const vector<vector<int>>& matrix1,
                                               const vector<vector<int>>& matrix2) {
    int rows1 = matrix1.size();
    int cols1 = matrix1[0].size();
    int cols2 = matrix2[0].size();
    vector<vector<int>> result(rows1, vector<int>(cols2, 0));
    for (int i = 0; i < rows1; ++i) {
        for (int j = 0; j < cols2; ++j) {
            for (int k = 0; k < cols1; ++k) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
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
                                             {4, 5, 6}};
    vector<vector<int>> matrix2 = {{7, 8},
                                             {9, 10},
                                             {11, 12}};
    cout << "Matrix 1:" << endl;
    displayMatrix(matrix1);
    cout << "Matrix 2:" << endl;
    displayMatrix(matrix2);
    vector<vector<int>> product = multiplyMatrices(matrix1, matrix2);
    cout << "Product of Matrices:" << endl;
    displayMatrix(product);
    return 0;
}
