// The following is the solution to Spiral Matrix problem on leetcode
// The code below is not copied && is my own implementation
// Problem statement: Given an m x n matrix, return all elements of the matrix in spiral order.
// Link to problem: https://leetcode.com/problems/spiral-matrix/

#include<iostream>
#include<vector>

using namespace std;

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        if (matrix.size() == 1)
        {
            return matrix[0];
        }

        vector<int> res;

        vector<vector<bool>> vis(matrix.size(), vector<bool>(matrix[0].size(), false));
        goRight(matrix, vis, res, 0, 0);

        return res;
    }

    void goRight(vector<vector<int>> &mat, vector<vector<bool>> &vis, vector<int> &res, int i, int j)
    {
        while (j < mat[0].size() && vis[i][j] == false)
        {
            res.push_back(mat[i][j]);
            vis[i][j++] = true;
        }

        j--;

        if (i + 1 < mat.size() && vis[i + 1][j] == false)
        {
            goDown(mat, vis, res, i + 1, j);
        }
    }

    void goDown(vector<vector<int>> &mat, vector<vector<bool>> &vis, vector<int> &res, int i, int j)
    {
        while (i < mat.size() && vis[i][j] == false)
        {
            res.push_back(mat[i][j]);
            vis[i++][j] = true;
        }

        i--;

        if (j - 1 >= 0 && vis[i][j - 1] == false)
        {
            goLeft(mat, vis, res, i, j - 1);
        }
    }

    void goLeft(vector<vector<int>> &mat, vector<vector<bool>> &vis, vector<int> &res, int i, int j)
    {
        while (j >= 0 && vis[i][j] == false)
        {
            res.push_back(mat[i][j]);
            vis[i][j--] = true;
        }

        j++;

        if (i - 1 >= 0 && vis[i - 1][j] == false)
        {
            goUp(mat, vis, res, i - 1, j);
        }

        cout << "i=" << i << "\n";
    }

    void goUp(vector<vector<int>> &mat, vector<vector<bool>> &vis, vector<int> &res, int i, int j)
    {
        while (i >= 0 && vis[i][j] == false)
        {
            res.push_back(mat[i][j]);
            vis[i--][j] = true;
        }

        i++;

        if (j + 1 < mat[0].size() && vis[i][j + 1] == false)
        {
            goRight(mat, vis, res, i, j + 1);
        }
    }
};