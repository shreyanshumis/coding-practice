#include <iostream>
using namespace std;
struct Node {
    int data;
    Node* left;
    Node* right;
};
Node* createNode(int value) {
    Node* newNode = new Node();
    if (!newNode) {
        cout << "Memory allocation error!" << endl;
        return NULL;
    }
    newNode->data = value;
    newNode->left = newNode->right = NULL;
    return newNode;
}
Node* insertNode(Node* root, int value) {
    if (root == NULL) {
        return createNode(value);
    }
    if (value < root->data) {
        root->left = insertNode(root->left, value);
    }
    else if (value > root->data) {
        root->right = insertNode(root->right, value);
    }
    return root;
}
void preorderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    cout << root->data << " ";
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}
void inorderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    inorderTraversal(root->left);
    cout << root->data << " ";
    inorderTraversal(root->right);
}
void postorderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    postorderTraversal(root->left);
    postorderTraversal(root->right);
    cout << root->data << " ";
}
int main() {
    Node* root = NULL;
    int choice, value;
    do {
        cout << "Binary Search Tree Operations" << endl;
        cout << "1. Insert a node" << endl;
        cout << "2. Display in Preorder" << endl;
        cout << "3. Display in Inorder" << endl;
        cout << "4. Display in Postorder" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice) {
        case 1:
            cout << "Enter value to be inserted: ";
            cin >> value;
            root = insertNode(root, value);
            break;
        case 2:
            cout << "Preorder Traversal: ";
            preorderTraversal(root);
            cout << endl;
            break;
        case 3:
            cout << "Inorder Traversal: ";
            inorderTraversal(root);
            cout << endl;
            break;
        case 4:
            cout << "Postorder Traversal: ";
            postorderTraversal(root);
            cout << endl;
            break;
        case 5:
            cout << "Exiting..." << endl;
            break;
        default:
            cout << "Invalid choice! Please enter a valid option." << endl;
        }
    } while (choice != 5);
    return 0;
}
