// amount of time for binary tree to be infected

#include <iostream>
#include <stack> // Include the <stack> header
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
    TreeNode() : val(0), left(nullptr), right(nullptr), parent(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr), parent(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right, TreeNode *parent) : val(x), left(left), right(right), parent(parent) {}
};

class Solution {
public:
    int minTime(TreeNode* root, int start) {
        std::unordered_map<int, TreeNode*> nodeMap;
        std::unordered_set<int> visited;
        std::queue<TreeNode*> q;
        int maxDepth = 0;

        buildMap(root, nullptr, nodeMap);

        q.push(nodeMap[start]);
        visited.insert(start);
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left && visited.find(node->left->val) == visited.end()) {
                    q.push(node->left);
                    visited.insert(node->left->val);
                }
                if (node->right && visited.find(node->right->val) == visited.end()) {
                    q.push(node->right);
                    visited.insert(node->right->val);
                }
                if (node->parent && visited.find(node->parent->val) == visited.end()) {
                    q.push(node->parent);
                    visited.insert(node->parent->val);
                }
            }
            maxDepth++;
        }

        return maxDepth - 1; // Subtract 1 because the depth is 1-indexed
    }

private:
    void buildMap(TreeNode* node, TreeNode* parent, std::unordered_map<int, TreeNode*>& nodeMap) {
        if (node == nullptr) {
            return;
        }
        node->parent = parent;
        nodeMap[node->val] = node;
        buildMap(node->left, node, nodeMap);
        buildMap(node->right, node, nodeMap);
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

    Solution solution;
        int start = 3; // replace with the actual start node value
        std::cout << solution.minTime(root1, start) << std::endl;
    return 0;
}

// The time complexity is O(n) and the space complexity is O(n)

// testcase 


