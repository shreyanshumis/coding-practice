#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> transposeMatrix(const vector<vector<int>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    vector<vector<int>> transpose(cols, vector<int>(rows));
    for (int i = 0; i < cols; ++i) {
        for (int j = 0; j < rows; ++j) {
            transpose[i][j] = matrix[j][i];
        }
    }
    return transpose;
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
    vector<vector<int>> matrix = {{1, 2, 3},
                                            {4, 5, 6},
                                            {7, 8, 9}};
    cout << "Original Matrix:" << endl;
    displayMatrix(matrix);
    vector<vector<int>> transpose = transposeMatrix(matrix);
    cout << "Transpose Matrix:" << endl;
    displayMatrix(transpose);
    return 0;
}
