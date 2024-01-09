/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <iostream>
#include <stack> // Include the <stack> header
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        std::vector<int> leaves1, leaves2;
        getLeaves(root1, leaves1);
        getLeaves(root2, leaves2);
        return leaves1 == leaves2;
    }
        
private:
    void getLeaves(TreeNode* root, std::vector<int>& leaves) {
        if (root == nullptr) {
            return;
        }
        if (root->left == nullptr && root->right == nullptr) {
            leaves.push_back(root->val);
        }
        getLeaves(root->left, leaves);
        getLeaves(root->right, leaves);
    }
};

int main() {
    // Create the first binary tree
    TreeNode* root1 = new TreeNode(3);
    root1->left = new TreeNode(5);
    root1->left->left = new TreeNode(6);
    root1->left->right = new TreeNode(2);
    root1->left->right->left = new TreeNode(7);
    root1->left->right->right = new TreeNode(4);
    root1->right = new TreeNode(1);
    root1->right->left = new TreeNode(9);
    root1->right->right = new TreeNode(8);

    // Create the second binary tree
    TreeNode* root2 = new TreeNode(3);
    root2->left = new TreeNode(5);
    root2->left->left = new TreeNode(6);
    root2->left->right = new TreeNode(7);
    root2->right = new TreeNode(1);
    root2->right->left = new TreeNode(4);
    root2->right->right = new TreeNode(2);
    root2->right->right->left = new TreeNode(9);
    root2->right->right->right = new TreeNode(8);

    // Create a Solution object
    Solution solution;

    // Call the leafSimilar function
    bool result = solution.leafSimilar(root1, root2);

    // Print the result
    std::cout << (result ? "true" : "false") << std::endl;

    return 0;
}